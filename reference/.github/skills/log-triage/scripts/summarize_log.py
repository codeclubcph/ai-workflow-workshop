"""Summarise an application log so an AI agent doesn't have to read every line.

Usage: python summarize_log.py <logfile>
Standard library only.
"""
import re
import sys
from collections import Counter

LINE = re.compile(r"^(?P<ts>\S+)\s+(?P<level>INFO|WARN|WARNING|ERROR|DEBUG|CRITICAL)\s+(?P<msg>.*)$")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
SQL_INJECTION = re.compile(r"('\s*OR\s*'?\d'?\s*=\s*'?\d)|(--\s*$)|(;\s*DROP\s)", re.IGNORECASE)
SECRET = re.compile(r"(password|passwd|secret|api[_-]?key|token)\s*[=:]", re.IGNORECASE)


def normalise(msg: str) -> str:
    """Collapse numbers/ids so similar messages group together."""
    msg = re.sub(r"\d+", "N", msg)
    return msg[:140]


def main(path: str) -> None:
    levels: Counter = Counter()
    errors: Counter = Counter()
    warnings: Counter = Counter()
    exceptions: Counter = Counter()
    suspicious: list[str] = []
    first_ts = last_ts = None

    with open(path, encoding="utf-8", errors="replace") as f:
        for n, raw in enumerate(f, start=1):
            line = raw.rstrip("\n")
            m = LINE.match(line)
            if m:
                first_ts = first_ts or m["ts"]
                last_ts = m["ts"]
                levels[m["level"]] += 1
                if m["level"] in ("ERROR", "CRITICAL"):
                    errors[normalise(m["msg"])] += 1
                elif m["level"] in ("WARN", "WARNING"):
                    warnings[normalise(m["msg"])] += 1
            elif re.match(r"^\w*(Error|Exception)\b", line):
                exceptions[line.strip()[:160]] += 1
            elif line.strip().startswith('File "'):
                exceptions["  at " + line.strip()[:160]] += 0  # keep location visible

            if SQL_INJECTION.search(line):
                suspicious.append(f"L{n} possible SQL injection: {line[:160]}")
            if EMAIL.search(line):
                suspicious.append(f"L{n} personal data (email) in log: {line[:120]}")
            if SECRET.search(line):
                suspicious.append(f"L{n} possible secret in log: {line[:120]}")

    print(f"# Log summary: {path}")
    print(f"Time range: {first_ts} -> {last_ts}")
    print("Levels: " + ", ".join(f"{k}={v}" for k, v in levels.most_common()))

    print("\n## Top errors")
    for msg, count in errors.most_common(10):
        print(f"{count:>4}x  {msg}")

    print("\n## Top warnings")
    for msg, count in warnings.most_common(10):
        print(f"{count:>4}x  {msg}")

    print("\n## Exceptions and stack locations")
    for msg, count in exceptions.most_common(15):
        print(f"{count:>4}x  {msg}" if count else f"       {msg}")

    print("\n## Suspicious lines (security / privacy)")
    for item in suspicious[:20] or ["none found"]:
        print(f"- {item}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python summarize_log.py <logfile>")
    main(sys.argv[1])
