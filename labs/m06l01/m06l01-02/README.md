# m06l01-02 · A text search confuses comments with code

**Lesson:** [Static Application Security Testing](https://learnsome.tech/learn/security-course/m06l01) (lesson 6.1, module 6: Scanning And The Pipeline) · Pro  
**Check:** Graded

## Goal

You can explain what static analysis can and cannot see, run a small syntax aware scanner against vulnerable code, and tune a pipeline gate so useful findings stop the build without turning every warning into an emergency.

In the lesson: Here is the smallest reason to prefer a syntax aware rule. The sample has a comment mentioning an unsafe call and a real call split across two lines. Run both passes. The text search reports the comment and misses the shape of the multiline call. The tree pass ignores the comment and reports the call at its actual line. This is not advanced artificial intelligence. It is the difference between searching characters and asking the parser what the program means. Every rule you add should start from that distinction, because noisy matches train engineers to close findings without reading them.

## Files

- [`starter/grep_vs_ast.py`](starter/grep_vs_ast.py): the listing from the lesson
- [`starter/sample.py`](starter/sample.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-02/starter`
2. Read `grep_vs_ast.py`.
3. Notes from the lesson:
   - Line 9: the syntax tree finds the call even when it spans lines
4. Run it: `python3 grep_vs_ast.py`.
5. Check it from the repository root: `./check m06l01-02`.

## Expected output

```text
regex hit on line 1
tree pass
real call to eval on line 6
```

## How to check

`./check m06l01-02` copies `starter/` into a scratch directory and runs `python3 grep_vs_ast.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
