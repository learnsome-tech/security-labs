# Exercises — TLS And The Handshake

Lesson `m04l01` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m04l01)

## Exercise 1: Prove your own clients really check

1. List every place your code builds an HTTP client, a socket wrapper or a driver.
2. Search for verify equals false, insecure skip verify and certificate none.
3. Point one client at a service whose certificate names something else; confirm it refuses.
4. Add an alarm on days remaining for every certificate you serve or depend on.

> **Hint**: Test frameworks, container base images and internal service meshes are where verification quietly goes missing.


---

© LearnSome.tech · support@iwantto.learnsome.tech
