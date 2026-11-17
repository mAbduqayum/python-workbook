import pytest


@pytest.mark.parametrize(
    "status_code, expected_output",
    [
        (100, "informational"),
        (150, "informational"),
        (199, "informational"),
        (200, "success"),
        (250, "success"),
        (299, "success"),
        (300, "redirection"),
        (350, "redirection"),
        (399, "redirection"),
        (400, "client error"),
        (404, "client error"),
        (499, "client error"),
        (500, "server error"),
        (550, "server error"),
        (599, "server error"),
        (99, "unknown status code"),
        (600, "unknown status code"),
        (999, "unknown status code"),
        (0, "unknown status code"),
    ],
)
def test_http_errors(solution, status_code, expected_output):
    solution.check_output(
        input_text=f"{status_code}\n", expected_output=expected_output
    )
