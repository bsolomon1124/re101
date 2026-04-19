# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- MIT license copyright years updated to 2018–2026; author name normalized to "Brad Solomon".

## [1.0.0] - 2026-04-18

### Added

- `CHANGELOG.md` in Keep a Changelog format (replaces `changelog.txt`).
- `.editorconfig` for consistent editor behavior.
- `CLAUDE.md` with project conventions for AI-assisted development.
- GitHub Actions CI workflow covering test, lint, type-check, and build
  across Python 3.10, 3.11, 3.12, 3.13, and 3.14.
- Expanded pytest suite (235 tests) reaching 100% line + branch coverage,
  covering every public constant, class, and helper.

### Changed

- **Breaking**: require Python `>=3.10, <3.15`. Support for 3.9 and earlier
  is dropped.
- **Breaking**: migrated packaging from `setup.py` + `requirements/` to
  `pyproject.toml` using the [`uv_build`](https://docs.astral.sh/uv/)
  backend. Source moved to `src/re101/` layout.
- Replaced `flake8` / `black` / `tox` with [`ruff`](https://docs.astral.sh/ruff/)
  (lint + format) and [`ty`](https://github.com/astral-sh/ty)
  (type-check), both configured in `pyproject.toml`.
- Modernized source: `typing.re.Pattern` → `re.Pattern[str]`, f-strings,
  PEP 604 unions (`X | None`), module-level `__version__`.
- README updated to describe the `uv`-based workflow.

### Removed

- **Breaking**: removed the `_DeprecatedRegex` wrapper and all deprecated
  lowercase aliases. Use the UPPERCASE constants instead:
  - `email` → `EMAIL`
  - `mult_whitespace` → `MULT_WHITESPACE`
  - `mult_spaces` → `MULT_SPACES`
  - `word` → `WORD`
  - `adverb` → `ADVERB`
  - `ipv4` / `IPv4` → `IPV4`
  - `moneysign` → `MONEYSIGN`
  - `zipcode` → `US_ZIPCODE`
  - `state` → `US_STATE`
  - `nanp_phonenum` → `US_PHONENUM`
- Removed `setup.py`, `requirements.txt`, `requirements/`, `tox.ini`,
  and `test.sh`.
- Removed author email from source code.

### Fixed

- `extract_us_drivers_license` now returns a sorted list of matches; it
  previously returned the `re` module itself when called without a
  `state` argument.
- Corrected `[A_Z]` typo in the Kentucky drivers-license regex.
- Fixed missing commas in several test-data lists that caused silent
  string concatenation, and removed a duplicate test-function name
  that shadowed its sibling.

## [0.4.0]

### Added

- `US_ADDRESS`, `LOOSE_EMAIL`, `IPV6` constants.
- Separate `requirements/` directory alongside `setup.py`.

### Changed

- Python `< 3.6` compatibility shim: removed f-strings, used
  `typing.re.Pattern` instead of `re.Pattern`.
- Slight accuracy tweaks to the `EMAIL` pattern and the
  username/password patterns.

## [0.3.4] - 2018-10-19

### Added

- `LOOSE_URL_DOMAIN`.

## [0.3.3] - 2018-10-19

### Changed

- Replaced `NON_US_PHONENUM` with the more narrowly-scoped
  `E164_PHONENUM`.

## [0.3.0] - 2018-10-18

### Added

- UPPERCASE naming convention for `re.Pattern` constants.
- `US_`-prefix convention for US-specific patterns.
- New constants: `PASSWORD`, `USERNAME`, `STRICT_SSN`, `LOOSE_SSN`,
  `STRICT_URL`, `LOOSE_URL`, `NON_US_PHONENUM`, `CREDIT_CARD`, `DOB`,
  `US_PASSPORT`.
- New helpers: `extract_pw`, `extract_un`, `extract_dob`,
  `extract_us_drivers_license` (provisional).

### Changed

- Overhauled `test_101.py` to use `pytest.mark.parametrize`.
- Legacy lowercase names kept as importable deprecation shims.

## [0.2.0] - 2017-05-07

### Added

- `Number`, `Decimal`, `Integer` classes.

### Changed

- Moved module contents from `re101/re101.py` to `re101/__init__.py`.

## [0.1.1] - 2018-02-19

### Changed

- README updates.

## [0.1.0] - 2018-02-13

### Added

- Initial commit and PyPI upload.

[Unreleased]: https://github.com/bsolomon1124/re101/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/bsolomon1124/re101/compare/v0.4.0...v1.0.0
[0.4.0]: https://github.com/bsolomon1124/re101/compare/v0.3.4...v0.4.0
[0.3.4]: https://github.com/bsolomon1124/re101/compare/v0.3.3...v0.3.4
[0.3.3]: https://github.com/bsolomon1124/re101/compare/v0.3.0...v0.3.3
[0.3.0]: https://github.com/bsolomon1124/re101/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/bsolomon1124/re101/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/bsolomon1124/re101/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/bsolomon1124/re101/releases/tag/v0.1.0
