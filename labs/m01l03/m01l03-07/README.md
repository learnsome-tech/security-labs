# m01l03-07 · Fix: the verbs and resources the workload uses

**Lesson:** [Least Privilege In IAM And RBAC](https://learnsome.tech/learn/security-course/m01l03) (lesson 1.3, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can read a cloud identity policy and a Kubernetes role for what they actually permit, name the permissions that let a principal grant itself more, and narrow both to the actions and resources a workload really uses.

In the lesson: Narrow it to what the workload actually calls, which in this case is two verbs on one resource. Run the same three requests. The pod still does its job, and the two routes to somebody else's credentials are closed. Three rules of thumb for real clusters. Never bind cluster admin to a workload, only to people who need it, and preferably briefly. Prefer a Role in one namespace over a Cluster Role, because the namespace is a real boundary. And treat secrets, pod creation, and the escalate and bind verbs as administrative, whatever the resource name suggests, because each of them is a path to everything else.

## Files

- [`starter/rbac_narrow.py`](starter/rbac_narrow.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-07/starter`
2. Read `rbac_narrow.py`.
3. Run it: `python3 rbac_narrow.py`.
4. Check it from the repository root: `./check m01l03-07`.

## Expected output

```text
ALLOW get pods
deny get secrets
deny delete nodes
the same pod can no longer read one secret
```

## How to check

`./check m01l03-07` copies `starter/` into a scratch directory and runs `python3 rbac_narrow.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
