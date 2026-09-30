# m05l05-02 · Count the packages a base image brings

**Lesson:** [Container Security: Minimal Bases And Non Root](https://learnsome.tech/learn/security-course/m05l05) (lesson 5.5, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can reduce an image attack surface with a minimal base and a non root user, inspect those properties in a Dockerfile, and place an image scan where it can block an unsafe release.

In the lesson: Let us make the base image choice measurable. The data lists two representative images and the packages each carries. Run the inventory. The full distribution brings a shell, a package manager, download tools, and an interpreter that the service never needs. The small runtime carries only its library and certificate bundle. This is not a promise that the smaller image is safe. It is a reduction in reachable code and therefore a reduction in what an attacker can do after an exploit. Choose the smallest base that supports the application, then rebuild it regularly so the packages you kept receive security updates.

## Files

- [`starter/basecheck.py`](starter/basecheck.py): the listing from the lesson
- [`starter/images.json`](starter/images.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-02/starter`
2. Read `basecheck.py`.
3. Notes from the lesson:
   - Line 4: the runtime image carries only what execution needs
4. Run it: `python3 basecheck.py`.
5. Check it from the repository root: `./check m05l05-02`.

## Expected output

```text
debian-full packages: 7 shell: True package manager: True
  reachable tools: bash, apt, curl, perl, libc, openssl, ca-certificates
distroless-runtime packages: 2 shell: False package manager: False
  reachable tools: libc, ca-certificates
smallest base: distroless-runtime
```

## How to check

`./check m05l05-02` copies `starter/` into a scratch directory and runs `python3 basecheck.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
