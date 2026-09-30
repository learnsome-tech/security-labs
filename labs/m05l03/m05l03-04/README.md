# m05l03-04 · Two different documents: source and image

**Lesson:** [Software Bill Of Materials](https://learnsome.tech/learn/security-course/m05l03) (lesson 5.3, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can generate a machine readable bill of materials for a build, answer whether a new advisory affects you by querying it with a correct version comparison, and say what such a document does not cover.

In the lesson: A document generated from your source describes what your language package manager resolved. What you deploy is an image, and an image also contains an operating system. Run the comparison. The base image contributes its own packages, with identifiers from a different ecosystem, and none of them are in the lockfile, so a tool that only reads your lockfile is blind to all of them. That matters because the shell, the crypto library and the compression library in the base layer are exactly the components that attract remotely exploitable advisories. So generate both: one for the source you build, and one for the image you ship, and treat the second as the complete answer.

## Files

- [`starter/base-image.json`](starter/base-image.json)
- [`starter/imagebom.py`](starter/imagebom.py): the listing from the lesson
- [`starter/sbom.json`](starter/sbom.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-04/starter`
2. Read `imagebom.py`.
3. Notes from the lesson:
   - Line 10: none of the operating system packages appear in the lockfile
4. Run it: `python3 imagebom.py`.
5. Check it from the repository root: `./check m05l03-04`.

## Expected output

```text
the source build knows about: 4 components
the base image alpine:3.22 adds: 4
  pkg:apk/alpine/busybox@1.37.0-r18 in the lockfile: False
  pkg:apk/alpine/musl@1.2.5-r10 in the lockfile: False
  pkg:apk/alpine/openssl@3.5.1-r0 in the lockfile: False
  pkg:apk/alpine/zlib@1.3.1-r2 in the lockfile: False
what ships is the union: 8
```

## How to check

`./check m05l03-04` copies `starter/` into a scratch directory and runs `python3 imagebom.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
