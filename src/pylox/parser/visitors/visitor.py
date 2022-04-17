from abc import ABC, abstractmethod

class Visitor(ABC):
   @abstractmethod
   def visit_binary(self, binary):
      pass

   @abstractmethod
   def visit_unary(self, unary):
      pass

   @abstractmethod
   def visit_grouping(self, grouping):
      pass

   @abstractmethod
   def visit_literal(self, literal):
      pass