# m01l03-02 · Exploit: what a wildcard policy actually grants

**Lesson:** [Least Privilege In IAM And RBAC](https://learnsome.tech/learn/security-course/m01l03) (lesson 1.3, module 1: The Security Mindset) · Free  
**Check:** Graded

## Goal

You can read a cloud identity policy and a Kubernetes role for what they actually permit, name the permissions that let a principal grant itself more, and narrow both to the actions and resources a workload really uses.

In the lesson: A policy is a matching rule, so we can evaluate one honestly in a few lines. Action patterns and resource patterns, matched with shell style wildcards, which is close enough to how the real evaluator treats an asterisk. On screen is the policy somebody writes when a reporting job needs to read one file and the deployment is due. Run the three questions. Reading the report is allowed, which was the intention. Deleting the production backup bucket is allowed. Rewriting the bucket policy, so that the whole internet can read it, is allowed. All three come from the same line, and nobody ever intended the last two.

## Files

- [`starter/iam_wide.py`](starter/iam_wide.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-02/starter`
2. Read `iam_wide.py`.
3. Notes from the lesson:
   - Line 3: the policy a team writes when the job only needs to read one report
4. Run it: `python3 iam_wide.py`.
5. Check it from the repository root: `./check m01l03-02`.

## Expected output

```text
ALLOW s3:GetObject arn:aws:s3:::reports/june.csv
ALLOW s3:DeleteBucket arn:aws:s3:::production-backups
ALLOW s3:PutBucketPolicy arn:aws:s3:::production-backups
```

## How to check

`./check m01l03-02` copies `starter/` into a scratch directory and runs `python3 iam_wide.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
