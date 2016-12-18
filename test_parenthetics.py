"""Test file for parenthetics.py."""


import pytest

TEST_LIST = [
    ['((()))', 0],
    ['(what((for)jds', 1],
    ['hi () whst(idf)jkdf0)', -1],
    [')jfei()nsdf(fnif)j(', -1],
    ['()dhuew(dai0dasud)dnaudb(fkabfa(fkhaush)', 1],
    ['adfi()fhsd(ffjausd)fhaeb()hfa9', 0],
]


@pytest.mark.parametrize('input, answer', TEST_LIST)
def test_parenthetics_return(input, answer):
    """Test that parenthetics returns the proper value."""
    from parenthetics import parenthetics
    assert parenthetics(input) is answer
