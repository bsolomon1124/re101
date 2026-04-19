# CLAUDE.md

Guidance for Claude Code working in this repo.

## What this is

`re101` — a single-module library of curated `re.Pattern[str]` objects,
plus a small number of helper classes and `extract_*` functions. All
source lives in `src/re101/__init__.py`; all tests in
`tests/test_101.py`. Resist splitting either file.

## Common commands

Use Taskfile shortcuts (`task --list`) or their underlying invocations:

- `task install` — `uv sync --all-groups`
- `task test` — `uv run pytest --cov --cov-report=term`
- `task test-all` — run tests on Python 3.10 → 3.14
- `task fmt` — `uv run ruff format .` + `ruff check --fix`
- `task lint` — ruff (check + format-check) + `ty check` + markdownlint-cli2
- `task build` — `uv build` (sdist + wheel)
- `task hooks` / `task hooks-run` — manage prek hooks

## Conventions

- New regex constants: UPPERCASE, `US_`-prefixed if US-specific, with a
  source citation comment.
- New `extract_*` helpers: return `list[str]`, take a single positional
  `str` argument.
- Every new pattern gets both a positive and a negative case in the
  `SEARCH_CASES` / `EXTRA_SEARCH_CASES` table.
- Keep coverage at 100%. Coverage is enforced in CI.
- Bump `version` in **both** `pyproject.toml` and `src/re101/__init__.py`
  (`__version__`); add a new `[x.y.z] - YYYY-MM-DD` section to
  `CHANGELOG.md` under `[Unreleased]` and update the compare-link footer.

## Style

- Python `>=3.10, <3.15`. Use PEP 604 unions, `list[str]`,
  `re.Pattern[str]`, `Literal`, `TypeAlias`. `from __future__ import
  annotations` is already on.
- Ruff ruleset: E/W/F/I/N/D/UP/B/A/C4/SIM/PT/PTH/PIE/RET/TID/RUF. Ignore
  the regex-unfriendly rules listed in `pyproject.toml`.
- Docstring convention: NumPy (configured in ruff).
- Quote style: preserve (single quotes throughout, by convention).

## Don't

- Don't restore `setup.py`, `requirements.txt`, `tox.ini`, or the
  deprecated lowercase aliases (`email`, `ipv4`, `zipcode`, …). These
  were removed in 1.0.0.
- Don't add hard runtime dependencies — this package is stdlib-only on
  purpose.
- Don't re-introduce `typing.re.Pattern`; it was removed in Python 3.12.
- Don't pin GitHub Actions to floating tags. CI requires 40-char commit
  SHAs with the tag preserved as a trailing comment.
- Don't use `--no-verify` to bypass pre-commit, and don't skip the test
  gate. Publishing via tag-push runs the full matrix first.

## Release (human-triggered)

1. Update `version` (both places) and `CHANGELOG.md` in a PR.
2. Merge to `master`.
3. `git tag -s v$VERSION && git push origin v$VERSION`. This triggers
   `.github/workflows/publish.yml`, which runs the test matrix, builds
   sdist + wheel, emits an SBOM, Sigstore-signs every artifact,
   publishes to PyPI via OIDC Trusted Publisher, and creates the
   GitHub Release.

## Known quirks

- `IPV4` accepts zero-padded low octets by design (see RFC comment).
- `US_ADDRESS` requires capitalized street names to cut false positives.
- `Number` / `Integer` / `Decimal` anchor on whitespace/string bounds
  and will not match mid-token.
- `MONEYSIGN` is a `str`, not a `Pattern`.

## Pull request titles

Follow Conventional Commits format: `<type>: <description>` (e.g. `chore: update dependencies`, `fix: handle edge case`, `feat: add new pattern`).
