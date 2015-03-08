
from expr import Expr

class ConstExpr(Expr):
    def __init__(self, value):
        self.value = value
    
