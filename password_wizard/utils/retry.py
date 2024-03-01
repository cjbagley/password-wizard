"""Helper to call the 'Have I Been Pwned' API x number of retries if
a generated password shows as having previously been leaked.
"""

from password_wizard.api.hibp import get_matched_hash_count
from password_wizard.cli.options.abstract_option import ExecuteResult
from password_wizard.utils.utils import sha1_hash


def find_non_leaked_password(generator_func, retries: int = 10) -> ExecuteResult:
    """Call the 'Have I Been Pwned' api x times until a result with no matching
    hashes has been found. The generator_func should generate the final password,
    passphrase etc. for this function to hash and send to the API.
    """
    count = 0
    while count < retries:
        pw = generator_func()
        if get_matched_hash_count(sha1_hash(pw)) == 0:
            return ExecuteResult(exit_code=0, output=pw)
        count += 1

    return ExecuteResult(
        exit_code=1,
        output="Exceeded maximum tries when calling 'Have I Been Pwned' API",
    )
