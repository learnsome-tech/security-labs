# m05l04-04 · Provenance makes the build claim testable

**Lesson:** [Provenance And Signing](https://learnsome.tech/learn/security-course/m05l04) (lesson 5.4, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what provenance records, verify that a release was signed by the expected builder, and reject an artefact whose bytes or origin no longer match the release policy.

In the lesson: A signature tells you which key approved bytes, but a key alone is not a build story. This statement records a source repository, a revision, a builder identity, and the digest of the source the builder checked out. Run the policy check. The deployment rule can now require the trusted builder and the reviewed revision before it accepts the release. In a real system the statement is signed and attached to the image or package, so nobody can edit these fields without breaking verification. Provenance is useful because it turns a conversation such as somebody built this from somewhere into fields a policy engine can inspect.

## Files

- [`starter/provenance.py`](starter/provenance.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-04/starter`
2. Read `provenance.py`.
3. Notes from the lesson:
   - Line 5: the builder identity is part of the statement
4. Run it: `python3 provenance.py`.
5. Check it from the repository root: `./check m05l04-04`.

## Expected output

```text
source: repo@example/checkout revision 777
builder: ci trusted pool
source digest recorded: be9c4f7002b72114
policy accepts builder: True
policy accepts revision: True
```

## How to check

`./check m05l04-04` copies `starter/` into a scratch directory and runs `python3 provenance.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
