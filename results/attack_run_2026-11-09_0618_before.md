# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 06:18
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `815a6d39-28dc-4d62-a7e2-5124271a19fa` | human | 0.331 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `5cc6d35e-8c21-4c2b-a87f-b00bf33bfc31` | unsure | 0.415 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c8ac5d53-defa-4a22-b1d7-800264ccec1a` | unsure | 0.590 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `37fb6491-a3c7-4271-aee0-11c523bc7e3e` | unsure | 0.624 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `106ac1e1-6e53-4737-a166-0669c8c91a68` | human | 0.378 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `34cfa9cc-82b8-4907-ae0f-c555f705816c` | unsure | 0.495 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `a8dd153a-7c31-4c31-90a0-14118fbe6a02` | unsure | 0.584 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `138d7871-77e2-4413-b7dd-ab8c88ecb247` | human | 0.351 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `81e77971-065b-40bf-b499-ed52f2edafc0` | unsure | 0.614 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `8bbfe789-7d32-4cf3-8967-7e03525d1b6e` | ai | 0.817 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `bc89c04d-94d9-4cf8-bd9a-db3e6c8b4782` | unsure | 0.595 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `43f64061-9cd6-4d32-a43c-999f8e35f451` | ai | 0.701 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ca02c479-204e-44ff-b1b3-950715ff2ed8` | ai | 0.714 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `93322aae-9fbd-4c5e-a9e5-65df5dc472a5` | ai | 0.667 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `36e9bfd2-4110-42be-ba97-26b5fd486257` | ai | 0.745 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `98259488-1636-4029-8db1-97575474b3d9` | ai | 0.659 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `15a8dbb0-7776-43f8-9a80-9ecb7037b7bd` | ai | 0.661 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `0000e1f0-a0fe-4ff3-8286-3e322ce14264` | unsure | 0.404 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7c77530e-d542-4443-a686-4b5cfc85ede7` | unsure | 0.438 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e640e8ab-d370-4dc5-8619-1d11b4ee99ac` | human | 0.282 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `3a2a00f6-e1ba-459c-a459-49e9fd175b97` | unsure | 0.554 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `2d4c62c6-b3da-4642-bbfc-8b9764687c5c` | unsure | 0.523 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c68697b8-0635-4e60-8d62-d3fdae96fcc8` | human | 0.392 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `b53ec00e-0817-4664-8b3e-eb2a3443fe12` | unsure | 0.568 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `0e7a56e4-3c50-4661-b9ea-109146967451` | human | 0.233 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `1e107e80-fa0d-45df-b8c3-90a3ebaceced` | human | 0.357 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `cf1cd52f-bc68-4a05-a9a1-2773420e9985` | ai | 0.782 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `729138d4-8603-46c5-9e59-f203fde0f564` | ai | 0.999 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `2d4e7b70-8662-4ab4-ad3b-44aab4da73c2` | ai | 0.953 | BROKE |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7c34ddaf-ff0f-4106-aa58-63298bd5dca4` | human | 0.252 | N/A |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `44566b63-8d32-4623-a6f7-d62fd4f39678` | human | 0.252 | N/A |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8e5a7148-597f-47b7-97f2-dbd2fb1ad24b` | human | 0.252 | N/A |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4708d7c6-747c-4160-951c-e19814cc2507` | human | 0.252 | N/A |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8b99043d-672c-47b8-95af-e2e9fd84b2ea` | human | 0.252 | N/A |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aa0f6669-4895-499e-acd6-2a212e477975` | human | 0.252 | N/A |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e00e79f0-87cf-42e7-8a73-b1a461d165d8` | human | 0.252 | N/A |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e4ed18b0-1131-4dda-9e05-d0cb343ab547` | human | 0.252 | N/A |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e2f53153-bb0d-40c9-9e0a-f95a77bcf9d9` | human | 0.252 | N/A |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dded0e31-0cd0-4171-9e25-fb9f9022d029` | human | 0.252 | N/A |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `807038ba-e00f-4187-9c08-4ce8dbff073a` | human | 0.252 | N/A |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c7b1473e-dc03-4283-b0f3-958a6b761580` | human | 0.252 | N/A |

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
  "content_id": "815a6d39-28dc-4d62-a7e2-5124271a19fa",
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
  "content_id": "5cc6d35e-8c21-4c2b-a87f-b00bf33bfc31",
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
  "content_id": "c8ac5d53-defa-4a22-b1d7-800264ccec1a",
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
  "content_id": "37fb6491-a3c7-4271-aee0-11c523bc7e3e",
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
  "content_id": "106ac1e1-6e53-4737-a166-0669c8c91a68",
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
  "content_id": "34cfa9cc-82b8-4907-ae0f-c555f705816c",
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
  "content_id": "a8dd153a-7c31-4c31-90a0-14118fbe6a02",
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
  "content_id": "138d7871-77e2-4413-b7dd-ab8c88ecb247",
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
  "content_id": "81e77971-065b-40bf-b499-ed52f2edafc0",
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
  "content_id": "8bbfe789-7d32-4cf3-8967-7e03525d1b6e",
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
  "content_id": "bc89c04d-94d9-4cf8-bd9a-db3e6c8b4782",
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
  "content_id": "43f64061-9cd6-4d32-a43c-999f8e35f451",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7008,
  "model_score": 0.7387,
  "style_score": 0.663,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "ca02c479-204e-44ff-b1b3-950715ff2ed8",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7137,
  "model_score": 0.8051,
  "style_score": 0.6223,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "93322aae-9fbd-4c5e-a9e5-65df5dc472a5",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.667,
  "model_score": 0.8329,
  "style_score": 0.5776,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "36e9bfd2-4110-42be-ba97-26b5fd486257",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.745,
  "model_score": 0.8005,
  "style_score": 0.6894,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "98259488-1636-4029-8db1-97575474b3d9",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6588,
  "model_score": 0.8814,
  "style_score": 0.5389,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "15a8dbb0-7776-43f8-9a80-9ecb7037b7bd",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6614,
  "model_score": 0.8816,
  "style_score": 0.5429,
  "label": "We think this was most likely written by an AI system, not a person. If you wrote this yourself, you can appeal this decision and tell us why below.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "0000e1f0-a0fe-4ff3-8286-3e322ce14264",
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
  "content_id": "7c77530e-d542-4443-a686-4b5cfc85ede7",
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
  "content_id": "e640e8ab-d370-4dc5-8619-1d11b4ee99ac",
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
  "content_id": "3a2a00f6-e1ba-459c-a459-49e9fd175b97",
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
  "content_id": "2d4c62c6-b3da-4642-bbfc-8b9764687c5c",
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
  "content_id": "c68697b8-0635-4e60-8d62-d3fdae96fcc8",
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
  "content_id": "b53ec00e-0817-4664-8b3e-eb2a3443fe12",
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
  "content_id": "0e7a56e4-3c50-4661-b9ea-109146967451",
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
  "content_id": "1e107e80-fa0d-45df-b8c3-90a3ebaceced",
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
  "content_id": "cf1cd52f-bc68-4a05-a9a1-2773420e9985",
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
  "content_id": "729138d4-8603-46c5-9e59-f203fde0f564",
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
  "content_id": "2d4e7b70-8662-4ab4-ad3b-44aab4da73c2",
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
  "content_id": "7c34ddaf-ff0f-4106-aa58-63298bd5dca4",
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
  "content_id": "44566b63-8d32-4623-a6f7-d62fd4f39678",
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
  "content_id": "8e5a7148-597f-47b7-97f2-dbd2fb1ad24b",
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
  "content_id": "4708d7c6-747c-4160-951c-e19814cc2507",
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
  "content_id": "8b99043d-672c-47b8-95af-e2e9fd84b2ea",
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
  "content_id": "aa0f6669-4895-499e-acd6-2a212e477975",
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
  "content_id": "e00e79f0-87cf-42e7-8a73-b1a461d165d8",
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
  "content_id": "e4ed18b0-1131-4dda-9e05-d0cb343ab547",
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
  "content_id": "e2f53153-bb0d-40c9-9e0a-f95a77bcf9d9",
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
  "content_id": "dded0e31-0cd0-4171-9e25-fb9f9022d029",
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
  "content_id": "807038ba-e00f-4187-9c08-4ce8dbff073a",
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
  "content_id": "c7b1473e-dc03-4283-b0f3-958a6b761580",
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
