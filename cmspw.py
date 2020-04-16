#!/usr/bin/env python3
#
"""
CMS password generator
"""

import secrets
import string


def validate_eua(candidate: str):
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
