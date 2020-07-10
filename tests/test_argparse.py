import pytest
from cmspw import __main__ as cmspw


@pytest.fixture
def argparse_mock(mocker):
    return mocker.patch("argparse.ArgumentParser", autospec=True)


def test_argparser_called(argparse_mock):
    cmspw.parse_args()
    argparse_mock.assert_called_once_with(
        prog="cmspw", description="generates passwords for CMS"
    )
