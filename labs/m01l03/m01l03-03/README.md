# m01l03-03 · Fix: name the action and name the resource

**Lesson:** [Least Privilege In IAM And RBAC](https://learnsome.tech/learn/security-course/m01l03) (lesson 1.3, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can read a cloud identity policy and a Kubernetes role for what they actually permit, name the permissions that let a principal grant itself more, and narrow both to the actions and resources a workload really uses.

In the lesson: The fix is not clever, it is only specific. One action, because the job reads objects and nothing else. One resource prefix, because the job reads reports and has no business anywhere else. Run the same three questions against it and the intended one still works while both of the accidents are denied. Two habits make this sustainable. Start from nothing and add permissions when something fails, rather than starting wide and promising to narrow it later, which never happens. And read the deny lines in the output as the point of the exercise, because they are the blast radius you no longer have.

## Files

- [`starter/iam_scoped.py`](starter/iam_scoped.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-03/starter`
2. Read `iam_scoped.py`.
3. Run it: `python3 iam_scoped.py`.
4. Check it from the repository root: `./check m01l03-03`.

## Expected output

```text
ALLOW s3:GetObject arn:aws:s3:::reports/june.csv
deny s3:DeleteBucket arn:aws:s3:::production-backups
deny s3:PutBucketPolicy arn:aws:s3:::production-backups
```

## How to check

`./check m01l03-03` copies `starter/` into a scratch directory and runs `python3 iam_scoped.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
