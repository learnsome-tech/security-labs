# m02l03-05 · Rotation: version two becomes current

**Lesson:** [Moving To A Secret Manager](https://learnsome.tech/learn/security-course/m02l03) (lesson 2.3, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the five properties a secret manager adds over an environment variable, and build or drive one that enforces a per caller policy, records every read, versions values for rotation, and hands out short leases.

In the lesson: Rotation is where versioning pays for itself. We store a first value, and a small stand in for the upstream service accepts whatever the current version happens to be, which is how a real provider behaves once you have rolled a key. Run the rotation. Version one is accepted. We store a new value and the manager tells us it is version two. The next fetch returns version two, the upstream accepts it, and the copy of version one we are still holding is now rejected. Nothing was redeployed and no manifest changed. That is the difference between a credential you can rotate on a Tuesday afternoon and one that needs a change window.

## Files

- [`starter/lease.py`](starter/lease.py)
- [`starter/rotate.py`](starter/rotate.py): the listing from the lesson
- [`starter/vault.py`](starter/vault.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-05/starter`
2. Read `rotate.py`.
3. Notes from the lesson:
   - Line 8: the upstream accepts only the current version, as a real provider does
4. Run it: `python3 rotate.py`.
5. Check it from the repository root: `./check m02l03-05`.

## Expected output

```text
version one at the upstream: accepted
rotation stores version: 2
current version is now: 2
version two at the upstream: accepted
version one at the upstream: rejected
```

## How to check

`./check m02l03-05` copies `starter/` into a scratch directory and runs `python3 rotate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
