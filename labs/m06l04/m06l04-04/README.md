# m06l04-04 · A working tree can be clean while history is not

**Lesson:** [Secret Scanning](https://learnsome.tech/learn/security-course/m06l04) (lesson 6.4, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can detect common credential shapes and high entropy strings, explain why scanning history matters, and stop a new secret before it reaches the repository.

In the lesson: A working tree scan answers only what is checked out now. This small history model shows why that is not enough. Run the history check. The current content is clean, but the earlier commit still contains the token shape. A real history scanner walks every commit and every branch you ask it to inspect, then the response is rotation and removal from any downstream system that copied the value. Do not rely on deleting a line, force pushing, or renaming the variable. Assume the old value is public once it entered a repository.

## Files

- [`starter/history.py`](starter/history.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-04/starter`
2. Read `history.py`.
3. Run it: `python3 history.py`.
4. Check it from the repository root: `./check m06l04-04`.

## Expected output

```text
working tree scan: clean
add settings contains token: True
move to environment contains token: False
```

## How to check

`./check m06l04-04` copies `starter/` into a scratch directory and runs `python3 history.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
