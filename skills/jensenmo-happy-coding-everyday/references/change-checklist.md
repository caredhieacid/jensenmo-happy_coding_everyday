# Change checklist

A quick completeness scan, run while reviewing your final diff, for any change to logic, data, an interface, or UI, and for any bug fix. Read only the rows that match what you changed and handle what applies; skip the rest without comment. This is a memory aid, not a process: it adds no write-up and no new features.

Cover a case with an existing mechanism or a test before adding code. If a row points at something nobody asked for (a limit, a new option, extra hardening), mention it in the report instead of building it.

| You changed | Check briefly |
| --- | --- |
| Any logic | Empty, zero, one, many, and maximum inputs; invalid input; the error path; every caller of what you changed |
| A bug | A test that fails without the fix; the same mistake elsewhere (search); the root cause, not only the symptom |
| A public function, API, CLI, file format, or config key | Backward compatibility, defaults, validation messages, docs that list it, and known consumers |
| An endpoint, handler, job, or tool | Authorization, input validation, error responses, retry safety where it can be retried, and limits where input is unbounded |
| Stored data or a schema | Existing rows, defaults and nullability, migration and rollback, indexes for new queries, concurrent writers |
| Money, time, or text | Decimal arithmetic and the rounding rule; time zones, date boundaries, and daylight-saving changes; encoding, Unicode, and long strings |
| Concurrency, I/O, or network | Timeouts, retries, cancellation, partial failure, ordering, and resource cleanup |
| A loop or query on a hot path | Unbounded growth, one query per item, and repeated work that could be done once |
| UI | Loading, empty, and error states; long text and narrow screens; keyboard and labels; the product's existing look and words, with one name for each thing |
| A dependency or build setting | Need, maintenance, license, size, and the lockfile |
| A removal or rename | Every reference, including config, docs, scripts, and tests; a deprecation path when outside callers exist |

Professional code reads plainly: names say what things are, logic you introduced is not duplicated, comments explain only a non-obvious why, and no debug output, commented-out code, or leftover to-do notes remain. Everything you handled or deliberately left out that a user or caller would notice belongs in the report.
