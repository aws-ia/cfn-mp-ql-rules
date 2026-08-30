import sys
from importlib.metadata import entry_points
from pathlib import Path

EXIT_CODES = {
    4: 0,
    8: 0,
    12: 0,
}


def _load_cfn_lint_entry_point():
    available = entry_points()
    if hasattr(available, "select"):
        matching = available.select(group="console_scripts", name="cfn-lint")
    else:
        matching = (
            entry_point
            for entry_point in available.get("console_scripts", ())
            if entry_point.name == "cfn-lint"
        )
    return next(iter(matching)).load()


def main():
    entrypoint_func = _load_cfn_lint_entry_point()
    custom_rule_location = Path(__file__).resolve().parent
    sys.argv[1:] = [f"-a={custom_rule_location}"] + sys.argv[1:]
    ec = entrypoint_func()
    sys.exit(EXIT_CODES.get(ec, ec))
