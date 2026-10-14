# Warehouse Asset Maintenance Registry

**Lab 5 — Static Code Analysis**

## Overview

The Warehouse Asset Maintenance Registry is a Python-based application that maintains records of warehouse assets, tracks their service dates, identifies assets due for inspection, and generates maintenance reports.

This project focuses on improving code quality, reliability, maintainability, and security by applying static code analysis tools and addressing issues identified in the original starter code.

## Objectives

- Analyze Python code using Pylint, Bandit, and Flake8.
- Identify potential bugs, security weaknesses, and code-quality issues.
- Document the issues found in the original starter code.
- Apply appropriate fixes to improve the program.
- Generate reports documenting the static analysis results.
- Reflect on the importance of static analysis in software development.

## Features

- **Asset registration:** Register warehouse assets with their IDs and machine types.
- **Service-date updates:** Update the last service date associated with an asset.
- **Inspection tracking:** Identify assets whose service dates exceed the configured maintenance interval.
- **Maintenance alerts:** Display alerts for assets due for inspection.
- **Service interval configuration:** Change the number of days between inspections.
- **JSON report generation:** Export registered asset information to `maintenance.json`.
- **Temporary report generation:** Create a temporary JSON copy of the asset registry.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application implementation |
| Pylint | Python code-quality analysis |
| Bandit | Security-focused static analysis |
| Flake8 | Style and linting checks |
| JSON | Maintenance data and report storage |
| Git and GitHub | Version control and project submission |

## Project Structure

```text
Warehouse_assets/
├── maintenance_system.py
├── issues.md
├── reflection.md
├── README.md
├── pylint_report.txt
├── bandit_report.txt
├── flake8_report.txt
└── maintenance.json          # Generated at runtime
```

`maintenance.json` is generated when the application runs and may not be present in a fresh checkout until the program is executed.

## Requirements

- Python 3.8 or later
- Pylint
- Bandit
- Flake8

Install the analysis tools using:

```bash
python -m pip install pylint bandit flake8
```

## How to Run the Application

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the application:

```bash
python maintenance_system.py
```

4. When prompted, enter a service date in `YYYY-MM-DD` format or press Enter to skip the update.
5. Review the maintenance alerts and generated report messages.

The program generates `maintenance.json` in the current working directory.

## Static Code Analysis

Three static analysis tools were used to evaluate the Python application.

### 1. Pylint

Pylint analyzes Python code for programming errors, coding-standard violations, and maintainability concerns.

Run:

```bash
python -m pylint maintenance_system.py
```

**Reported result:** 10.00/10.

### 2. Bandit

Bandit examines Python source code for common security issues.

Run:

```bash
python -m bandit -r maintenance_system.py
```

**Reported result:** No issues identified.

### 3. Flake8

Flake8 checks Python code for style violations and other linting problems.

Run:

```bash
python -m flake8 maintenance_system.py
```

**Reported result:** No reported violations.

The corresponding output files are included in the repository for review.

## Issues Identified and Fixes

The original starter code was reviewed for potential problems, including:

- Mutable default arguments.
- Bare exception handling.
- Missing asset and date validation.
- Unsafe temporary-file creation.
- Manual file handling without context managers.
- Invalid service intervals.
- Duplicate and empty asset IDs.
- Inconsistent logging and output.
- Non-idiomatic function naming.

The identified issues and their proposed fixes are documented in [`issues.md`](issues.md).

## Reflection

This lab demonstrates how static code analysis can help identify potential problems before software is deployed. Pylint helps improve code quality, Bandit focuses on security-related patterns, and Flake8 helps maintain consistent coding standards.

Using these tools alongside code review encourages early detection of defects and supports more reliable, readable, and maintainable Python applications.

Additional observations and learning outcomes are documented in [`reflection.md`](reflection.md).

## Repository Contents

- [`maintenance_system.py`](maintenance_system.py) — Python application source code.
- [`issues.md`](issues.md) — Issues identified in the original starter code and their fixes.
- [`reflection.md`](reflection.md) — Reflection on the lab and lessons learned.
- [`pylint_report.txt`](pylint_report.txt) — Pylint analysis output.
- [`bandit_report.txt`](bandit_report.txt) — Bandit analysis output.
- [`flake8_report.txt`](flake8_report.txt) — Flake8 analysis output.

## Conclusion

The Warehouse Asset Maintenance Registry was evaluated using Pylint, Bandit, and Flake8. The reported final results were a Pylint score of 10.00/10, no Bandit issues, and no Flake8 violations.

This exercise reinforces the value of combining automated static analysis with manual code review to improve software quality, security awareness, and maintainability.
 to present.
