# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer's text and `creator_id` arrive as JSON at `POST /submit`.
2. The route validates the input — `text` must be a non-empty string under a
   size limit — and generates a fresh `content_id` (a UUID) for this piece of
   writing.
3. **Signal one** (`detector.model_signal`, in `detector.py`) runs a local
   language model over the text and returns a 0–1 score: how predictable the
   text is, where higher means more likely AI.
4. **Signal two** (`stylometry.style_signal`, in `stylometry.py`) measures the
   text's shape — sentence-length variation, vocabulary variety, punctuation
   density — and returns its own 0–1 score, same direction.
5. `scoring.combine_signals` merges the two 0–1 scores into one combined
   score.
6. `scoring.score_to_label` maps that combined score to a short `guess`
   (`ai` / `human` / `unsure`) and the full-sentence label text a reader
   actually sees, using the thresholds in `config.py`.
7. `audit.log_decision` writes one entry — timestamp, `content_id`,
   `creator_id`, guess, both signal scores, the combined score, the label, and
   status `decided` — to `logs/audit.jsonl`. The route then returns the
   `content_id`, guess, confidence, label, and both signal scores to the
   caller.

If a writer disputes the result, `POST /appeal` takes their `content_id` and
their reasoning, moves that item's status to `under_review`, and records the
appeal in the same log, next to the original decision.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
How surprised a local language model (gpt2) is by the text — its perplexity,
squashed onto a 0–1 scale. Low surprise (the model could have guessed the next
word) scores close to 1.0 (AI-like); high surprise scores close to 0.0
(human-like).

**Why that might differ between human and AI writing:**
A language model writes by repeatedly picking a likely next token, so text a
model produced tends to be text a model finds easy to predict. Human writing
wanders — odd word choices, abrupt turns, specific rather than typical phrasing
— which this model finds harder to predict.

**What it can't see:**
Predictability is not the same thing as authorship. This signal rewards common
words in short, ordinary sentences, whoever wrote them — so a non-native
English speaker sticking to vocabulary they're sure of, a younger writer, or
anyone writing plainly on purpose can score as machine-like as AI text does.
The reverse is also true: dense, ornate prose full of rare words often reads as
*human* here even when it's AI-generated, because rare words are exactly what
this model fails to predict. The writers it's most likely to accuse are the
ones with the least room to argue back — that's structural, not a bug.

### Signal two — the style signal

**What it measures:**
The text's shape, without reading a word of it: how much sentence length
varies, how much of the vocabulary repeats (unique words / total words), and
how dense the punctuation is. The three combine into one 0–1 score, same
direction as signal one.

**Why that might differ between human and AI writing:**
Generated prose tends toward even, mid-length sentences and a narrower band of
vocabulary, because that's what "most likely next word" produces on average.
Human writing is lumpier — a three-word sentence next to a forty-word one, more
varied word choice, more idiosyncratic punctuation.

**What it can't see:**
This signal cannot read. It has no idea what the text says or means. Anything
that changes the shape of the text without changing its substance moves the
score — adding typos, breaking a long sentence into short ones, pasting in a
quoted block. That's a very cheap thing to do on purpose, which is exactly what
makes it a blind spot rather than a corner case.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
When the two signals are within 0.25 of each other, combine them as a plain
50/50 weighted average. When they disagree by more than 0.25, don't average
straight through the disagreement — instead weight the lower (more
human-reading) score at 0.65 and the higher (more AI-reading) score at 0.35.
A missed detection costs the site less than a false accusation costs the
writer, so when the two methods can't agree, the benefit of the doubt goes to
the writer.

**The numbers:**
- `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5` (agreement case)
- `DISAGREEMENT_THRESHOLD = 0.25` (how far apart counts as a real split)
- `DISAGREEMENT_LOWER_WEIGHT = 0.65` (weight on the more-human-reading score
  when they split)

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
A plain, ordinary piece of human writing (a short diary-style paragraph about
a grocery trip) scored `model_score = 0.69` — signal one read its short,
common-word sentences as AI-predictable — but `style_score = 0.40`, because
its sentence lengths actually vary and it carries a semicolon and a dash,
which read as human. That's a 0.29 split, above the 0.25 threshold, so the
rule leans toward the lower score: `0.65 × 0.40 + 0.35 × 0.69 = 0.50`. A
straight 50/50 average would have landed at 0.545 — still "unsure" here, but
closer to the "ai" threshold (0.65) than the leaned result is, and a more
AI-ish version of the same plain writing could have crossed it under a plain
average. This is the exact false-positive scenario from Milestone 1: the
writer with the least room to argue back is the one this rule is designed to
protect.

I also found the opposite split on an AI-generated paragraph with typos added
to it as a cheap evasion attempt: `model_score` dropped to 0.33 (the typos
made the text look "surprising" to signal one) while `style_score` stayed at
0.58 (the sentence shapes were still AI-regular). That's a 0.24 split — just
under the disagreement threshold — so it combines as a plain average (0.45,
"unsure"). It isn't caught as AI, but it also isn't mislabeled as confidently
human; it lands in the band built for exactly this kind of uncertainty.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.40 | "We think this was most likely written by a person." |
| unsure | 0.40 – 0.65 | "We can't confidently tell whether this was written by a person or an AI system — our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part." |
| high-confidence AI | 0.65 – 1.00 | "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below." |

**Why I worded the "unsure" one this way:**
It needed to admit uncertainty without reading as half an accusation, because
the person seeing it may well have written every word themselves. I avoided
"this might be AI-generated" (still names AI first, still sounds like
suspicion) in favor of naming the uncertainty itself as the result — "our
checks didn't clearly point either way" puts the limitation on the system,
not on the writer. The closing line ("no action is needed on your part")
exists specifically so a writer landing here doesn't feel compelled to defend
themselves against a label that was built to not be an accusation.

**Why `HUMAN_THRESHOLD` moved from 0.35 to 0.40:** During calibration, a
genuinely literary human sample scored 0.363 — just above the original 0.35
cutoff — and landed in "unsure" instead of "human." Raising the human
threshold to 0.40 only moves the human/unsure boundary; it doesn't touch
`AI_THRESHOLD` (0.65) at all, so it has no effect on false-positive risk. It
only makes the human label easier to reach, which is the direction that
costs nothing.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables. It is also worth noting that proper testing is essential for ensuring reliability. Furthermore, the design should prioritize both scalability and maintainability. Finally, user feedback should be incorporated throughout the development process.", "creator_id": "test_ai"}'
```

```json
{
  "confidence": 0.741,
  "content_id": "7e97519c-ace4-4ea4-b30a-9b590fd99630",
  "guess": "ai",
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "model_score": 0.8577,
  "style_score": 0.6244
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "7e97519c-ace4-4ea4-b30a-9b590fd99630", "reasoning": "I wrote this myself as a formal essay for class. English is my second language, so I write carefully and plainly on purpose."}'
```

```json
{
  "content_id": "7e97519c-ace4-4ea4-b30a-9b590fd99630",
  "message": "Your appeal has been recorded and this item is now under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.3629,
      "content_id": "97123f46-9a71-429c-8dd6-89ca22def5bf",
      "creator_id": "test_human2",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.386,
      "status": "decided",
      "style_score": 0.3397,
      "timestamp": "2026-11-04T04:48:26+00:00"
    },
    {
      "combined_score": 0.741,
      "content_id": "7e97519c-ace4-4ea4-b30a-9b590fd99630",
      "creator_id": "test_ai",
      "guess": "ai",
      "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
      "model_score": 0.8577,
      "status": "decided",
      "style_score": 0.6244,
      "timestamp": "2026-11-04T04:47:13+00:00"
    },
    {
      "content_id": "7e97519c-ace4-4ea4-b30a-9b590fd99630",
      "creator_id": "test_ai",
      "event": "appeal",
      "reasoning": "I wrote this myself as a formal essay for class. English is my second language, so I write carefully and plainly on purpose.",
      "status": "under_review",
      "timestamp": "2026-11-04T04:48:33+00:00"
    }
  ]
}
```

Note the original `decided` entry for `7e97519c-...` stays untouched, and the
appeal sits after it with the new `under_review` status — the log is
append-only, so both the original decision and the challenge to it are
visible in order.

---

## How I Used AI

**Moment 1**

- *What I asked for:* Build the three stylometry measures and the
  `style_signal` combiner, then test it on four calibration inputs (clearly
  AI, clearly human, plain human, lightly-edited AI).
- *What came back:* The first pass used short, 1–3 sentence test snippets.
  The results were backwards — the "clearly human" sample scored 0.6852
  (more AI-like) and the "clearly AI" sample scored only 0.644. The signal
  wasn't discriminating at all.
- *What I changed:* Instead of accepting the numbers, I had it diagnose why
  before touching any code: short texts collapse `sentence_length_spread` to
  0.0 (fewer than two sentences means no spread to measure) and all land
  near-identical, artificially high `type_token_ratio` regardless of
  authorship. I had it rebuild the calibration inputs as longer, more
  realistic passages, which fixed the ordering and also produced a real,
  documented finding — short submissions are a blind spot for this signal —
  that's now written into the Signals and Scoring section rather than hidden.

**Moment 2**

- *What I asked for:* I gave two starting numbers for the acceptance
  criteria — false positives at most 20%, false negatives at most 20% — and
  asked for help drafting the remaining three criteria.
- *What came back:* It flagged that the brief explicitly warns against
  treating both error types as equally costly ("a criterion that treats both
  errors as equally bad is describing a system nobody would ship") and
  recommended tightening the false-positive target to 10% while leaving
  false negatives at 20%, citing the brief's own worked example.
- *What I changed:* I adopted the asymmetric numbers (FP ≤ 10%, FN ≤ 20%)
  instead of my original symmetric draft. I didn't take the suggestion on
  faith — I checked it against the brief's own stated reasoning (false
  accusations cost a real writer more than a missed detection costs the
  site) before agreeing it was the better target.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

Full run: `python run_attacks.py --set attack_set --label before` → 56 attacks,
0 crashes, written to `results/attack_run_2026-11-09_0618_before.md`.

**Held/broke methodology** (mine — the attack set doesn't supply this):
- `evasion`: BROKE only if it fully evaded to `human`. Landing in `unsure`
  counts as held — the system didn't commit to a wrong answer.
- `false_positive`: BROKE if genuine human writing landed `ai`.
- `prompt_injection`: BROKE if the injected instruction actually changed
  behavior.
- `malformed`: BROKE on a crash, **or** on a confident, specific guess
  returned for input that isn't prose at all (control characters, emoji,
  single-word walls of text, non-Latin script) — a non-crash 200 that still
  hands out a wrong, confident claim is a real failure, not a pass.
- `flood_same_creator`: N/A — this family has exactly 12 rows against my
  12/minute limit, so none crossed it. Not a limiter failure; the limiter is
  already proven separately by the Milestone 1 flood-15 test.

**Totals: 14 BROKE, 30 HELD, 12 N/A.**

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.331 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.415 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.590 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.624 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.378 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.495 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.584 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.351 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.614 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.817 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.595 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.701 | **BROKE** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.714 | **BROKE** |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.667 | **BROKE** |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.745 | **BROKE** |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.659 | **BROKE** |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.661 | **BROKE** |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.404 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.438 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.282 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.554 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.523 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | human | 0.392 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.568 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | human | 0.233 | **BROKE** |
| MF04 | malformed | text is only punctuation | 200 | human | 0.357 | **BROKE** |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.782 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | ai | 0.999 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.953 | **BROKE** |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01–12 | flood_same_creator | rapid submissions from one creator | 200 | human | 0.252 | N/A |

**By family**

| Family | Attacks | BROKE | HELD | N/A |
|---|---|---|---|---|
| `evasion` | 10 | 3 | 7 | — |
| `false_positive` | 8 | 6 | 2 | — |
| `prompt_injection` | 6 | 0 | 6 | — |
| `malformed` | 20 | 5 | 15 | — |
| `flood_same_creator` | 12 | — | — | 12 |

**Ten audit log entries from the run**

```json
{"creator_id": "attacker_FP03", "content_id": "ca02c479-204e-44ff-b1b3-950715ff2ed8", "guess": "ai", "model_score": 0.8051, "style_score": 0.6223, "combined_score": 0.7137, "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.", "status": "decided", "timestamp": "2026-11-09T11:17:55+00:00"}
{"creator_id": "attacker_FP05", "content_id": "36e9bfd2-4110-42be-ba97-26b5fd486257", "guess": "ai", "model_score": 0.8005, "style_score": 0.6894, "combined_score": 0.745, "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.", "status": "decided", "timestamp": "2026-11-09T11:17:56+00:00"}
{"creator_id": "attacker_MF07", "content_id": "2d4e7b70-8662-4ab4-ad3b-44aab4da73c2", "guess": "ai", "model_score": 0.9064, "style_score": 1.0, "combined_score": 0.9532, "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.", "status": "decided", "timestamp": "2026-11-09T11:18:02+00:00"}
{"creator_id": "attacker_MF06", "content_id": "729138d4-8603-46c5-9e59-f203fde0f564", "guess": "ai", "model_score": 0.9969, "style_score": 1.0, "combined_score": 0.9985, "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.", "status": "decided", "timestamp": "2026-11-09T11:18:01+00:00"}
{"creator_id": "attacker_EV10", "content_id": "8bbfe789-7d32-4cf3-8967-7e03525d1b6e", "guess": "ai", "model_score": 0.9792, "style_score": 0.729, "combined_score": 0.8166, "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.", "status": "decided", "timestamp": "2026-11-09T11:17:53+00:00"}
{"creator_id": "attacker_EV01", "content_id": "815a6d39-28dc-4d62-a7e2-5124271a19fa", "guess": "human", "model_score": 0.1635, "style_score": 0.6428, "combined_score": 0.3313, "label": "We think this was most likely written by a person.", "status": "decided", "timestamp": "2026-11-09T11:17:51+00:00"}
{"creator_id": "attacker_PI05", "content_id": "c68697b8-0635-4e60-8d62-d3fdae96fcc8", "guess": "human", "model_score": 0.6401, "style_score": 0.2591, "combined_score": 0.3924, "label": "We think this was most likely written by a person.", "status": "decided", "timestamp": "2026-11-09T11:17:59+00:00"}
{"creator_id": "attacker_RQ01", "event": "rejected", "reason": "text_missing", "status": "rejected", "ip": "127.0.0.1", "device_id": null, "verb": "POST", "timestamp": "2026-11-09T11:18:02+00:00"}
{"creator_id": "attacker_MF02", "event": "rejected", "reason": "detector_error", "detail": "Text is too short to score — a few sentences at least.", "status": "rejected", "ip": "127.0.0.1", "device_id": null, "verb": "POST", "timestamp": "2026-11-09T11:17:59+00:00"}
{"creator_id": "flood_tester", "event": "rejected", "reason": "rate_limited", "limit": "12 per 1 minute", "status": "rejected", "ip": "127.0.0.1", "device_id": null, "verb": "POST", "timestamp": "2026-11-05T00:53:21+00:00"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

The `false_positive` family as a whole: 6 of 8 (75%) genuine human writing
samples — a non-native English speaker writing carefully (`FP03`, 0.714), a
student essay written to a rubric (`FP04`), technical documentation (`FP05`,
0.745), a formal register (`FP02`), a formal template (`FP06`), and
deliberate repetition (`FP07`) — all landed `ai`. Zero landed `human`. This
isn't one unlucky input; it's the exact scenario Milestone 1 traced through
the service before a line of code existed, happening on 75% of the family
built to test for it, which blows straight through the ≤10% false-positive
target set in `criteria.md` before any results existed. `FP03` specifically
is the one I'd least want to explain: a careful, non-native-English writer,
told with 71% confidence they didn't write their own work.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
