# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,2,1,2,1,2,3,2,19,8,2,1,3,1,3,1,3,3,3,24,8,3,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,32,8,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,1,2,1,0,3,4,32,
        0,10,1,0,0,0,2,13,1,0,0,0,4,15,1,0,0,0,6,20,1,0,0,0,8,31,1,0,0,0,
        10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,3,4,2,0,14,3,1,0,
        0,0,15,18,3,6,3,0,16,17,7,0,0,0,17,19,3,4,2,0,18,16,1,0,0,0,18,19,
        1,0,0,0,19,5,1,0,0,0,20,23,3,8,4,0,21,22,7,1,0,0,22,24,3,6,3,0,23,
        21,1,0,0,0,23,24,1,0,0,0,24,7,1,0,0,0,25,32,5,7,0,0,26,32,5,8,0,
        0,27,28,5,5,0,0,28,29,3,2,1,0,29,30,5,6,0,0,30,32,1,0,0,0,31,25,
        1,0,0,0,31,26,1,0,0,0,31,27,1,0,0,0,32,9,1,0,0,0,3,18,23,31
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_addExpr = 2
    RULE_mulExpr = 3
    RULE_atom = 4

    ruleNames =  [ "prog", "expr", "addExpr", "mulExpr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    NUM=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr()
            self.state = 11
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self):
            return self.getTypedRuleContext(ExprParser.AddExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.addExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_addExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddSubRightContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AddExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(ExprParser.MulExprContext,0)

        def addExpr(self):
            return self.getTypedRuleContext(ExprParser.AddExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubRight" ):
                listener.enterAddSubRight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubRight" ):
                listener.exitAddSubRight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubRight" ):
                return visitor.visitAddSubRight(self)
            else:
                return visitor.visitChildren(self)



    def addExpr(self):

        localctx = ExprParser.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.AddSubRightContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.mulExpr()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 16
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 17
                self.addExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_mulExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulDivRightContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.MulExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)

        def mulExpr(self):
            return self.getTypedRuleContext(ExprParser.MulExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivRight" ):
                listener.enterMulDivRight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivRight" ):
                listener.exitMulDivRight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivRight" ):
                return visitor.visitMulDivRight(self)
            else:
                return visitor.visitChildren(self)



    def mulExpr(self):

        localctx = ExprParser.MulExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.MulDivRightContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.atom()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3 or _la==4:
                self.state = 21
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 22
                self.mulExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = ExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ExprParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(ExprParser.ID)
                pass
            elif token in [8]:
                localctx = ExprParser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(ExprParser.NUM)
                pass
            elif token in [5]:
                localctx = ExprParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(ExprParser.T__4)
                self.state = 28
                self.expr()
                self.state = 29
                self.match(ExprParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





