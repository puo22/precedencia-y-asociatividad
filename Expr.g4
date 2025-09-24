grammar Expr;

prog: expr EOF;

expr
    : addExpr
    ;

addExpr
    : mulExpr (op=('+'|'-') addExpr)?   # AddSubRight
    ;

mulExpr
    : atom (op=('*'|'/') mulExpr)?      # MulDivRight
    ;

atom
    : ID                                # Id
    | NUM                               # Num
    | '(' expr ')'                      # Parens
    ;

ID : [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
