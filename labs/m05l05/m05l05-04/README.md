# m05l05-04 · The process really runs with a reduced identity

**Lesson:** [Container Security: Minimal Bases And Non Root](https://learnsome.tech/learn/security-course/m05l05) (lesson 5.5, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can reduce an image attack surface with a minimal base and a non root user, inspect those properties in a Dockerfile, and place an image scan where it can block an unsafe release.

In the lesson: The point of a non root user is the authority the process does not have. This small program models the two identities a deployment policy might see and prints the consequence of each. Run the identity check. The root process can bind a privileged port and write wherever the container permits. The application identity cannot do either by default, so a compromised request handler has fewer useful next steps. This does not remove the need for a kernel boundary, read only filesystems, or careful capabilities. It makes the common failure mode smaller, and it gives the deployment system a property it can reject.

## Files

- [`starter/identity.py`](starter/identity.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-04/starter`
2. Read `identity.py`.
3. Run it: `python3 identity.py`.
4. Check it from the repository root: `./check m05l05-04`.

## Expected output

```text
root uid 0 can bind privileged port: True
  write policy: all writable paths
app uid 10001 can bind privileged port: False
  write policy: application paths only
deployment accepts uid zero: False
```

## How to check

`./check m05l05-04` copies `starter/` into a scratch directory and runs `python3 identity.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
