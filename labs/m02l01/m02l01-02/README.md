# m02l01-02 · Deleting a committed secret does not remove it

**Lesson:** [Why Secrets Leak](https://learnsome.tech/learn/security-course/m02l01) (lesson 2.1, module 2: Secrets And Identity) · Pro  
**Check:** Graded

## Goal

You can name the ordinary routes a secret takes out of a system, prove that deleting a committed file does not remove it, and stop a configuration object or a request logger from printing a live credential.

In the lesson: Here is the route people most often believe they have closed. We create a repository, commit a file holding a token, then delete that file and commit the deletion. The working tree is clean afterwards, and nobody browsing the project can see anything. Run the script. The count of tracked files is zero, and then we ask the repository for that same path one commit back, and the token comes straight out. A delete is another commit, not an erase. Anyone with a clone already has the value, and rewriting history does nothing about the clones that have already left the building.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/leak.sh`](starter/leak.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-02/starter`
2. Read `leak.sh`.
3. Notes from the lesson:
   - Line 7: the removal is recorded as a change; the old content stays reachable
   - Line 10: ask for the same path at the earlier commit and it prints verbatim
4. Run it: `bash leak.sh`.
5. Check it from the repository root: `./check m02l01-02`.

## Expected output

```text
files tracked at head: 0
asking git for the file one commit back:
API_TOKEN=sk-live-4d1f-demo
a delete is another commit, not an erase
```

## How to check

`./check m02l01-02` copies `starter/` into a scratch directory and runs `bash leak.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
