# m02l03-04 · An authorised read, a refusal, and the audit trail

**Lesson:** [Moving To A Secret Manager](https://learnsome.tech/learn/security-course/m02l03) (lesson 2.3, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the five properties a secret manager adds over an environment variable, and build or drive one that enforces a per caller policy, records every read, versions values for rotation, and hands out short leases.

In the lesson: Here is a client. The policy says the billing service may read the payment key, and the reporting service may read nothing at all. Run the first client. Billing asks, receives a lease which prints as a version rather than a value, and reveals only the tail. Reporting asks for the same name and is refused, with an error naming who was asking and what they wanted. Then we print the audit trail and both events are in it, the grant and the denial. That list is the thing you cannot build out of environment variables at any price, and it is the first artefact an incident responder will ask you for.

## Files

- [`starter/fetch.py`](starter/fetch.py): the listing from the lesson
- [`starter/lease.py`](starter/lease.py)
- [`starter/vault.py`](starter/vault.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-04/starter`
2. Read `fetch.py`.
3. Run it: `python3 fetch.py`.
4. Check it from the repository root: `./check m02l03-04`.

## Expected output

```text
billing receives: Lease(version 1)
value ends with: demo
refused: reports may not read stripe-key
audit trail:
 - billing stripe-key granted
 - reports stripe-key denied
```

## How to check

`./check m02l03-04` copies `starter/` into a scratch directory and runs `python3 fetch.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
