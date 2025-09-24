from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ParseTreeVisitor

class EvalVisitor(ParseTreeVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        return self.visit(ctx.addExpr())

    def visitAddSubRight(self, ctx):
        left = self.visit(ctx.mulExpr())
        if ctx.addExpr():
            right = self.visit(ctx.addExpr())
            if ctx.op.text == '+':
                return left + right
            else:
                return left - right
        return left

    def visitMulDivRight(self, ctx):
        left = self.visit(ctx.atom())
        if ctx.mulExpr():
            right = self.visit(ctx.mulExpr())
            if ctx.op.text == '*':
                return left * right
            else:
                return left / right
        return left

    def visitNum(self, ctx):
        return int(ctx.getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitId(self, ctx):
        return ctx.getText()

def main():
    while True:
        expr = input("Ingrese una expresión (o 'exit' para salir): ")
        if expr == "exit":
            break
        input_stream = InputStream(expr)
        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = EvalVisitor()
        result = visitor.visit(tree)
        print("Resultado:", result)


main()

