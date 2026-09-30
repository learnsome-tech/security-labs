# m04l01-02 · Signing a certificate with your own authority

**Lesson:** [TLS And The Handshake](https://learnsome.tech/learn/security-course/m04l01) (lesson 4.1, module 4: API Security) · Pro  
**Check:** Graded

## Goal

You can say exactly what a completed handshake proves and what it leaves open, read a certificate verification error and name the reason, and tell the difference between a client that checks a chain and a client that only encrypts.

In the lesson: Before we can watch a handshake we need something to handshake with, so this script builds a miniature world with openssl. First a self signed root: a key pair, and a certificate that declares itself an authority allowed to sign others. Then a request for the orders service, naming it, and the authority signing that request. Notice what the signature covers. The subject line is the name the service claims. The issuer line is whoever vouched for it. The subject alternative name is the list of names a client will accept. Run it, and the verify command walks the chain from the certificate to the root and prints the one word that matters.

## Files

- [`starter/certs.sh`](starter/certs.sh): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`starter/ext.cnf`](starter/ext.cnf)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-02/starter`
2. Read `certs.sh`.
3. Notes from the lesson:
   - Line 4: a root that signs itself: trusted because you chose to trust it
   - Line 7: the authority signs the request, binding the name to that key pair
4. Run it: `bash certs.sh`.
5. Check it from the repository root: `./check m04l01-02`.

## Expected output

```text
what the authority actually signed:
subject=CN = orders.internal
issuer=CN = Course Root CA
valid for the name: orders.internal
does the chain verify:
srv.pem: OK
```

## How to check

`./check m04l01-02` copies `starter/` into a scratch directory and runs `bash certs.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
