---
applyTo: "infra/**,**/Dockerfile,.github/workflows/**"
---
# Infrastructure and CI rules

## Dockerfiles
- Pin base images to a specific version (e.g. `python:3.13-slim`), never `latest`.
- Set `WORKDIR`, copy dependency files first, then the source (better layer caching).
- Run as a non-root user.
- Never copy `.env` files or secrets into the image; rely on `.dockerignore`.
- Add a `HEALTHCHECK` that hits `/health`.

## GitHub Actions
- Quote version numbers in YAML (`"3.13"`, not `3.13`) - unquoted `3.10` becomes `3.1`.
- The default branch is `main`.
- Pin third-party actions to a major version tag at minimum.
- Give workflows least-privilege `permissions:`.
