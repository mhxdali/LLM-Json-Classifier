# Text Classifier with Structured JSON Output

A small Python script that classifies a sentence as `complaint`, `inquiry` or `praise` with the Gemini API and reads the answer back as JSON.

## What I did

- Built the classifier: a prompt that asks for `{"category": "...", "confidence": 0.0}`, parsed with `json.loads`.
- Compared **zero-shot** (no examples) with **few-shot** (3 examples) on 5 fixed sentences, including sarcasm and mixed-sentiment cases. One run per sentence.
- Broke it on purpose: a sentence with no meaning, and a prompt asking for JSON inside a markdown code block.

| | zero-shot | few-shot |
|---|---|---|
| Correct category | 5 / 5 | 5 / 5 |
| Valid JSON | 4 / 5 | 5 / 5 |

## What I learned

- A model can ignore "return ONLY JSON": one zero-shot reply came back wrapped in a markdown block, and `json.loads` rejected it even though the content was correct.
- Valid JSON is not the same as the JSON I need. When I removed the format description from the prompt, the model chose its own fields and left out `confidence`.
- The model always picks a category. For a meaningless sentence it returned `praise` with confidence `0.2`, so the confidence value is what shows it was unsure. It is a number the model reports, not a measured probability.
- Few-shot had no format error in my run and zero-shot had one, but that is one sentence out of five from a single run, so I cannot say the examples caused it.
- Not every failure is the model's: three calls failed with `503 UNAVAILABLE` (server overloaded) and my script crashed because it had no error handling.

## Limits

5 sentences, one run each, one model, English only. Some predictions were written after running, not before.
