# Password Wizard 

<p>
    <img alt="MIT Licence Badge" src="https://img.shields.io/badge/Licence-MIT-blue">
    <img alt="Bandit Badge" src="https://github.com/cjbagley/password-wizard/actions/workflows/bandit.yml">
</p>

## What is it?
A CLI tool that can:

- Check the [haveibeenpwned.com] (https://haveibeenpwned.com) leaked password list to see if a given password has been leaked
- Generate a password string (which also has no matching records on haveibeenpwned.com)
- Generate a passphrase (which also has no matching records on haveibeenpwned.com)

The aim of this tool was to learn some python (as I've primarily been a PHP developer) but also to make something I would use myself.

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

