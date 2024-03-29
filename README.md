# Password Wizard 


![MIT Licence Badge](https://img.shields.io/badge/Licence-MIT-navy)
[![Bandit Badge](https://img.shields.io/badge/Bandit-Security?style=flat&label=Security&labelColor=58525B&color=%2303491D)](https://github.com/cjbagley/password-wizard/actions/workflows/bandit.yml)
[![Pylint Badge](https://img.shields.io/badge/Pylint-Linting?style=flat&label=Linting&labelColor=58525B&color=%2303491D)](https://github.com/cjbagley/password-wizard/actions/workflows/pylint.yml)
[![Ruff Badge](https://img.shields.io/badge/Ruff-Formatting?style=flat&label=Formatting&labelColor=58525B&color=%2303491D)](https://github.com/cjbagley/password-wizard/actions/workflows/ruff.yml)

## What is it?
A CLI tool that can:

- Check the [haveibeenpwned.com](https://haveibeenpwned.com) leaked password list to see if a given password has been leaked
- Generate a password string (with no matching records on [haveibeenpwned.com](https://haveibeenpwned.com))
- Generate a passphrase (with no matching records on [haveibeenpwned.com](https://haveibeenpwned.com))

The aim of creating this tool was to practice python (as I'm primarily a PHP developer) whilst also making something that I would use myself.

## How is the password checked?
The password is checked using the [haveibeenpwned.com API](https://haveibeenpwned.com/API/v3#PwnedPasswords).

## Wait, you are sending the password to another website? Isn't that a really bad idea?
Don't worry - no passwords are sent anywhere!

## So how do you check it then?
The link below has more information, but the short version: it uses something called the 'k-Anonymity model' to search previously leaked passwords by the first 5 characters of a *hash* of the password, not the password itself.
The password is hashed locally with a SHA-1 hash, and then only the first 5 characters of the hash are sent to the [haveibeenpwned.com](https://haveibeenpwned.com) API.
The API returns any matching hashes that start with those 5 characters (but only the remaining parts of the full hash string, i.e. they do not have the first 5 characters).
The results can then be combined with the original 5 characters locally to find if any combined hash matches the full hash of the password.
If a match has been found: that password has been leaked at some point.

More details [here](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/).

## Sounds good, how do I use it?

1. Download the source code or clone the repository.
2. Install requirements via the following:

```shell
pip install -r requirements.txt
```

3. It's ready to go! Currently, this is how you run it:

```shell
python -m password_wizard {command} {arguments...}
```

## Usage

### Password Check

```shell
python -m password_wizard check 
```

<p>
    <img src="https://res.cloudinary.com/dlrj5sbsg/image/upload/v1709219671/pww-check_tch8wa.gif" width=500 alt="Password Generation Demo">
</p>

```
options:
None
```

### Password Generation

```shell
python -m password_wizard password
```

<p>
    <img src="https://res.cloudinary.com/dlrj5sbsg/image/upload/q_auto/pww-password_c1qlu6.gif" width=500 alt="Password Generation Demo">
</p>

```
options:
  -l LENGTH,        Specify a length for the generated password.
  --length LENGTH   The length should be a number passed along with this option, for example '-l 20'.
                    The number must be between 5 and 20.
                    (default: 18)
  -s                By default, a full punctuation list is used when generating the random string.
                    To use only a set selection of special characters, e.g. only use a special
                    character from one of w '#!_', this flag can be set.
                    No value should be given, and a separate prompt will appear in which to enter
                    the special characters to use.
                    (default: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
  -ns               By default, special characters will be included in the generated password.
                    To exclude any special characters from being used, this flag can be set.
                    No option value should be given, and this option will override any other special 
                    character related options.
```

### Passphrase Generation

```shell
python -m password_wizard passphrase 
```

<p>
    <img src="https://res.cloudinary.com/dlrj5sbsg/image/upload/q_auto/pww-passphrase_snazq6.gif" width=500 alt="Password Generation Demo">
</p>

```
options:
  -w WORDS,         Specify the number of words to use for the generated passphrase.
  --words WORDS     The number should be passed along with this option, for example '-w 5'.
                    The number must be between 3 and 8.
                    (default: 4)
  -s, --separator   Specify a separator between words.
                    No value should be given, and a separate prompt will appear in which to enter
                    a separator to use.
                    The first given separator will be used.
                    (default: No separator)
```

## Possible Todo Items for future versions
- Figure out how to properly package it
- Implement a GUI
- Add ability to point to a different wordlist to use
- Lookup a password against a list of bad passwords, and do not use if it's on the list
- Add a 'higher or lower' game: given two bad passwords, guess which of the two has been leaked the most amount of times
