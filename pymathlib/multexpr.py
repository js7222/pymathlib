
from binaryop import INFIX, BinaryOp

MULTCHAR = '*'


class MultExpr(BinaryOp):
    def __init__(self, l_expr, r_expr):
        super(MultExpr, self).__init__(l_expr, r_expr, op_char=MULTCHAR, convention=INFIX)
