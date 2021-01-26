import re
num_evaluator = re.compile(r'\d+')


def is_valid_number(n: str):

    if num_evaluator.fullmatch(n):
        n_int = int(n)

        if 1 <= n_int <= 10000:
            return True

    return False
