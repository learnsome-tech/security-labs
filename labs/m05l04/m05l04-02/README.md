# m05l04-02 · A digest catches one changed byte

**Lesson:** [Provenance And Signing](https://learnsome.tech/learn/security-course/m05l04) (lesson 5.4, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can explain what provenance records, verify that a release was signed by the expected builder, and reject an artefact whose bytes or origin no longer match the release policy.

In the lesson: Start with the smallest useful claim. We hash the bytes that the build produced, keep the hexadecimal digest in the release record, and compare a copy later. Run the comparison. The untouched copy matches and the copy with one word changed does not. That is why deployment systems address images and packages by digest when they need an immutable reference. Notice the limit in the final line. Anybody can calculate a digest for malicious bytes, so a digest gives you identity but gives you no origin. To answer who approved the bytes, we need a signature.

## Files

- [`starter/digest.py`](starter/digest.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-02/starter`
2. Read `digest.py`.
3. Notes from the lesson:
   - Line 4: record the digest beside the release metadata
4. Run it: `python3 digest.py`.
5. Check it from the repository root: `./check m05l04-02`.

## Expected output

```text
recorded digest: ff6e666b218b349e
release copy matches: True
tampered copy matches: False
the digest identifies bytes, not the author
```

## How to check

`./check m05l04-02` copies `starter/` into a scratch directory and runs `python3 digest.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
