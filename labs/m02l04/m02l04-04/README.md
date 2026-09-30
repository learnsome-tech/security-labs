# m02l04-04 · Wrong audience and wrong workload are refused

**Lesson:** [Workload Identity](https://learnsome.tech/learn/security-course/m02l04) (lesson 2.4, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain how workload identity replaces a stored cloud key, verify a short lived exchange for an allowed service, and reject a caller whose identity or audience is wrong.

In the lesson: The identity is useful because policy can reject specific mistakes. Run the policy checks. Billing may request payments, but the same workload cannot ask for storage, and the reports workload cannot ask for payments at all. This is narrower than handing every service a cloud key with broad permissions. Keep the audience check in the token verifier and keep the workload to action mapping in reviewed policy. A token that is valid cryptographically but intended for another service must still be rejected.

## Files

- [`starter/reject.py`](starter/reject.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-04/starter`
2. Read `reject.py`.
3. Run it: `python3 reject.py`.
4. Check it from the repository root: `./check m02l04-04`.

## Expected output

```text
billing-api payments ACCEPT
billing-api storage REJECT
reports-api payments REJECT
```

## How to check

`./check m02l04-04` copies `starter/` into a scratch directory and runs `python3 reject.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
