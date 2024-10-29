from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        #If the cell "A1" contains "1", the result of its evaluation is 1.
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1")
        self.assertEqual(spreadsheet.evaluate("A1"), "1")

    def test_evaluate_invalid_integer(self):
        #If the cell "A1" contains "1.5", the result of its evaluation is "#Error".
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        #If the cell "A1" contains "'Apple'", the result of its evaluation is "Apple".
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual(spreadsheet.evaluate("A1"), "Apple")

    def test_evaluate_invalid_string(self):
        #If the cell "A1" contains "'Apple", the result of its evaluation is "#Error".
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_simple_formula_string(self):
        #If the cell "A1" contains "='Apple'", the result of its evaluation is "Apple".
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple",spreadsheet.evaluate("A1"))

    def test_evaluate_equals_one(self):
        #If the cell "A1" contains "=1", the result of its evaluation is 1.
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1")
        self.assertEqual("1", spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_single_quote(self):
        #If the cell "A1" contains "='Apple", the result of its evaluation is "#Error".
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_simple_formula_with_reference(self):
        #If the cell "A1" contains "=B1" and "B1" contains "42", the result of the evaluation of "A1" is 42.
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "42")
        self.assertEqual(spreadsheet.evaluate("A1"), "42")

    def test_simple_formula_with_reference_error(self):
        #If the cell "A1" contains "=B1" and "B1" contains "42.5", the result of the evaluation of "A1" is "#Error".
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "42.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_simple_formula_with_circularity(self):
        #If the cell "A1" contains "=B1" and "B1" contains "=A1", the result of the evaluation of "A1" is "#Circular".
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_simple_formula_with_addition(self):
        #If the cell "A1" contains "=1+3", the result of its evaluation is 4.
        # THIS IS ADDITION THIS SHOULD BE SIMPLE
        #DO NOT CHANGE THE API OF THE METHODS
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3")
        self.assertEqual("4", spreadsheet.evaluate("A1"))
