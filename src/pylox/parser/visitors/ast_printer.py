from pylox.parser.expressions.binary import Binary
from pylox.parser.expressions.unary import Unary
from pylox.parser.expressions.literal import Literal
from pylox.parser.expressions.grouping import Grouping
from pylox.parser.expressions.expression import Expression

from pylox.parser.visitors.visitor import Visitor

class AST_Printer(Visitor):      
   def print(self, expression: Expression):
      return self.parenthesize(expression)

   def visit_binary(self, binary: Binary):
      return f'{binary.operator.lexeme} {binary.left.accept(self)} {binary.right.accept(self)}'

   def visit_unary(self, unary: Unary):
      return f'{unary.operator.lexeme} {unary.expression.accept(self)}'

   def visit_grouping(self, grouping: Grouping):
      return f'({grouping.expression.accept(self)})'

   def visit_literal(self, literal: Literal):
      return f'{literal.value}'

   def parenthesize(self, expression: Expression) -> str:
      return f'({expression.accept(self)})'