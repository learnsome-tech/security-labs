# m05l01-04 · Name confusion, measured rather than guessed

**Lesson:** [Dependency Risk And Typosquatting](https://learnsome.tech/learn/security-course/m05l01) (lesson 5.1, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can describe the trust surface a single install command opens, detect a name that is one edit away from a package you meant, and name the four defences that shrink the surface without stopping delivery.

In the lesson: Now the cheapest attack of the four: publish a package whose name is one keystroke from a popular one, and wait. Here is a detector rather than an anecdote. For every requested name we compute the edit script against a list of well known names, keep the candidates that differ by exactly one insertion, deletion or substitution, and for substitutions we ask whether the two characters sit next to each other on a keyboard. Run it over the requirements. One entry is genuinely fine. Four are a single edit from something real: an inserted vowel, a digit beside the right digit, a letter missing from the middle of a long name, and a swapped vowel. The keyboard column separates a plausible slip from a deliberate imitation.

## Files

- [`starter/typosquat.py`](starter/typosquat.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-04/starter`
2. Read `typosquat.py`.
3. Run it: `python3 typosquat.py`.
4. Check it from the repository root: `./check m05l01-04`.

## Expected output

```text
ok       requests
SUSPECT  colourama - one edit from colorama - key slip: False
SUSPECT  urllib4 - one edit from urllib3 - key slip: True
SUSPECT  python-datutil - one edit from python-dateutil - key slip: False
SUSPECT  reqiests - one edit from requests - key slip: True
```

## How to check

`./check m05l01-04` copies `starter/` into a scratch directory and runs `python3 typosquat.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
