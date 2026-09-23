# Application Security & Threat Modeling for Engineers — lesson m01l03 — Least Privilege In IAM And RBAC
# https://learnsome.tech/courses/security-course/watch?lesson=m01l03
# © LearnSome.tech
kubectl create role order-reader \
  --verb=get --verb=list \
  --resource=pods \
  --dry-run=client -o yaml
