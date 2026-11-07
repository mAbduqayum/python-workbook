def test_fizz_buzz(solution):
    result = solution.run(input_text="")

    lines = result.stdout.strip().split("\n")

    assert len(lines) == 100

    assert lines[0] == "1"
    assert lines[1] == "2"
    assert lines[2] == "Fizz"
    assert lines[3] == "4"
    assert lines[4] == "Buzz"
    assert lines[5] == "Fizz"
    assert lines[14] == "FizzBuzz"
    assert lines[29] == "FizzBuzz"
    assert lines[99] == "Buzz"
