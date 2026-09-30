# m06l04-02 · Recognise named credential shapes

**Lesson:** [Secret Scanning](https://learnsome.tech/learn/security-course/m06l04) (lesson 6.4, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can detect common credential shapes and high entropy strings, explain why scanning history matters, and stop a new secret before it reaches the repository.

In the lesson: The first pass looks for credential families with a documented shape. Run the detector. It reports the line, a high severity label, the rule name, and a masked value that lets the owner recognise which entry needs rotation. The full token never appears in the scanner output. This is deliberately simple, because a fast local hook and a fast review check catch the mistake before it spreads. The service still needs a real secret manager, but scanning is the cheap last chance before source becomes history.

## Files

- [`starter/detect.py`](starter/detect.py): the listing from the lesson
- [`starter/settings.py`](starter/settings.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-02/starter`
2. Read `detect.py`.
3. Run it: `python3 detect.py`.
4. Check it from the repository root: `./check m06l04-02`.

## Expected output

```text
line 1 HIGH cloud key AKIA********MQ4
line 2 HIGH source token ghp_********2pU
```

## How to check

`./check m06l04-02` copies `starter/` into a scratch directory and runs `python3 detect.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
