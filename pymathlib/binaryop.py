
class BinaryOp(Expr):
    def __init__(l_expr, r_expr, op_char):
        self.l_expr = l_expr
        self.r_expr = r_expr
        self.op_char = op_char
