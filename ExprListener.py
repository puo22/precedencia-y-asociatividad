# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSubRight.
    def enterAddSubRight(self, ctx:ExprParser.AddSubRightContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSubRight.
    def exitAddSubRight(self, ctx:ExprParser.AddSubRightContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDivRight.
    def enterMulDivRight(self, ctx:ExprParser.MulDivRightContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDivRight.
    def exitMulDivRight(self, ctx:ExprParser.MulDivRightContext):
        pass


    # Enter a parse tree produced by ExprParser#Id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#Id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#Num.
    def enterNum(self, ctx:ExprParser.NumContext):
        pass

    # Exit a parse tree produced by ExprParser#Num.
    def exitNum(self, ctx:ExprParser.NumContext):
        pass


    # Enter a parse tree produced by ExprParser#Parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#Parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass



del ExprParser