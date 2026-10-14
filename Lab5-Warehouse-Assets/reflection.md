# Lab 5 — Reflection

**Note:** The supplied handout describes four reflection questions but the uploaded copy does not show the actual questions. These draft responses cover the lab's stated learning outcomes; adjust the headings if your instructor provided the questions separately.

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It helps identify potential bugs, security risks, maintainability problems, and style violations early. It complements testing because it can flag suspicious patterns even when a particular execution path has not been tested.

## 2. What is the difference between Pylint, Flake8, and Bandit?

Pylint focuses on code quality, possible logical errors, naming, design, and maintainability. Flake8 focuses mainly on Python style and common errors, including PEP 8 formatting. Bandit scans Python code for common security-related patterns. Using all three provides broader coverage than relying on only one tool.

## 3. What issues did you find, and how did you fix them?

The original code used a mutable list as a default argument, caught every exception in a date update, compared a date/time value with a `timedelta` incorrectly in the inspection check, and did not validate service dates or inspection intervals. I changed the default argument to `None`, caught the expected `ValueError`, compared elapsed dates with a `timedelta`, and added checks for date format, future dates, and positive interval values. I also improved file handling by using context managers and configured logging.

## 4. How did static analysis improve the program, and what are its limitations?

Static analysis helped identify style and quality concerns that are easy to overlook during manual review. Fixing the findings made the program easier to read, more predictable when receiving invalid input, and more maintainable. However, static analysis cannot prove that a program is completely correct: the program still needs to be run with normal, boundary, and invalid inputs, and the generated reports must be reviewed rather than blindly followed.
