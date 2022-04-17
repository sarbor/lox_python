from abc import ABC, abstractmethod
from pylox.parser.visitors.visitor import Visitor

class Expression(ABC):
   @abstractmethod
   def accept(self, v: Visitor):
      pass
