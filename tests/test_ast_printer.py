import unittest

from pylox.parser.expressions.binary import Binary
from pylox.parser.expressions.literal import Literal
from pylox.lexer.token import Token
from pylox.lexer.token_types import Token_Type
from pylox.parser.expressions.unary import Unary
from pylox.parser.expressions.grouping import Grouping
from pylox.parser.expressions.literal import Literal

from pylox.parser.visitors.ast_printer import AST_Printer


class Test_AST_Printer(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      cls.printer = AST_Printer()

   def test_binary_printing(self):
      expression = Binary(Literal('3'), Token(Token_Type.PLUS, '+', 1, None), Literal('2'))
      output = self.printer.print(expression)
      expected_output = '(+ 3 2)'
      self.assertEquals(output, expected_output)

   def test_unary_printing(self):
      expression = Unary(Token(Token_Type.MINUS, '-', 1, None), Literal('2'))
      output = self.printer.print(expression)
      expected_output = '(- 2)'
      self.assertEquals(output, expected_output)

   def test_literal_printing(self):
      expression =  Literal('abcd')
      output = self.printer.print(expression)
      expected_output = '(abcd)'
      self.assertEquals(output, expected_output)

   def test_grouping_printing(self):
      expression =  Grouping(Literal('abcd'))
      output = self.printer.print(expression)
      expected_output = '((abcd))'
      self.assertEquals(output, expected_output)

def main():
   unittest.main()

if __name__ == '__main__':
   main()