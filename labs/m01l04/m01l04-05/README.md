# m01l04-05 · A default that fits in one function

**Lesson:** [Secure Defaults](https://learnsome.tech/learn/security-course/m01l04) (lesson 1.4, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can tell a permissive default from a safe one, make the unsafe setting the one that has to be asked for and refused in production, and design interfaces that fail closed so a new route or a new caller is denied rather than served.

In the lesson: This is the pattern at the smallest useful scale, and it is the one to copy. A helper that builds a cookie header, with the protective flags on unless a caller asks otherwise. Secure, so it never travels without encryption. Http only, so a script cannot read it. Same site lax, so it is not attached to requests another site makes, which is most of the defence against the forgery attack later in this course. Run the two calls. The first is what every caller gets for free. The second is somebody opting out, and because they had to name the flags to lose them, that line is searchable, reviewable and explainable.

## Files

- [`starter/cookie.py`](starter/cookie.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-05/starter`
2. Read `cookie.py`.
3. Run it: `python3 cookie.py`.
4. Check it from the repository root: `./check m01l04-05`.

## Expected output

```text
Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Lax; Path=/
Set-Cookie: session=abc123; Secure; SameSite=None; Path=/
```

## How to check

`./check m01l04-05` copies `starter/` into a scratch directory and runs `python3 cookie.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
