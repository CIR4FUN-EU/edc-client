# Release guide

This repository publishes the `edc-client` package to PyPI from version tags matching
`v<major>.<minor>.<patch>`. Publishing runs on GitHub Actions
(`.github/workflows/release.yml`) using PyPI **Trusted Publishing (OIDC)** — no API
token is stored anywhere.

## One-time setup (do this once, in the browser)

Trusted Publishing and the GitHub environments must be configured before the first tag.

1. **PyPI** — https://pypi.org → your account → *Publishing* → *Add a pending publisher*:
   - PyPI Project Name: `edc-client`
   - Owner: `CIR4FUN-EU`
   - Repository name: `edc-client`
   - Workflow name: `release.yml`
   - Environment name: `pypi`
2. **TestPyPI** — https://test.pypi.org → same *Add a pending publisher* form, identical
   values except Environment name: `testpypi`.
3. **GitHub environments** — repo → *Settings* → *Environments* → create `pypi` and
   `testpypi`. (Optional but recommended: add a required-reviewer protection rule on
   `pypi`.)

You need a PyPI and a TestPyPI account. No tokens go into the repository.

## Before tagging

Run from the repository root (the directory with `pyproject.toml`):

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
python -m pytest
```

Confirm `pyproject.toml` `[project].version` equals the tag you intend to push, and that
`CHANGELOG.md` has an entry for it.

## Publishing

The release is triggered by pushing a `v*.*.*` **tag**, not by pushing to `main`. So the
branch workflow and the release are independent: land your changes on `main` via a feature
branch and pull request, then tag the merged commit. `.github/workflows/release.yml` verifies
the tag matches the package version, builds the sdist + wheel, runs `twine check`, proves a
fresh install imports `edc_client`, publishes to **TestPyPI**, then to **PyPI**.

```bash
# 1. Prepare the release on a feature branch.
git checkout -b release/v1.0.0
# bump version in pyproject.toml + edc_client/__init__.py, add a CHANGELOG.md entry
git commit -am "Release v1.0.0"
git push -u origin release/v1.0.0

# 2. Open a PR into main on GitHub and merge it.

# 3. Get the merged commit locally. This matters: if the PR was squash/rebase-merged,
#    the merged commit has a different SHA than your branch — always pull before tagging.
git checkout main
git pull

# 4. Tag the merged commit (name must match pyproject.toml [project].version).
git tag v1.0.0

# 5. Push the tag to start the release workflow.
git push origin v1.0.0
```

Merging the PR does **not** release on its own — you push the tag when you're ready to
publish. Once the tag is pushed the workflow runs automatically. Do not delete or move a tag
after it has published. To release again, repeat from step 1 with the next version.
