import pytest


@pytest.mark.parametrize(
    "height, weight, expected_output",
    [
        (1.65, 45, "underweight"),  # BMI ≈ 16.53
        (1.70, 50, "underweight"),  # BMI ≈ 17.30
        (1.70, 55, "normal weight"),  # BMI ≈ 19.03
        (1.75, 70, "normal weight"),  # BMI ≈ 22.86
        (1.60, 60, "normal weight"),  # BMI ≈ 23.44
        (1.75, 75, "normal weight"),  # BMI ≈ 24.49
        (1.75, 85, "overweight"),  # BMI ≈ 27.76
        (1.80, 90, "overweight"),  # BMI ≈ 27.78
        (1.60, 80, "obese"),  # BMI ≈ 31.25
        (1.75, 100, "obese"),  # BMI ≈ 32.65
        (1.70, 120, "obese"),  # BMI ≈ 41.52
    ],
)
def test_bmi_categories(solution, height, weight, expected_output):
    solution.check_output(
        input_text=f"{height}\n{weight}\n", expected_output=expected_output
    )
