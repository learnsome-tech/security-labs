# m06l04-03 · Entropy finds secrets without a known prefix

**Lesson:** [Secret Scanning](https://learnsome.tech/learn/security-course/m06l04) (lesson 6.4, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can detect common credential shapes and high entropy strings, explain why scanning history matters, and stop a new secret before it reaches the repository.

In the lesson: A private key or database password may not have a prefix that a rule recognises. Entropy is a useful second pass: values with many evenly distributed characters are more likely to be generated secrets than ordinary prose. Run the entropy check. The token and the digest are flagged, and so is the comment, because a sentence with many different letters also clears this threshold. Entropy is not proof. A release digest can be high entropy and harmless, while a short password can be dangerous and look ordinary. Use the result to ask for context, then rotate anything that was exposed rather than trying to tune the threshold until the warning disappears.

## Files

- [`starter/entropy.py`](starter/entropy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-03/starter`
2. Read `entropy.py`.
3. Run it: `python3 entropy.py`.
4. Check it from the repository root: `./check m06l04-03`.

## Expected output

```text
token flagged
comment flagged
digest flagged
```

## How to check

`./check m06l04-03` copies `starter/` into a scratch directory and runs `python3 entropy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
