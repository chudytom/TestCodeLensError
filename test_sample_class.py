import pytest

from sample_class import SampleClass


@pytest.mark.parametrize((
    "x,"
    "y,"
    "expected_result"), [
        (0, 0, 0),
        (3, 2, 6)
    ]
)
def test_return_1(x, y, expected_result):

    sample_class = SampleClass()
    value = sample_class.Multiply(x, y)

    assert value == expected_result
