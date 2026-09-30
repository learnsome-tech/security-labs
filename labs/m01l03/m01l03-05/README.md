# m01l03-05 · A Kubernetes Role is the same idea, in YAML

**Lesson:** [Least Privilege In IAM And RBAC](https://learnsome.tech/learn/security-course/m01l03) (lesson 1.3, module 1: The Security Mindset) · Free  
**Check:** Read along

## Goal

You can read a cloud identity policy and a Kubernetes role for what they actually permit, name the permissions that let a principal grant itself more, and narrow both to the actions and resources a workload really uses.

In the lesson: Kubernetes spells the same idea differently. Rather than write the file by hand, let the tool write it: verbs, resources, and a client side dry run. Run it with the client side dry run and read the object that comes back, without touching a cluster. Rules is a list, and each rule is a cross product of api groups, resources and verbs. A Role is namespaced, so it grants nothing outside its namespace, and a Cluster Role is the same shape without that limit. On its own a Role permits nothing at all: it has to be bound to a subject by a Role Binding, and the two halves are where teams lose track of who has what.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/role.sh`](starter/role.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/role.sh` alongside the lesson.
2. Notes from the lesson:
   - Line 4: dry run client prints the object without touching a cluster
3. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash role.sh
   ```

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/security-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
