# m05l04-03 · Signing and verifying the exact artefact

**Lesson:** [Provenance And Signing](https://learnsome.tech/learn/security-course/m05l04) (lesson 5.4, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what provenance records, verify that a release was signed by the expected builder, and reject an artefact whose bytes or origin no longer match the release policy.

In the lesson: Here is the same idea with a signing key. This short program uses a keyed message authentication code so it stays self contained, while the acceptance rule is the one public key signing systems use: calculate the expected value over the received bytes and compare it with the attached signature. Run the verifier. The expected builder accepts the release and rejects the changed bytes. A version label never enters that calculation, because labels can be copied or rewritten. In production the private key lives in a protected signer and the verifier has only its public key. The important boundary is the same: verify before you deploy, and verify the bytes you are about to run.

## Files

- [`starter/sign.py`](starter/sign.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-03/starter`
2. Read `sign.py`.
3. Notes from the lesson:
   - Line 6: the signature is calculated over the artefact bytes
4. Run it: `python3 sign.py`.
5. Check it from the repository root: `./check m05l04-03`.

## Expected output

```text
signature: 7d0f2ff6b5c3faa2074c
expected signer accepts release: True
expected signer accepts changed bytes: False
signature covers bytes, not a version label
```

## How to check

`./check m05l04-03` copies `starter/` into a scratch directory and runs `python3 sign.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
