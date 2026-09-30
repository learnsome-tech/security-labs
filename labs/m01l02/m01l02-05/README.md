# m01l02-05 · Exploit: believing the role the client sent

**Lesson:** [Authentication Versus Authorisation](https://learnsome.tech/learn/security-course/m01l02) (lesson 1.2, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can say which of the two questions a piece of code is answering, verify a password safely with a memory-hard hash and a constant-time compare, and spot the two classic authorisation mistakes: no ownership check, and trusting a role the client sent.

In the lesson: Here is the other classic, and it is worse because it looks like a permission check. The handler reads the role out of the request body and compares it with admin. There is an if statement, there is a rule, somebody could point at it in a review and say authorisation is handled. Run it and watch bob promote himself by editing one field of the data he sends. The lesson generalises past request bodies. Anything the caller controls is not evidence: a hidden form field, a cookie your own code set and never signed, a header, a client side token whose signature nobody verifies. The client is not a source of truth about the client's own rights.

## Files

- [`starter/role_vuln.py`](starter/role_vuln.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-05/starter`
2. Read `role_vuln.py`.
3. Run it: `python3 role_vuln.py`.
4. Check it from the repository root: `./check m01l02-05`.

## Expected output

```text
bob may not do that
bob deleted the customer table
```

## How to check

`./check m01l02-05` copies `starter/` into a scratch directory and runs `python3 role_vuln.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
