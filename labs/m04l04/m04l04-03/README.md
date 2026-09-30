# m04l04-03 · Fix: stop the expensive check after the budget

**Lesson:** [Rate Limiting And Resource Consumption](https://learnsome.tech/learn/security-course/m04l04) (lesson 4.4, module 4: API Security) · Pro  
**Check:** Graded

## Goal

You can demonstrate an unlimited guessing path and an unbounded page size, then add limits with clear responses and account aware backoff.

In the lesson: The fixed path counts attempts before it performs the password check. Run the limited loop. Three guesses receive a normal authentication response, and later guesses receive too many requests without reaching the expensive check. The attacker did not recover the password. A production limiter should use shared state, return a retry hint, and avoid making account lockout a denial of service against one victim. Combine an account budget with an address budget and alert on the pattern rather than trusting one counter.

## Files

- [`starter/brute_fixed.py`](starter/brute_fixed.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-03/starter`
2. Read `brute_fixed.py`.
3. Run it: `python3 brute_fixed.py`.
4. Check it from the repository root: `./check m04l04-03`.

## Expected output

```text
status codes: [401, 401, 401, 429, 429]
checks performed: 3
password recovered: False
```

## How to check

`./check m04l04-03` copies `starter/` into a scratch directory and runs `python3 brute_fixed.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
