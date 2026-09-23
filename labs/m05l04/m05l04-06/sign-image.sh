# Application Security & Threat Modeling for Engineers — lesson m05l04 — Provenance And Signing
# https://learnsome.tech/courses/security-course/watch?lesson=m05l04
# © LearnSome.tech
cosign sign --key cosign.key registry.example/app@sha256:deadbeef
cosign verify --key cosign.pub registry.example/app@sha256:deadbeef
