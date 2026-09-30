# m01l03-06 · Exploit: the asterisk in a Kubernetes rule

**Lesson:** [Least Privilege In IAM And RBAC](https://learnsome.tech/learn/security-course/m01l03) (lesson 1.3, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can read a cloud identity policy and a Kubernetes role for what they actually permit, name the permissions that let a principal grant itself more, and narrow both to the actions and resources a workload really uses.

In the lesson: Here is the rule teams write when a container needs to list pods and the incident is ongoing. Every resource, every verb, in the core api group. Run the three requests. Listing pods works, which was the need. Reading secrets works, and in a default cluster that includes service account tokens, so a compromised container in this namespace can collect other workloads' credentials and keep moving. Deleting nodes works too. The Kubernetes documentation is blunt about this: read access to secrets in a namespace is equivalent to the rights of everything in that namespace, and the wildcard hands it over without anybody typing the word secret.

## Files

- [`starter/rbac_wide.py`](starter/rbac_wide.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-06/starter`
2. Read `rbac_wide.py`.
3. Run it: `python3 rbac_wide.py`.
4. Check it from the repository root: `./check m01l03-06`.

## Expected output

```text
ALLOW get pods
ALLOW get secrets
ALLOW delete nodes
a pod with this role can read every service account token
```

## How to check

`./check m01l03-06` copies `starter/` into a scratch directory and runs `python3 rbac_wide.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
