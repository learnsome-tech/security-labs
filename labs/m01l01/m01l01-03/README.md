# m01l01-03 · Question one: where does the data actually go?

**Lesson:** [The Threat Model Habit](https://learnsome.tech/learn/security-course/m01l01) (lesson 1.1, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can threat model a change in a few minutes by naming its data flows, its trust boundaries and its entry points, walking STRIDE over each one, and writing down only the answers that change what you build.

In the lesson: Here is question one, written as data instead of a diagram, because a list you can run does not go stale in a drawer. Four flows: where the data comes from, where it goes, what it carries, and which network it travels over. One of them stays inside our own boundary and the rest leave it. The rule underneath is the whole of trust boundary thinking: when data crosses into something with a different level of trust, the crossing needs a decision. Run it. Three crossings carry a card number, and the third one is the interesting one, because nobody designs a logging pipeline and thinks of it as a place card numbers go to live.

## Files

- [`starter/dataflow.py`](starter/dataflow.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-03/starter`
2. Read `dataflow.py` the way the lesson builds it:
   - Lines 1–6: four flows
   - Lines 7–13: the rule underneath
3. Notes from the lesson:
   - Line 4: same VPC is the only flow that stays inside one trust boundary
4. Run it: `python3 dataflow.py`.
5. Check it from the repository root: `./check m01l01-03`.

## Expected output

```text
CROSSES browser to web app carrying card number
  -> must be encrypted, minimised or not sent at all
CROSSES web app to payments API carrying card number
  -> must be encrypted, minimised or not sent at all
internal web app to database carrying order
CROSSES web app to log service carrying card number
  -> must be encrypted, minimised or not sent at all
```

## How to check

`./check m01l01-03` copies `starter/` into a scratch directory and runs `python3 dataflow.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
