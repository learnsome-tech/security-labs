# m01l02-03 · Exploit: authenticated, and reading somebody else's note

**Lesson:** [Authentication Versus Authorisation](https://learnsome.tech/learn/security-course/m01l02) (lesson 1.2, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can say which of the two questions a piece of code is answering, verify a password safely with a memory-hard hash and a constant-time compare, and spot the two classic authorisation mistakes: no ownership check, and trusting a role the client sent.

In the lesson: Now the mistake, as small in code as it is in real systems. Read note takes the session user and the note identifier, looks the note up, and returns its text. The function is perfectly correct about authentication: bob really is bob, his session is real, his password was good. But the argument is never used. Run the exploit. Bob asks for his own note and gets it, which is the case anybody tests. Then bob changes a number in the address bar and asks for note one, and he is handed alice's pay rise proposal. Nothing was broken into. Every control that exists worked. The system never asked the second question at all.

## Files

- [`starter/bola_vuln.py`](starter/bola_vuln.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-03/starter`
2. Read `bola_vuln.py`.
3. Notes from the lesson:
   - Line 6: session_user arrives, is never used, and that is the whole bug
4. Run it: `python3 bola_vuln.py`.
5. Check it from the repository root: `./check m01l02-03`.

## Expected output

```text
bob is authenticated: True
bob asks for his own note: bob lunch order
bob asks for note one: alice pay rise proposal
```

## How to check

`./check m01l02-03` copies `starter/` into a scratch directory and runs `python3 bola_vuln.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
