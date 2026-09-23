# Exercises — Container Security: Minimal Bases And Non Root

Lesson `m05l05` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m05l05)

## Exercise 1: Harden one image you own

1. List every package and executable in the current runtime image.
2. Change the Dockerfile to use a smaller base and an explicit user.
3. Run the image as non root with a read only root filesystem.
4. Add a scan gate that blocks high and critical findings.

> **Hint**: If a debugging tool is needed in production, first ask whether it belongs in a separate diagnostic image.


---

© LearnSome.tech · support@iwantto.learnsome.tech
