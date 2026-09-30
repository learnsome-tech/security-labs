# m01l02-06 · Fix: the server decides what the caller is

**Lesson:** [Authentication Versus Authorisation](https://learnsome.tech/learn/security-course/m01l02) (lesson 1.2, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can say which of the two questions a piece of code is answering, verify a password safely with a memory-hard hash and a constant-time compare, and spot the two classic authorisation mistakes: no ownership check, and trusting a role the client sent.

In the lesson: The fix is to look the role up on the server against the identity that authentication established. Run the fix. Bob claiming to be a viewer and bob claiming to be an admin now produce the same answer, because the field is still in the request and it is ignored. Alice, whose role the server itself records, can do the dangerous thing. In a real system that lookup is a database read or a verified token claim, and verified is the load bearing word: a signed token is only evidence if you check the signature, the audience and the expiry, which is a later lesson. Until then, remember which side of the wire the truth lives on.

## Files

- [`starter/role_fixed.py`](starter/role_fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-06/starter`
2. Read `role_fixed.py`.
3. Notes from the lesson:
   - Line 8: the role field in the request is now simply ignored
4. Run it: `python3 role_fixed.py`.
5. Check it from the repository root: `./check m01l02-06`.

## Expected output

```text
bob may not do that, role is viewer
bob may not do that, role is viewer
alice deleted the customer table
```

## How to check

`./check m01l02-06` copies `starter/` into a scratch directory and runs `python3 role_fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
