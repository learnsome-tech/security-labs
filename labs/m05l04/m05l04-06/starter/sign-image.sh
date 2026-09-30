cosign sign --key cosign.key registry.example/app@sha256:deadbeef
cosign verify --key cosign.pub registry.example/app@sha256:deadbeef
