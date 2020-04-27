# CMS password generator

## EUA

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

## CloudVPN

CloudVPN rules implemented in this script are:

- Cannot contain keyboard walks of 3 or more consecutive keyboard keys in a row
  (e.g. asd, zaq, 123, was, pol, ser, gyu, bhj, 9o0, p;[, etc.)
- Password length greater than 15 characters.
- Contain 3 out of 4 the following:
  - 1 digits (0-9).
  - 1 symbols (!, @, #, $, %, \*, etc.).
  - 1 uppercase English letters (A-Z).
  - 1 lowercase English letters (a-z).

Rules NOT implemented:

- Password must differ from previous password by 24 password(s).
- Password must be at least 1day(s) since last password change.

## Installation

You need python3:

```console
brew install python3
```

## Usage

It will generate random alphanumeric strings and mark those that EUA/CloudVPN
would reject as "failed", and stop when a string matches the rule set.

```console
$ python3 cmspw.py --help
usage: cmspw [-h] --ruleset RULESET [--length NUM]

generates passwords for CMS

optional arguments:
  -h, --help            show this help message and exit
  --ruleset RULESET, -r RULESET
                        rule set to validate against. can be one of ['eua', 'vpn'].
  --length NUM, -l NUM  password length. if ruleset is 'eua', this is ignored.
$ python3 cmspw.py --ruleset eua
failed 1MtIhKhA
passed qJbcNJ2Y
$ python3 cmspw.py --ruleset vpn --length 24
failed o[Pb*~9:)y8_<GH-99[cdR%N
passed 4H+-X^#XV(8'&wB5ZNn'H%>q
```

## Development

You need poetry:

```console
brew install poetry
```

Inside the project directory you can enter a virtual environment like so:

```console
poetry install && poetry shell
```
