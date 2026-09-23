# Exercises — Least Privilege In IAM And RBAC

Lesson `m01l03` · [Watch](https://learnsome.tech/courses/security-course/watch?lesson=m01l03)

## Exercise 1: Narrow one real policy

1. Take one policy or role from your own infrastructure that contains an asterisk.
2. List the actions the workload really makes, from its logs or from its code.
3. Rewrite the policy naming only those actions and only the resources they touch.
4. Check separately whether anything in it can create, attach or pass identities.

> **Hint**: Cloud providers publish the calls each service makes; access logs are better evidence than memory.


---

© LearnSome.tech · support@iwantto.learnsome.tech
