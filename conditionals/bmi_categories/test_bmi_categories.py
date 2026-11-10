import pytest


@pytest.mark.parametrize(
    "height, weight, expected_output",
    [
        (1.65, 45, "Underweight"),  # BMI ≈ 16.53
        (1.70, 50, "Underweight"),  # BMI ≈ 17.30
        (1.70, 55, "Normal weight"),  # BMI ≈ 19.03
        (1.75, 70, "Normal weight"),  # BMI ≈ 22.86
        (1.60, 60, "Normal weight"),  # BMI ≈ 23.44
        (1.75, 75, "Normal weight"),  # BMI ≈ 24.49
        (1.75, 85, "Overweight"),  # BMI ≈ 27.76
        (1.80, 90, "Overweight"),  # BMI ≈ 27.78
        (1.60, 80, "Obese"),  # BMI ≈ 31.25
        (1.75, 100, "Obese"),  # BMI ≈ 32.65
        (1.70, 120, "Obese"),  # BMI ≈ 41.52
    ],
)
def test_bmi_categories(solution, height, weight, expected_output):
    solution.check_output(
        input_text=f"{height}\n{weight}\n", expected_output=expected_output
    )
