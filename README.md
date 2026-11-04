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

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

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

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



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
