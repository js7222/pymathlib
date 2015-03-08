
from expr import Expr

PREFIX = 0
INFIX = 1

class BinaryOp(Expr):
    def __init__(self, l_expr, r_expr, op_char, convention):
        self.l_expr = l_expr
        self.r_expr = r_expr
        self.op_char = op_char
        self.convention = convention
