import pytest
from cmspw import __main__ as cmspw

pre_str = "1%______"
end_str = "_______M"

cloudvpn = [
    ("pheifoeX6eehoo", False),
    ("pheifoeX6eehoo#a", True),
    (pre_str + end_str, True),
    (pre_str + "qws" + end_str, False),
    (pre_str + "~1q" + end_str, False),
    (pre_str + "+{]" + end_str, False),
    (pre_str + "+[]" + end_str, False),
    (pre_str + "/:." + end_str, False),
    (pre_str + "/:`" + end_str, True),
    (pre_str + "hqK" + end_str, True),
    (pre_str + "hgf" + end_str, False),
    (pre_str + "hhg" + end_str, True),
    (pre_str + "hfg" + end_str, True),
    (pre_str + ".<l" + end_str, False),
    (pre_str + "-{}" + end_str, False),
    (pre_str + "{[}" + end_str, True),
    ("", False),
]


@pytest.mark.parametrize("pwd, expected", cloudvpn)
def test_cloudvpn(pwd, expected):
    assert cmspw.validate_cloudvpn(pwd) == expected
