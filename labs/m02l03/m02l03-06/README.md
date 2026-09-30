# m02l03-06 · Leases: cache, refetch, and refuse an expired one

**Lesson:** [Moving To A Secret Manager](https://learnsome.tech/learn/security-course/m02l03) (lesson 2.3, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the five properties a secret manager adds over an environment variable, and build or drive one that enforces a per caller policy, records every read, versions values for rotation, and hands out short leases.

In the lesson: The last property is the lease. A sensible client caches, because fetching on every request is slow and noisy, but it caches the lease and it checks validity before reusing it. Run the lease demo. The first call fetches. The second call reuses the cached lease, and the fetch count does not move. Then we wait past the lifetime and the next call refetches by itself, which is how a short lease turns into rotation that nobody has to schedule. Finally we take a lease that has already ended and try to use it, and revealing refuses. Build clients this way and a stolen copy is worth minutes rather than years.

## Files

- [`starter/expiry.py`](starter/expiry.py): the listing from the lesson
- [`starter/lease.py`](starter/lease.py)
- [`starter/vault.py`](starter/vault.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-06/starter`
2. Read `expiry.py`.
3. Notes from the lesson:
   - Line 12: check validity before reuse; a cache without a clock is a copy
4. Run it: `python3 expiry.py`.
5. Check it from the repository root: `./check m02l03-06`.

## Expected output

```text
first call: demo fetches: 1
second call: demo fetches: 1
after the lease ends: demo fetches: 2
refused: lease on version 1 ended
```

## How to check

`./check m02l03-06` copies `starter/` into a scratch directory and runs `python3 expiry.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
