# m01l04-02 · Exploit: nobody typed anything wrong

**Lesson:** [Secure Defaults](https://learnsome.tech/learn/security-course/m01l04) (lesson 1.4, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can tell a permissive default from a safe one, make the unsafe setting the one that has to be asked for and refused in production, and design interfaces that fail closed so a new route or a new caller is denied rather than served.

In the lesson: Here is a service with a familiar set of defaults. Debug pages on, so a stack trace with source and environment goes to whoever asks for a broken URL. Certificate checking off, because somebody hit a self signed certificate once. Every origin allowed, because the front end team was blocked. Cookies without the secure flag. An administrator password that is a word in the code. Run it with no overrides at all, an empty override, in production. Every one of those settings is now live, and nobody made a decision, nobody reviewed a diff, nobody was careless. The design did all of it, because the design's idea of nothing was unsafe.

## Files

- [`starter/insecure_defaults.py`](starter/insecure_defaults.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-02/starter`
2. Read `insecure_defaults.py`.
3. Notes from the lesson:
   - Line 17: the override dictionary is empty: this is what shipping in a hurry looks like
4. Run it: `python3 insecure_defaults.py`.
5. Check it from the repository root: `./check m01l04-02`.

## Expected output

```text
starting in production
  debug = True
  verify_tls = False
  allowed_origins = *
  cookie_secure = False
  admin_password = changeme
nobody typed anything wrong, and every setting is unsafe
```

## How to check

`./check m01l04-02` copies `starter/` into a scratch directory and runs `python3 insecure_defaults.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
