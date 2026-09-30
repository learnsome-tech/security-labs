# m05l05-05 · Drop capabilities and make the filesystem read only

**Lesson:** [Container Security: Minimal Bases And Non Root](https://learnsome.tech/learn/security-course/m05l05) (lesson 5.5, module 5: The Supply Chain) · Pro  
**Check:** Graded

## Goal

You can reduce an image attack surface with a minimal base and a non root user, inspect those properties in a Dockerfile, and place an image scan where it can block an unsafe release.

In the lesson: User identity is one part of the runtime contract. This policy also requires a read only root filesystem and no extra Linux capabilities. Run the runtime policy. The default configuration is rejected on all three counts. The hardened configuration passes because it runs as the service user, cannot rewrite the image layer, and has no optional capabilities. Give the process a separate writable volume only where the application needs one, and keep that path narrow. These settings are defence in depth: an application vulnerability still matters, but the post exploit path is less powerful and easier to observe.

## Files

- [`starter/runtime_policy.py`](starter/runtime_policy.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l05/m05l05-05/starter`
2. Read `runtime_policy.py`.
3. Notes from the lesson:
   - Line 8: the policy combines identity, storage and capabilities
4. Run it: `python3 runtime_policy.py`.
5. Check it from the repository root: `./check m05l05-05`.

## Expected output

```text
default REJECT uid 0 read only False caps all
hardened ACCEPT uid 10001 read only True caps none
```

## How to check

`./check m05l05-05` copies `starter/` into a scratch directory and runs `python3 runtime_policy.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
