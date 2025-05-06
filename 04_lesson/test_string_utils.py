import pytest

from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, result",
    [
        ("  Buratino", "Buratino"),
        ('     2025 0 12', '2025 0 12'),
        ("       friday 13", "friday 13"),
    ],
)
def test_trim_positive(string, result):
    assert string_utils.trim(string) == result


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, result",
    [
        ("", ""),
        ("  ", " "),
        (1, None),
        ([], None),
    ],
)
def test_trim_negative(string, result):
    assert string_utils.trim(string) == result


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("Buratino", "B"),
        ('2025 0 12', '2025'),
        ("friday 13", "week 14"),
    ],
)
def test_cont_positive(string, symbol):
    res = string_utils.contains(string, symbol)
    if res is True:
        assert res is True
    else:
        assert res is False


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("", ""),
        ("  ", " "),
        (1, None),
        ([], 0),
    ],
)
def test_cont_negative(string, symbol):
    res = string_utils.contains(string, symbol)
    if res is True:
        assert res is True
    else:
        assert res is False


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("Buratino", "in", "Burato"),
        ('2025 0 12', '02', '25 0 12'),
        ("friday 13", "fri", "day 13"),
    ],
)
def test_delete_sym_positive(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("", "", ""),
        ("  ", " ", ""),
        (122, 2, 12),
        ([], 0, None),
    ],
)
def test_delete_sym_negative(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, result",
    [
        ("buratino", "Buratino"),
        ("x-file", "X-file"),
        ("2 восточный", "2 восточный")
    ],
)
def test_trim_positive1(string, result):
    assert string_utils.capitalize(string) == result


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, result",
    [
        ("", ""),
        ("  ", " "),
        (2025, None),
        ([], None)
    ],
)
def test_trim_negative1(string, result):
    assert string_utils.capitalize(string) == result
