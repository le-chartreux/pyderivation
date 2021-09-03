import unittest
import random

import utils as m_utils


class TestDirection(unittest.TestCase):

    def test_is_formula_valid(self):
        formula_and_valid = [
            ("", False),
            ("%d" % random.randint(-10000, 10000), True),
            ("%f" % (random.random() * 10000), True),
            ("x", True),
            # addition, subtraction, multiplication, division
            ("x + %d" % random.randint(-10000, 10000), True),
            ("x + %f" % (random.random() * 10000), True),
            ("x - %d" % random.randint(-10000, 10000), True),
            ("x - %f" % (random.random() * 10000), True),
            ("x * %d" % random.randint(-10000, 10000), True),
            ("x * %f" % (random.random() * 10000), True),
            ("x / %d" % random.randint(-10000, 10000), True),
            ("x / %f" % (random.random() * 10000), True),
            # duplicated symbol
            ("x ++ %d" % random.randint(-10000, 10000), False),
            ("x ++ %f" % (random.random() * 10000), False),
            ("x +- %d" % random.randint(-10000, 10000), False),
            ("x +- %f" % (random.random() * 10000), False),
            ("x +* %d" % random.randint(-10000, 10000), False),
            ("x +* %f" % (random.random() * 10000), False),
            ("x +/ %d" % random.randint(-10000, 10000), False),
            ("x +/ %f" % (random.random() * 10000), False),
            ("x -+ %d" % random.randint(-10000, 10000), False),
            ("x -+ %f" % (random.random() * 10000), False),
            ("x -- %d" % random.randint(-10000, 10000), False),
            ("x -- %f" % (random.random() * 10000), False),
            ("x -* %d" % random.randint(-10000, 10000), False),
            ("x -* %f" % (random.random() * 10000), False),
            ("x -/ %d" % random.randint(-10000, 10000), False),
            ("x -/ %f" % (random.random() * 10000), False),
            ("x *+ %d" % random.randint(-10000, 10000), False),
            ("x *+ %f" % (random.random() * 10000), False),
            ("x *- %d" % random.randint(-10000, 10000), False),
            ("x *- %f" % (random.random() * 10000), False),
            ("x ** %d" % random.randint(-10000, 10000), False),
            ("x ** %f" % (random.random() * 10000), False),
            ("x */ %d" % random.randint(-10000, 10000), False),
            ("x */ %f" % (random.random() * 10000), False),
            ("x /+ %d" % random.randint(-10000, 10000), False),
            ("x /+ %f" % (random.random() * 10000), False),
            ("x /- %d" % random.randint(-10000, 10000), False),
            ("x /- %f" % (random.random() * 10000), False),
            ("x /* %d" % random.randint(-10000, 10000), False),
            ("x /* %f" % (random.random() * 10000), False),
            ("x // %d" % random.randint(-10000, 10000), False),
            ("x // %f" % (random.random() * 10000), False),
            # functions
            ("%d^(%d)" % (random.randint(-10000, 10000), random.randint(-10000, 10000)), True),
            ("%f^(%f)" % ((random.random() * 10000), (random.random() * 10000)), True),
            ("%d^%d" % (random.randint(-10000, 10000), random.randint(-10000, 10000)), False),
            ("%f^%f" % ((random.random() * 10000), (random.random() * 10000)), False),
            ("%d^()" % random.randint(-10000, 10000), False),
            ("%f^()" % (random.random() * 10000), False),
            ("cos(%d)" % random.randint(-10000, 10000), True),
            ("cos(%f)" % (random.random() * 10000), True),
            ("cos()", False),
            ("cos%d" % random.randint(-10000, 10000), False),
            ("cos%f" % (random.random() * 10000), False),
            ("sin(%d)" % random.randint(-10000, 10000), True),
            ("sin(%f)" % (random.random() * 10000), True),
            ("sin%d" % random.randint(-10000, 10000), False),
            ("sin%f" % (random.random() * 10000), False),
            ("sin()", False),
            ("tan(%d)" % random.randint(-10000, 10000), True),
            ("tan(%f)" % (random.random() * 10000), True),
            ("tan%d" % random.randint(-10000, 10000), False),
            ("tan%f" % (random.random() * 10000), False),
            ("tan()", False)
        ]
        print("")
        for couple in formula_and_valid:
            print(couple)
            self.assertEqual(
                m_utils.is_formula_valid(couple[0]),
                couple[1]
            )

    def test_get_derivative(self):
        pass  # TODO


if __name__ == '__main__':
    unittest.main()
