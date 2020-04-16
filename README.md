# EUA password generator

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

## Installation

You need python3:

```console
brew install python3
```

Copy `euapw.py` anywhere convenient.

## Usage

It will generate random alphanumeric strings and mark those that EUA would
reject as "failed", and stop when a string matches the rule set.

```console
$ python3 euapw.py
failed 1MtIhKhA
passed qJbcNJ2Y
```

## Development

You need poetry:

```console
brew install poetry
```

Inside the project directory you can enter a virtual environment like so:

```console
poetry shell
```
