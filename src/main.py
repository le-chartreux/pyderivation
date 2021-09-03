import sys
import utils as m_utils


def main():
    # this argument must exist since it's checked by the launcher
    formula = sys.argv[1]

    if m_utils.is_formula_valid(formula):
        print(m_utils.get_derivative(formula))
    else:
        raise ValueError("Error: invalid formula.")


if __name__ == '__main__':
    main()
