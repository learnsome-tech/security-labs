# m01l02-02 · Authentication, done the boring correct way

**Lesson:** [Authentication Versus Authorisation](https://learnsome.tech/learn/security-course/m01l02) (lesson 1.2, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can say which of the two questions a piece of code is answering, verify a password safely with a memory-hard hash and a constant-time compare, and spot the two classic authorisation mistakes: no ownership check, and trusting a role the client sent.

In the lesson: This is the whole of password authentication, and it is deliberately dull. Store takes a password, generates a fresh random salt, and derives a key with scrypt, which is deliberately slow and memory hungry so that guessing at scale costs real money. Verify derives a key from the candidate password with the same salt and the same parameters, and then does the comparison with compare digest rather than with the equality operator, because equality stops at the first differing byte and leaks how much of the guess was right. Run it, and you get exactly one bit of information back: this caller is who they claim to be. Nothing here says a word about what they may do.

## Files

- [`starter/authn.py`](starter/authn.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-02/starter`
2. Read `authn.py` the way the lesson builds it:
   - Lines 1–6: a fresh random salt
   - Lines 7–11: the comparison
   - Lines 12–17: run it
3. Notes from the lesson:
   - Line 5: scrypt is memory hard: a graphics card cannot parallelise it cheaply
   - Line 11: compare_digest takes the same time whether or not the bytes match
4. Run it: `python3 authn.py`.
5. Check it from the repository root: `./check m01l02-02`.

## Expected output

```text
stored key length in bytes: 64
right password: True
wrong password: False
authentication answers who you are, and nothing else
```

## How to check

`./check m01l02-02` copies `starter/` into a scratch directory and runs `python3 authn.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
