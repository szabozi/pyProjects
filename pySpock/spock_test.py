from spock_decorators import given, when, then, where


@given("two numbers {} and {}")
def set_numbers(a, b):
    return a, b


@when("they are added")
def add_numbers(a, b):
    return a + b


@then("the results should be {}")
def check_results(result, expected_sum):
    assert result == expected_sum, f"Expected {expected_sum}, but got {result}"


@where(
    # a, b, expected_sum
    (1, 1, 2),
    (2, 3, 5),
    (5, 7, 12),
    (0, 0, 0)
)
def test_addition(a, b, expected_sum):
    a, b = set_numbers(a, b)
    result = add_numbers(a, b)
    check_results(result, expected_sum)


if __name__ == "__main__":
    test_addition()
