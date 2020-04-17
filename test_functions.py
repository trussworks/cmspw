import pytest
import cmspw

pre_str = "a%che1mk"
end_str = "fhXek6^a"

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
]


@pytest.mark.parametrize("pwd, expected", cloudvpn)
def test_cloudvpn(pwd, expected):
    assert cmspw.validate_cloudvpn(pwd) == expected


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