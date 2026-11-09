# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 07:05
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `eb7808cb-2017-42a5-a2c0-dfa5c8e0efa0` | human | 0.331 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1ceff6e5-83d3-4e48-a362-b6fb0e9491b0` | unsure | 0.415 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `cb2cdd6c-39df-4e1d-82c6-99142f35452a` | unsure | 0.590 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `aae9dc44-3702-456c-b866-c527cac10d8a` | unsure | 0.624 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2b3ddb42-e6a9-4184-9fa8-191775c72c8e` | human | 0.378 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e1134946-9139-4622-b0ed-e8690697d714` | unsure | 0.495 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `9cef2f4c-2f00-40de-a6de-e735231a51ba` | unsure | 0.584 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `c905bd58-ea63-4d23-b989-9cbd8d60424b` | human | 0.351 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c81ead26-d073-4846-a789-d8d964ddf35a` | unsure | 0.614 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `7450ae28-efdb-43cb-88fc-1bfefd924c18` | ai | 0.817 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9de6e4e6-0245-41bf-bbf1-1ce73992bf0f` | unsure | 0.595 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `f562b1dc-cc71-4872-b35e-db6a27922a72` | unsure | 0.701 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `cd67c5d3-4565-4b41-bbc2-3d11f39b110d` | unsure | 0.714 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `0f214042-8e11-438d-801b-5bea7c36258f` | unsure | 0.667 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `700e5186-35cd-41c4-93c1-d2f77bc1365e` | unsure | 0.745 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `fe58cbf9-f8c3-40ef-a9de-f2d338afc24f` | unsure | 0.659 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `04b3b9a3-1466-4414-9ce2-6c4b86cba1e5` | unsure | 0.661 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `c1a167f7-6dc5-4d91-be55-6a001fdca9b8` | unsure | 0.404 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `13ec063d-109b-49d5-820d-2b05e5d43f9a` | unsure | 0.438 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `329295ce-a94f-4f7b-9c0f-9ee21917a3be` | human | 0.282 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c4e850cc-07a9-477a-b5fc-5c772993dfda` | unsure | 0.554 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `ff3070ec-327d-44b5-b142-1ecc434566ee` | unsure | 0.523 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f644d8e7-8aef-457b-8649-95e760bec4f0` | human | 0.392 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `aad45146-32d6-4972-a042-e33391c50fe0` | unsure | 0.568 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `6148225c-23c8-44df-bc69-11105af87410` | human | 0.233 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `ab1e1e8d-a8e1-42d7-8016-9da4dc5a1f0b` | human | 0.357 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `61ed5099-cb27-4d6d-b655-6ccb66330d6e` | ai | 0.782 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `6f3dbb3d-4324-46c4-8d6f-e0fb6ff37bc0` | ai | 0.999 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `a1798cde-aa23-46c2-884b-87748aa3ba26` | ai | 0.953 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5c0234b9-0fde-4348-84e0-3d52dbb40f3c` | human | 0.252 | N/A |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ff97a7d6-4332-4acc-99e6-3534dd50ea57` | human | 0.252 | N/A |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d354151a-a3d2-4077-b737-e852f7019e28` | human | 0.252 | N/A |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f2898aaa-130b-4c99-b03f-08f8895b93b7` | human | 0.252 | N/A |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f2fadb74-82fd-4ba7-9556-c6bd0607868d` | human | 0.252 | N/A |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `08112f87-98ea-4098-b594-f96753d11349` | human | 0.252 | N/A |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `facd2556-5076-4881-ad8b-0fb2d35647cc` | human | 0.252 | N/A |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ec5db1e6-88a1-43d7-aa53-9a17ed1e9271` | human | 0.252 | N/A |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2df35867-498e-4852-93cf-d357751e15ff` | human | 0.252 | N/A |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `963e38c8-9543-4082-8438-a9d24f9dacbd` | human | 0.252 | N/A |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f61fc4c9-5266-4279-a071-3ba306bf3079` | human | 0.252 | N/A |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eadff3da-4e97-494e-aa01-d1a95ecb48e3` | human | 0.252 | N/A |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "eb7808cb-2017-42a5-a2c0-dfa5c8e0efa0",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3313,
  "model_score": 0.1635,
  "style_score": 0.6428,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "1ceff6e5-83d3-4e48-a362-b6fb0e9491b0",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4152,
  "model_score": 0.5943,
  "style_score": 0.3187,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "cb2cdd6c-39df-4e1d-82c6-99142f35452a",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5903,
  "model_score": 0.6662,
  "style_score": 0.5144,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "aae9dc44-3702-456c-b866-c527cac10d8a",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6241,
  "model_score": 0.6114,
  "style_score": 0.6368,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2b3ddb42-e6a9-4184-9fa8-191775c72c8e",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3783,
  "model_score": 0.3212,
  "style_score": 0.4354,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "e1134946-9139-4622-b0ed-e8690697d714",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4947,
  "model_score": 0.5727,
  "style_score": 0.4167,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "9cef2f4c-2f00-40de-a6de-e735231a51ba",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.584,
  "model_score": 0.5862,
  "style_score": 0.5819,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c905bd58-ea63-4d23-b989-9cbd8d60424b",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3515,
  "model_score": 0.2452,
  "style_score": 0.5488,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c81ead26-d073-4846-a789-d8d964ddf35a",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6136,
  "model_score": 0.7042,
  "style_score": 0.5229,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "7450ae28-efdb-43cb-88fc-1bfefd924c18",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8166,
  "model_score": 0.9792,
  "style_score": 0.729,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "HELD"
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "9de6e4e6-0245-41bf-bbf1-1ce73992bf0f",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5953,
  "model_score": 0.6175,
  "style_score": 0.5731,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "f562b1dc-cc71-4872-b35e-db6a27922a72",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7008,
  "model_score": 0.7387,
  "style_score": 0.663,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "cd67c5d3-4565-4b41-bbc2-3d11f39b110d",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7137,
  "model_score": 0.8051,
  "style_score": 0.6223,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "0f214042-8e11-438d-801b-5bea7c36258f",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.667,
  "model_score": 0.8329,
  "style_score": 0.5776,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "700e5186-35cd-41c4-93c1-d2f77bc1365e",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.745,
  "model_score": 0.8005,
  "style_score": 0.6894,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "fe58cbf9-f8c3-40ef-a9de-f2d338afc24f",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6588,
  "model_score": 0.8814,
  "style_score": 0.5389,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "04b3b9a3-1466-4414-9ce2-6c4b86cba1e5",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6614,
  "model_score": 0.8816,
  "style_score": 0.5429,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c1a167f7-6dc5-4d91-be55-6a001fdca9b8",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4042,
  "model_score": 0.3223,
  "style_score": 0.4862,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "13ec063d-109b-49d5-820d-2b05e5d43f9a",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4376,
  "model_score": 0.4625,
  "style_score": 0.4128,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "329295ce-a94f-4f7b-9c0f-9ee21917a3be",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2824,
  "model_score": 0.2044,
  "style_score": 0.3605,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c4e850cc-07a9-477a-b5fc-5c772993dfda",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5539,
  "model_score": 0.5943,
  "style_score": 0.5136,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "ff3070ec-327d-44b5-b142-1ecc434566ee",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5234,
  "model_score": 0.4998,
  "style_score": 0.5471,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "f644d8e7-8aef-457b-8649-95e760bec4f0",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3924,
  "model_score": 0.6401,
  "style_score": 0.2591,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "aad45146-32d6-4972-a042-e33391c50fe0",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5684,
  "model_score": 0.5583,
  "style_score": 0.5784,
  "label": "We can't confidently tell whether this was written by a person or an AI system \u2014 our checks didn't clearly point either way. This isn't a judgment against you, and no action is needed on your part.",
  "error": null,
  "verdict": "HELD"
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "6148225c-23c8-44df-bc69-11105af87410",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2333,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "ab1e1e8d-a8e1-42d7-8016-9da4dc5a1f0b",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3573,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "61ed5099-cb27-4d6d-b655-6ccb66330d6e",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7825,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "6f3dbb3d-4324-46c4-8d6f-e0fb6ff37bc0",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "a1798cde-aa23-46c2-884b-87748aa3ba26",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "5c0234b9-0fde-4348-84e0-3d52dbb40f3c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "ff97a7d6-4332-4acc-99e6-3534dd50ea57",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "d354151a-a3d2-4077-b737-e852f7019e28",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "f2898aaa-130b-4c99-b03f-08f8895b93b7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "f2fadb74-82fd-4ba7-9556-c6bd0607868d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "08112f87-98ea-4098-b594-f96753d11349",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "facd2556-5076-4881-ad8b-0fb2d35647cc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "ec5db1e6-88a1-43d7-aa53-9a17ed1e9271",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "2df35867-498e-4852-93cf-d357751e15ff",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "963e38c8-9543-4082-8438-a9d24f9dacbd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 200,
  "content_id": "f61fc4c9-5266-4279-a071-3ba306bf3079",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 200,
  "content_id": "eadff3da-4e97-494e-aa01-d1a95ecb48e3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.252,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": "N/A"
}
```
