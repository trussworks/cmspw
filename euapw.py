#!/usr/bin/env python3
#
"""
EUA password generator

EUA rules implemented in this script are:

- Must start with a letter
- At least one number (0-9)
- At least one Lowercase alphabetic character (a-z)
- At least one Upper Case alphabetic character (A-Z)
- MUST BE EXACTLY 8 characters long
- May not include "punctuation characters" (undocumented)

Rules NOT implemented:

- Cannot include your EUA UserID and any part of your name
- Cannot include any word/word portion prohibited by the defined CMS dictionary
- Password can’t contain 50% characters from previous password
- Be different from the previous 24 passwords

Usage:

$ python3 euapw.py
"""

import secrets
import string


def validate(candidate: str):
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
        candidate = ''.join(secrets.choice(alphabet) for i in range(length))

        if validate(candidate):
            print(f"passed {candidate}")
            break
        else:
            print(f"failed {candidate}")


if __name__ == "__main__":
    main()
