# m06l04-05 · Stop a new secret at the commit boundary

**Lesson:** [Secret Scanning](https://learnsome.tech/learn/security-course/m06l04) (lesson 6.4, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can detect common credential shapes and high entropy strings, explain why scanning history matters, and stop a new secret before it reaches the repository.

In the lesson: The earliest useful gate runs before a commit exists. This hook checks the staged text for known credential shapes and rejects the change that contains a token while accepting the environment lookup. Run the commit check. A local hook is helpful feedback, but it is not the control you trust alone because hooks can be skipped. Run the same detector in the central pipeline and on the full history, and make the response a rotation workflow rather than a noisy red build with no owner.

## Files

- [`starter/hook.py`](starter/hook.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-05/starter`
2. Read `hook.py`.
3. Notes from the lesson:
   - Line 3: the hook examines staged text before a commit exists
4. Run it: `python3 hook.py`.
5. Check it from the repository root: `./check m06l04-05`.

## Expected output

```text
new token rejected
environment lookup accepted
```

## How to check

`./check m06l04-05` copies `starter/` into a scratch directory and runs `python3 hook.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
