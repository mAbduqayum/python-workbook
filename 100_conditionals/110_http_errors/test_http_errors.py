from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "status_code, expected_output",
    [
        (100, "Informational"),
        (150, "Informational"),
        (199, "Informational"),
        (200, "Success"),
        (250, "Success"),
        (299, "Success"),
        (300, "Redirection"),
        (350, "Redirection"),
        (399, "Redirection"),
        (400, "Client Error"),
        (404, "Client Error"),
        (499, "Client Error"),
        (500, "Server Error"),
        (550, "Server Error"),
        (599, "Server Error"),
        (99, "Unknown status code"),
        (600, "Unknown status code"),
        (999, "Unknown status code"),
        (0, "Unknown status code"),
    ],
)
def test_http_errors(script_runner, status_code, expected_output):
    script_path = Path(__file__).parent / "http_errors.py"

    if not script_path.exists():
        pytest.skip("Solution file http_errors.py not found")

    runner = script_runner(script_path)
    runner.run_and_check_output_only(
        input_text=f"{status_code}\n", expected_output=expected_output
    )