from my_funcs.utils import division
import pytest


@pytest.mark.parametrize("divider_one, divider_two, expected_result", [
    (10, 2, 5),
    (20, 10, 2),
    (30, -3, -10),
    (5, 2, 2.5),
])
def test_division_good(divider_one, divider_two, expected_result):
    assert division(divider_one, divider_two) == expected_result


@pytest.mark.parametrize("error_expected, divider_mistake", [
    (ZeroDivisionError, 0),
    (TypeError, "0"),
])
def test_division_error(error_expected, divider_mistake):
    with pytest.raises(error_expected):
        division(10, divider_mistake)
