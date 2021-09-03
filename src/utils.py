import re


def is_formula_valid(formula: str) -> bool:
    """
    Checks if the formula is valid.

    :param formula: the formula to check
    :return: if the formula is valid
    """
    return bool(
        re.match(
            r"(-?\d+)",
            formula
        )
    )


def get_derivative(formula: str) -> str:
    """
    Computes the derivative of the given formula.

    :param formula: the formula of which we want the derivative. Must be valid
    :return: the derivative of the given formula
    """
    pass
