# m03l05-02 · Exploit: input changes the operation

**Lesson:** [Cross-Site Request Forgery](https://learnsome.tech/learn/security-course/m03l05) (lesson 3.5, module 3: Web Vulnerabilities) · Pro  
**Check:** Graded

## Goal

You can demonstrate a cookie only state change and fix it with a session bound request token.

In the lesson: Cross-Site Request Forgery lesson. Run the vulnerable program with the hostile value. The output shows the effect on the target, which is the evidence a security review needs. The important detail is where the input crossed from data into an interpreter, because that is the boundary the fix must restore.

## Files

- [`starter/exploit.py`](starter/exploit.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-02/starter`
2. Read `exploit.py`.
3. Run it: `python3 exploit.py`.
4. Check it from the repository root: `./check m03l05-02`.

## Expected output

```text
state change accepted: True
```

## How to check

`./check m03l05-02` copies `starter/` into a scratch directory and runs `python3 exploit.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
