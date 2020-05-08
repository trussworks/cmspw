import pytest
from cmspw import __main__ as cmspw


eua = [
    ("maia5Chi", True),
    ("maia5chi", False),
    ("MAIA5CHI", False),
    ("0aia5Chi", False),
    ("ma!a5Chi", False),
    ("maiza5Chi", False),
    ("maiza5C", False),
    ("a", False),
]


@pytest.mark.parametrize("pwd, expected", eua)
def test_eua(pwd, expected):
    assert cmspw.validate_eua(pwd) == expected
