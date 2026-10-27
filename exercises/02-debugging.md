# 02 - Debugging and troubleshooting (40 min, ~8 requests)

**Goal:** practise three common ways bugs reach you - a failing test, a symptom in
production, and a vague report from a human - and use AI without letting it guess.

**Why this matters:** AI is happy to jump straight to a confident fix. Without a
reproduction you can't tell whether it fixed the real bug, and without reading the
diff you won't notice when it "fixes" a test instead of the code. The loop below
keeps you in control and gives the AI the evidence it needs.

**The workflow for every bug:**
1. Reproduce (failing test or exact steps)
2. Explain (root cause, quoting the rule) - in **Ask** mode
3. Fix (smallest change) - review the diff yourself
4. Verify (`python -m pytest -q`)

---

## Bug A - a failing test (~2 requests)
`tests/test_pricing.py::test_order_of_exactly_500_gets_volume_discount` fails.
You found the root cause in Exercise 01. Now:

> Fix the root cause in src/orders/pricing.py with the smallest possible change.
> Don't touch the tests. Show the diff.

Run the tests. Then ask yourself: would a reviewer understand the fix from the diff alone?

## Bug B - a production symptom (~3 requests)
Support forwards this line from the production log (`logs/orders-api.log`):

```
08:01:15.447Z INFO  GET /orders?page=3 200 2ms ... items=0
08:01:15.448Z WARN  frontend: page 3 rendered with 0 items but total_pages=3
```

Users also say "page 1 is missing the first orders". Two tests in
`tests/test_pagination.py` fail too.

Your task: give the AI the symptom **and** the tests, get an explanation, then fix.
Tip: ask it to explain *why both symptoms have the same cause* before it changes code.

## Bug C - a vague human report (~3 requests)
From customer support, no test exists:

> "A customer ordered on **Thursday 29 October**. The website promised delivery on
> **Monday 2 November**, but it arrived Tuesday. We get more of these complaints for
> orders placed late in the week. Is the website lying?"

The rule is in the docstring of `src/orders/delivery.py`.

1. **First**, ask the AI to turn the report into a failing pytest test in
   `tests/test_delivery.py`. Check that the expected date is right *by hand*
   (look at a calendar - don't trust the AI's date arithmetic blindly).
2. Run it - it must fail.
3. Then ask for the fix.

## Check yourself
- [ ] After Bug A: **2 failed, 10 passed**. The fix changed one line in `pricing.py`
- [ ] After Bug B: **all 12 tests pass**. One explanation covers both symptoms
- [ ] Bug C: your new test **failed before the fix** and passes after it
- [ ] You checked the expected date in Bug C yourself, on a calendar
- [ ] `git diff --stat` shows changes in `src/orders/` and your **new** test only. No
      existing test was edited or deleted

## Stuck?
- **Bug B:** pages are 1-based (`page=1` is the first page). Work out by hand which list
  positions page 1 and page 3 should return for 25 items with 10 per page, then compare
  with what the code computes.
- **Bug C:** write out the days from Thursday 29 October on paper, mark which ones are
  business days according to the docstring, and count. Then ask the AI how the code
  decides whether a day is a business day. (In Python, `weekday()` returns 0 for Monday.)
- **The AI wants to change a test?** Say no: "The test is correct. Change only the code."
- **The fix is huge?** Ask: "Undo that. Make the smallest possible change."

## Discuss
- Which bug did the AI find fastest? Which one did it get wrong first, and why?
- Bug C: did the AI calculate the expected date correctly? Who checked it?
- Did anyone's AI change a test to make it pass? (That's the most common trap.)
