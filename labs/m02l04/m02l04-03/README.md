# m02l04-03 · Exchange an attested workload for a short token

**Lesson:** [Workload Identity](https://learnsome.tech/learn/security-course/m02l04) (lesson 2.4, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can explain how workload identity replaces a stored cloud key, verify a short lived exchange for an allowed service, and reject a caller whose identity or audience is wrong.

In the lesson: Here the platform has already attested the workload name. The exchange service checks that name against an audience policy and returns a token with a short lifetime. Run the exchange. Billing is allowed to request a payments token, the lifetime is twenty seconds in this example, and the application never stores a private signing key. The exact identity mechanism differs across clouds and clusters, but the contract is stable: a workload identity, an intended audience, a policy decision, and an expiry. The application presents the token to the service and renews it through the same identity path.

## Files

- [`starter/exchange.py`](starter/exchange.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-03/starter`
2. Read `exchange.py`.
3. Notes from the lesson:
   - Line 6: the policy binds the workload identity to one audience
4. Run it: `python3 exchange.py`.
5. Check it from the repository root: `./check m02l04-03`.

## Expected output

```text
workload: billing-api
audience allowed: True
token lifetime: 20 seconds
application stores private key: False
```

## How to check

`./check m02l04-03` copies `starter/` into a scratch directory and runs `python3 exchange.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
