#!/usr/bin/env python

from multexpr import  MultExpr
from constexpr import ConstExpr

def main():
    mult = MultExpr(l_expr= ConstExpr(1), r_expr=ConstExpr(2))

if __name__ == '__main__':
    main()

