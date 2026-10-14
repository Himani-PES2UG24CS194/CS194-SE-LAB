# Lab 5 — Static Code Analysis Issues

The following issues were identified in the original Warehouse Asset Maintenance Registry starter code through code review and static code analysis.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Reliability / Bug | 9 | The `register_asset()` function uses `logs=[]` as a default argument. The same list can be reused across function calls, causing unexpected state to persist. | Replace the mutable default with `None` and initialize a new list inside the function. |
| Bare exception handling | Error handling | 18–19 | The `update_service_date()` function uses a bare `except:` clause, which can hide unexpected errors and make debugging difficult. | Catch the expected exception, such as `KeyError` for an unknown asset, and handle it explicitly. |
| Missing asset and date validation | Input validation | 15–16 | The function updates an asset's service date without checking whether the asset exists or whether the date has a valid format. | Check that the asset exists and validate the date using `datetime.strptime()` before updating the registry. |
| Unsafe temporary file creation | Security | 30 | The `write_scratch_copy()` function uses `tempfile.mktemp()`, which can introduce a security risk because the temporary filename is generated without securely creating the file. | Use `tempfile.NamedTemporaryFile()` or another secure temporary-file creation method. |
| Files not managed with context managers | Reliability / Maintainability | 24–26, 31–33 | The report and scratch-copy functions open files and close them manually. An exception during writing could leave a file open. | Use `with open(...)` or a context manager to ensure files are closed properly. |
| Invalid service interval accepted | Input validation | 21–23, 45 | The `change_interval()` function accepts zero or negative values. The main function demonstrates this by setting the interval to `-30`, which can produce incorrect inspection results. | Validate that the service interval is a positive integer before updating the configuration. |
| Duplicate asset IDs overwrite existing records | Data integrity | 10, 41–42 | Registering an asset with an existing ID overwrites its existing record. The starter code registers `FL-01` twice with different machine types. | Check for duplicate asset IDs before registration and handle duplicates explicitly. |
| Invalid asset ID accepted | Input validation | 10, 40 | The program registers an asset with an empty ID, allowing an invalid record into the registry. | Reject empty or whitespace-only asset IDs before registration. |
| Inconsistent logging and output | Maintainability | 12, 19, 26, 35–36 | The program uses `print()` for operational messages despite importing `logging`. This makes output levels and error reporting harder to manage consistently. | Configure logging and use appropriate levels such as `logging.info()`, `logging.warning()`, and `logging.error()`. |
| Non-idiomatic function naming | Maintainability | 34 | The function `printAlerts()` uses camelCase rather than the conventional Python `snake_case` naming style. | Rename the function to `print_alerts()` and update its call sites. |

## Summary

The original starter code contains issues involving reliability, error handling, input validation, security, data integrity, file management, and maintainability. These issues were addressed through code improvements and static analysis.

### Final static analysis results

- **Pylint:** 10.00/10
- **Bandit:** No issues identified
- **Flake8:** No reported violations

The clean final reports indicate that the corrected code passes the configured static analysis checks. The issues documented above describe weaknesses identified in the original starter code, not necessarily findings reported directly by each analysis tool.
