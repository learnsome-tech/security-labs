# m02l04-05 · Expiry turns a stolen token into a short incident

**Lesson:** [Workload Identity](https://learnsome.tech/learn/security-course/m02l04) (lesson 2.4, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain how workload identity replaces a stored cloud key, verify a short lived exchange for an allowed service, and reject a caller whose identity or audience is wrong.

In the lesson: The final property is time. A verifier checks the expiry on every use, so a token copied from a process does not remain useful forever. Run the expiry check. The fresh token has twenty seconds left, the old token is rejected, and when time advances even the fresh token is no longer accepted. Short lifetimes do not replace least privilege or monitoring, but they reduce the window in which a leaked bearer token can be replayed. Make clock handling and renewal observable, because an outage caused by every token expiring at once is a reliability bug as well as a security bug.

## Files

- [`starter/expiry.py`](starter/expiry.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-05/starter`
2. Read `expiry.py`.
3. Run it: `python3 expiry.py`.
4. Check it from the repository root: `./check m02l04-05`.

## Expected output

```text
fresh accepted remaining: 20 seconds
old REJECTED remaining: 0 seconds
fresh token after time advances: False
```

## How to check

`./check m02l04-05` copies `starter/` into a scratch directory and runs `python3 expiry.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
