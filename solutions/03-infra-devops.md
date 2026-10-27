# Exercise 03 - Infrastructure and DevOps: solution

## Part A: Dockerfile review

The supplied `infra/Dockerfile` has these problems:

1. `python:latest` is a floating tag; choose a supported version, and use an
   immutable digest if reproducible builds require it.
2. `requirements.txt` does not exist. `requirements-dev.txt` contains pytest
   for development; the application itself uses only the Python standard
   library.
3. `COPY . .` puts the whole repository into the image instead of limiting
   copied files to what the service needs.
4. The default user is root; production containers should run as an unprivileged
   user where practical.
5. It exposes port 8080, while `src/orders/app.py` listens on 8000.
6. `CMD ["python", "app.py"]` points to a file that does not exist and does not
   use the documented module entry point.

A valid design uses a selected Python image, copies the service source, sets a
working directory where `orders` can be imported, runs
`python -m orders.app`, and exposes port 8000. Since the service has no runtime
third-party dependencies, it need not install pytest into a production image.
Many Dockerfiles can satisfy these requirements; the exercise is to verify the
proposed image against repository contents rather than match one exact answer.

## Part B: CI workflow (`.github/workflows/ci.yaml`)

The four problems:

1. **Wrong branch:** `push` triggers only on `master`, but the default branch is
   `main`, so pushes to `main` never run CI. Use `branches: [main]`.
2. **YAML number trap:** unquoted `python-version: 3.10` is parsed as the number
   `3.1`, so `setup-python` looks for Python 3.1. Quote it: `"3.10"` (or use
   `"3.13"`; the project requires 3.11+, so 3.10 is also too old).
3. **Missing file:** `pip install -r requirements.txt` fails because the repo
   has `requirements-dev.txt`.
4. **Wrong test path:** `pytest test/` points to a folder that doesn't exist;
   the tests are in `tests/`.

Each fix is one line in the workflow. Verify claims against the repository
(branch name, file names, folder names) rather than trusting an AI's answer.

## Part C: log triage

| Log evidence | Explanation and limits | Suggested next step |
|---|---|---|
| `/orders?page=3` returns zero items although `total_pages=3` | Consistent with the 1-based pagination offset bug in `src/orders/pagination.py`. | Verify with tests and correct the offset. |
| `/orders?page=next` returns 500 and traceback shows `int(...)` raising `ValueError` in `src/orders/app.py` | The endpoint does not validate the page parameter; invalid user input becomes an unhandled server error. | Validate input and return a client error such as 400; add tests. |
| Health checks take over two seconds, liveness probes fail, then the container restarts | The log attributes the restart to liveness failure and says it was not OOM-killed. It does not show why the endpoint became slow. | Check health-handler dependencies, runtime/resource metrics, and probe settings. |
| Query contains `x' OR '1'='1`; 4,182 rows are reported | Suspicious and consistent with SQL injection. Unsafe f-string SQL exists in `src/orders/repository.py`; log alone cannot prove authorization or which data was accessed. | Parameterize SQL and investigate access/audit records and returned data. |
| Email addresses and a query selecting customer/email fields appear in logs | Personal/customer information and query details are exposed. | Minimize and redact logged data; review access and retention controls. |

Be explicit about what the logs prove versus what remains unknown. The example
addresses and identities are workshop data.
