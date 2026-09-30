# m06l01-05 · The fix changes the construction, not the warning

**Lesson:** [Static Application Security Testing](https://learnsome.tech/learn/security-course/m06l01) (lesson 6.1, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can explain what static analysis can and cannot see, run a small syntax aware scanner against vulnerable code, and tune a pipeline gate so useful findings stop the build without turning every warning into an emergency.

In the lesson: The fix is visible in the construction, not in a comment beside it. The corrected function checks a small allowlist and passes a list of arguments to a process API with shell mode disabled. Run the fixed check. The rule sees no shell parsing and sees a list rather than one string assembled from request data. Static analysis can now verify the property it cares about. The runtime still needs tests, because a hostname allowlist can be incomplete or the command can fail for another reason. SAST and tests answer different questions and belong in the same change.

## Files

- [`starter/fixed.py`](starter/fixed.py): the listing from the lesson
- [`starter/fixed_app.py`](starter/fixed_app.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-05/starter`
2. Read `fixed.py`.
3. Notes from the lesson:
   - Line 12: a list of arguments and shell false remove shell parsing
4. Run it: `python3 fixed.py`.
5. Check it from the repository root: `./check m06l01-05`.

## Expected output

```text
report_fixed shell mode: False list arguments: True
```

## How to check

`./check m06l01-05` copies `starter/` into a scratch directory and runs `python3 fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
