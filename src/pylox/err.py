from dataclasses import dataclass
import sys

@dataclass
class Lox_Err:
   msg: str
   line_num: int

   def report_error(self):
      print(f'line: {self.line_num} {self.msg}', file=sys.stderr)