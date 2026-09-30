# m04l04-02 · Exploit: unlimited guesses reveal the password

**Lesson:** [Rate Limiting And Resource Consumption](https://learnsome.tech/learn/security-course/m04l04) (lesson 4.4, module 4: API Security) · Pro  
**Check:** Graded

## Goal

You can demonstrate an unlimited guessing path and an unbounded page size, then add limits with clear responses and account aware backoff.

In the lesson: The weak login path answers every guess until one is correct. Run the guessing loop. Seven requests are answered and the password is recovered from a small list, with no delay or refusal. A real attacker would distribute guesses across addresses and accounts, so one counter at one process is not enough. The service needs a policy that limits attempts by the account, the source, or both, and it must return a retry response without continuing to perform the expensive password check.

## Files

- [`starter/brute.py`](starter/brute.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `brute.py`.
3. Run it: `python3 brute.py`.
4. Check it from the repository root: `./check m04l04-02`.

## Expected output

```text
requests answered: 7
password recovered: hunter2
limit enforced: False
```

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `python3 brute.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
