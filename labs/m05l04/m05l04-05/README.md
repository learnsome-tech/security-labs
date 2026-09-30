# m05l04-05 · Reject the wrong builder before deployment

**Lesson:** [Provenance And Signing](https://learnsome.tech/learn/security-course/m05l04) (lesson 5.4, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what provenance records, verify that a release was signed by the expected builder, and reject an artefact whose bytes or origin no longer match the release policy.

In the lesson: The policy should be boring enough to run every time. This example accepts only a signed statement from the named continuous integration builder. Run the deployment rule. The first release passes. The second has a signature but came from a laptop, so it is rejected. The third came from the right builder but has no valid signature, so it is rejected as well. This is the useful separation between authentication and provenance: the key proves who signed, while the statement says what process produced the bytes. Keep the accepted builder identities and required checks in policy code, reviewed like any other production change.

## Files

- [`starter/policy.py`](starter/policy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-05/starter`
2. Read `policy.py`.
3. Notes from the lesson:
   - Line 6: both signature and builder identity must pass
4. Run it: `python3 policy.py`.
5. Check it from the repository root: `./check m05l04-05`.

## Expected output

```text
release one ACCEPT - ci trusted pool
release two REJECT - laptop shell
release three REJECT - ci trusted pool
```

## How to check

`./check m05l04-05` copies `starter/` into a scratch directory and runs `python3 policy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
