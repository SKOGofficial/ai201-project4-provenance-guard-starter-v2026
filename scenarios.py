"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # My own writing, typos and all. Not cleaned up — a detector that only
        # works on polished prose isn't the thing being tested here.
        "texts": [
            "the best computer for any individual is the one that meets their spesific demands within a budget limit. Obviosuly there are tradeoffs",
            "Sherwin Williams offers great paints for an office building",
            "how many woodchucks could chuck wood if they could - somedy probabily",
            "the largest industry in america is fiannce driving the global debt market ithink",
            "A tire on wheels is probabily not a car",
            "ElevenLabs is a great start up",
            "python is a beginer friendly language that avoids the nuances of a structured language like javea or C making it a terrbiel language for students to start learning",
            "there is a strong corrolation between chronic AI usage and reduction in cognitive function",
            "is AI the notes plato was talking about, how come something he considered blasphamous to human cognition is the main way, even healthy way to do learning, can the same thing be said about AI in the future",
            "I have a fovrite pancake and for the purposes of this assignment that information is not going to be shared",
        ],
    },
    {
        "name": "AI-generated texts",
        "criterion": 2,
        # AI-generated, varied topic and length, for the false-negative check.
        "texts": [
            "Neural networks are computational systems inspired by the structure of the human brain. They consist of layers of interconnected nodes, each of which processes information and passes it forward. During training, the network adjusts the strength of these connections based on the error between its predictions and the correct answers. Over many iterations, this process allows the network to recognize patterns it has never explicitly been told to look for.",
            "Introducing BrightPath, the all-in-one productivity app designed to help you stay organized. With intuitive task management, smart reminders, and seamless calendar integration, BrightPath makes it easy to focus on what matters most. Whether you're managing a team or simply trying to stay on top of daily errands, BrightPath adapts to your workflow.",
            "Every challenge is an opportunity in disguise. When we face setbacks, it is important to remember that growth often comes from discomfort. By embracing difficulty with an open mind, we position ourselves to learn valuable lessons that we might otherwise have missed.",
            "To prepare the dish, begin by gathering all necessary ingredients. First, chop the vegetables into even pieces to ensure consistent cooking. Next, heat the oil in a large pan over medium heat. Once the pan is hot, add the vegetables and stir occasionally for approximately eight minutes. Finally, season to taste and serve immediately while warm.",
            "City officials announced today that the new transit initiative will begin construction next month. The project, which has been in planning for over two years, aims to reduce commute times across several key corridors. Local residents have expressed a mix of support and concern regarding the expected disruption.",
            "Dear Team, I hope this message finds you well. I wanted to provide a brief update on the status of the quarterly report. We are currently on track to meet the deadline, and I appreciate everyone's continued effort. Please let me know if you have any questions or concerns moving forward.",
            "The old lighthouse stood at the edge of the cliff, its paint long faded by decades of salt and wind. No one in town could quite remember when it had last been lit, yet every evening, without fail, a faint glow could be seen from its highest window.",
            "Nestled along the coastline, this charming city offers visitors a perfect blend of history and natural beauty. Cobblestone streets wind past centuries-old architecture, while nearby beaches provide a relaxing escape from the bustle of downtown. Local cuisine, rich with fresh seafood, is not to be missed.",
            "Recycling plays a critical role in reducing the environmental impact of everyday consumption. By diverting waste from landfills, communities can conserve natural resources and reduce greenhouse gas emissions. It is essential that individuals and organizations alike commit to responsible recycling practices.",
            "Improving sleep quality starts with establishing a consistent routine. Experts recommend going to bed and waking up at the same time each day, even on weekends. Additionally, limiting screen exposure before bedtime and keeping the bedroom cool and dark can significantly improve rest.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Known calibration fixtures from Unit 7 (clearly AI, borderline) plus
        # one of my own pieces (clearly human) — see README for why this one.
        "texts": [
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables. It is also worth noting that proper testing is essential for ensuring reliability. Furthermore, the design should prioritize both scalability and maintainability. Finally, user feedback should be incorporated throughout the development process.",
            "the best computer for any individual is the one that meets their spesific demands within a budget limit. Obviosuly there are tradeoffs",
            "I went to the store yesterday. I needed milk, bread, and some eggs, but they were out of the bread I usually get so I grabbed a different kind. The checkout line was long -- maybe fifteen people -- and the guy in front of me paid entirely in coins, which took forever. I didn't mind too much. It was a good trip overall, even with the wait; sometimes that's just how it goes.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},               # no text field at all
            {"text": "", "creator_id": "eval_bad_empty"},     # empty text
            {"text": 42, "creator_id": "eval_bad_number"},    # non-string text
            {"text": "word " * 5000, "creator_id": "eval_bad_huge"},  # 25,000 chars
        ],
    },

    # Criterion 4 (the appeal path) needs a submission's real content_id before
    # an appeal can target it, which doesn't fit the texts/bodies shape here.
    # Tested by hand with curl instead — see README's Run Log and Verdicts.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
