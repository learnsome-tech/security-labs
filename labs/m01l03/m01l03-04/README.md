# m01l03-04 · The permissions that grant permissions

**Lesson:** [Least Privilege In IAM And RBAC](https://learnsome.tech/learn/security-course/m01l03) (lesson 1.3, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can read a cloud identity policy and a Kubernetes role for what they actually permit, name the permissions that let a principal grant itself more, and narrow both to the actions and resources a workload really uses.

In the lesson: Now the subtle one, and the reason a permission audit cannot be done by counting. This role has no storage permissions at all. What it has is the right to grant rights. Run it. The first answer is a refusal, which is what a shallow review sees. Then the role attaches an administrator policy to itself, and the same question comes back allowed. Anything that can create a role, attach a policy, pass a role to a service, or update a trust relationship is effectively an administrator with extra steps. The same trap exists in Kubernetes, where the escalate and bind verbs, and the right to create pods or read secrets, all lead upwards.

## Files

- [`starter/escalate.py`](starter/escalate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `escalate.py`.
3. Notes from the lesson:
   - Line 3: identity permissions are transitive: they grant the right to grant
4. Run it: `python3 escalate.py`.
5. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
can the build role delete a bucket: False
can it attach a policy to itself: True
it attached AdministratorAccess to itself
can it delete a bucket now: True
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `python3 escalate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
