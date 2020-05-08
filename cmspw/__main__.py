#!/usr/bin/env python3
#
"""
CMS password generator
"""

import argparse
import secrets
import string
from .data.kbmap import qwerty as kbmap


def parse_args() -> argparse.Namespace:
    """Define an argument parser and return the parsed arguments."""
    parser = argparse.ArgumentParser(
        prog="cmspw", description="generates passwords for CMS",
    )
    parser.add_argument(
        "--ruleset",
        "-r",
        help="rule set to validate against. can be one of ['eua', 'vpn'].",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--length",
        "-l",
        help="password length. if ruleset is 'eua', this is ignored.",
        type=int,
        metavar="NUM",
        default=0,
    )

    return parser.parse_args()


def validate_cloudvpn(candidate: str) -> bool:
    """
    Validate a candidate password according to CloudVPN rules
    """
    try:
        # Cannot contain keyboard walks of 3 or more consecutive keyboard keys
        # in a row
        # (e.g. asd, zaq, 123, was, pol, ser, gyu, bhj, 9o0, p;[, etc.)

        chunks = [candidate[i : i + 3] for i in range(0, len(candidate) - 2)]
        for chunk in chunks:
            assert not all(
                (
                    chunk[0] in kbmap[chunk[1]],
                    chunk[1] in kbmap[chunk[0]],
                    chunk[1] in kbmap[chunk[2]],
                    chunk[2] in kbmap[chunk[1]],
                )
            )

        # Password length greater than 15 characters.
        assert len(candidate) > 15

        # Contain 3 the following:
        # - 1 digits (0-9).
        # - 1 symbols (!, @, #, $, %, *, etc.).
        # - 1 uppercase English letters (A-Z).
        # - 1 lowercase English letters (a-z).
        assert (
            any(char in string.digits for char in candidate)
            + any(char in string.punctuation for char in candidate)
            + any(char in string.ascii_uppercase for char in candidate)
            + any(char in string.ascii_lowercase for char in candidate)
        ) >= 3
    except AssertionError:
        return False
    else:
        return True


def validate_eua(candidate: str) -> bool:
    """
    Validate a candidate password according to EUA rules
    """
    try:
        # Must start with a letter
        assert candidate[0] in string.ascii_letters
        # At least one number (0-9)
        assert any(char in string.digits for char in candidate)
        # At least one Lowercase alphabetic character (a-z)
        assert any(char in string.ascii_lowercase for char in candidate)
        # At least one Upper Case alphabetic character (A-Z)
        assert any(char in string.ascii_uppercase for char in candidate)
        # MUST BE EXACTLY 8 characters long
        assert len(candidate) == 8
        # May not include "punctuation characters" (undocumented)
        assert not any(char in string.punctuation for char in candidate)
    except AssertionError:
        return False
    else:
        return True


def main():
    args = parse_args()

    _dispatch = {
        "eua": {
            "validator": validate_eua,
            "length": 8,
            "min_length": 8,
            "max_length": 8,
            "alphabet": string.ascii_letters + string.digits,
        },
        "vpn": {
            "validator": validate_cloudvpn,
            "length": args.length or 16,
            "min_length": 16,
            "max_length": None,
            "alphabet": string.ascii_letters
            + string.digits
            + string.punctuation,
        },
    }
    try:
        validator = _dispatch[args.ruleset].get("validator")
        alphabet = _dispatch[args.ruleset].get("alphabet")
        length = _dispatch[args.ruleset].get("length")
        min_length = _dispatch[args.ruleset].get("min_length")
        max_length = _dispatch[args.ruleset].get("max_length")
    except KeyError:
        print(f"Ruleset not found: {args.ruleset}")
        print("Must be one of {}".format(list(_dispatch)))
        return 1

    if not min_length <= length <= (max_length or 9999):
        print(f"Password length {length} out of bounds")
        print(f"Minimum length: {min_length}")
        print(f"Maximum length: {max_length}")
        return 1

    while True:
        candidate = "".join(secrets.choice(alphabet) for i in range(length))

        if validator(candidate):
            print(f"passed {candidate}")
            break
        else:
            print(f"failed {candidate}")


if __name__ == "__main__":
    main()
