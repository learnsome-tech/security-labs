# m03l01-04 · Injection three: the template string

**Lesson:** [Injection In All Its Forms](https://learnsome.tech/learn/security-course/m03l01) (lesson 3.1, module 3: Web Vulnerabilities) · Pro  
**Check:** Graded

## Goal

You can recognise injection as one bug in many interpreters, name the interpreter a piece of code is talking to, and choose the strongest defence available: parameters first, an allowlist where the grammar has no parameters, and escaping only as a last resort.

In the lesson: The third one surprises people, because no database and no shell are involved. The format method in Python is a small language of its own, and it can follow attributes. If the template itself comes from a caller, that caller writes the program. Run the third program. The first two templates do what a greeting should. The third one uses dotted attribute access to walk from the object you passed to the module that defined it, and out comes a deploy key that was never meant to be rendered. The rule that follows is short: templates are code, so templates come from your repository, and caller data is only ever a value you hand to a template.

## Files

- [`starter/concat_format.py`](starter/concat_format.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-04/starter`
2. Read `concat_format.py`.
3. Notes from the lesson:
   - Line 8: a caller controlled template walks attributes it was never shown
4. Run it: `python3 concat_format.py`.
5. Check it from the repository root: `./check m03l01-04`.

## Expected output

```text
Hello bob
Hello bob, session s-9001
Hello deploy-key-4417
```

## How to check

`./check m03l01-04` copies `starter/` into a scratch directory and runs `python3 concat_format.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
