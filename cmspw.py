#!/usr/bin/env python3
#
"""
CMS password generator
"""

import secrets
import string
import json


def validate_cloudvpn(candidate: str) -> bool:
    """
    Validate a candidate password according to CloudVPN rules
    """
    try:
        # Cannot contain keyboard walks of 3 or more consecutive keyboard keys
        # in a row
        # (e.g. asd, zaq, 123, was, pol, ser, gyu, bhj, 9o0, p;[, etc.)
        with open("kbmap.json") as file:
            kbmap = json.load(file)

            chunks = [
                candidate[i : i + 3] for i in range(0, len(candidate) - 2)
            ]
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
        (
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


def main(length=8):
    while True:
        alphabet = string.ascii_letters + string.digits
        candidate = "".join(secrets.choice(alphabet) for i in range(length))

        if validate_eua(candidate):
            print(f"passed {candidate}")
            break
        else:
            print(f"failed {candidate}")


if __name__ == "__main__":
    main()
