# m01l04-03 · Fix: safe by default, and refused where it matters

**Lesson:** [Secure Defaults](https://learnsome.tech/learn/security-course/m01l04) (lesson 1.4, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can tell a permissive default from a safe one, make the unsafe setting the one that has to be asked for and refused in production, and design interfaces that fail closed so a new route or a new caller is denied rather than served.

In the lesson: Now invert it. Every default is the cautious answer, and the empty list of allowed origins means no cross origin caller is trusted until somebody names one. Then a second table naming the settings that are acceptable while you are developing and unacceptable in production, and a service that refuses to start rather than run in that state. The environment decides. Run both calls. On a laptop, turning off certificate checking is allowed and the service comes up. In production the same override kills the process with a message that names the setting. A service that will not start is an obvious problem at deploy time. A service quietly running with certificate checking off is a problem you find out about much later.

## Files

- [`starter/secure_defaults.py`](starter/secure_defaults.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-03/starter`
2. Read `secure_defaults.py` the way the lesson builds it:
   - Lines 1–7: a second table naming the settings
   - Lines 8–16: refuses to start
   - Lines 17–19: run both calls
3. Notes from the lesson:
   - Line 13: the environment decides: unsafe on a laptop, fatal in production
4. Run it: `python3 secure_defaults.py`.
5. Check it from the repository root: `./check m01l04-03`.

## Expected output

```text
laptop, tls check off: False
Traceback (most recent call last):
  File "secure_defaults.py", line 19, in <module>
    print(start("production", {"verify_tls": False}))
  File "secure_defaults.py", line 14, in start
    raise ValueError("refusing to start: " + key + " is unsafe here")
ValueError: refusing to start: verify_tls is unsafe here
```

## How to check

`./check m01l04-03` copies `starter/` into a scratch directory and runs `python3 secure_defaults.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
