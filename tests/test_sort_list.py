import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from sort_list import sort_list

SCRIPT_PATH = PROJECT_ROOT / "sort_list.py"


def run_script(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), *args],
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([3, 1, 2], [1, 2, 3]),
        ([], []),
        ([-2, 5, 0], [-2, 0, 5]),
    ],
)
def test_sort_list(numbers, expected):
    assert sort_list(numbers) == expected


def test_cli_sorts_numbers():
    result = run_script("3", "1", "2")
    assert result.returncode == 0
    assert result.stdout.strip() == "1 2 3"
    assert result.stderr == ""


def test_cli_no_arguments_shows_usage():
    result = run_script()
    assert result.returncode == 1
    assert "Usage: python sort_list.py" in result.stdout
    assert result.stderr == ""


def test_cli_rejects_non_integer_arguments():
    result = run_script("1", "a", "2")
    assert result.returncode == 1
    assert result.stdout.strip() == "Error: all arguments must be integers."
    assert result.stderr == ""
