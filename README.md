# precedencia-y-asociatividad
---
```markdown
# Intérprete de expresiones aritméticas con ANTLR4

Este proyecto implementa un **analizador sintáctico e intérprete** para expresiones aritméticas usando **ANTLR4** y **Python 3**.  

Se desarrollaron **dos versiones de la gramática**:
1. **Asociatividad por izquierda (IZQ)** → lo normal en matemáticas.
2. **Asociatividad por derecha (DER)** → versión alternativa para observar diferencias.

---

## 📂 Estructura del proyecto
---




```

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
````

2. Crear entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

Ejecuta el programa en la carpeta que quieras (IZQ o DER):

```bash
cd IZQ
python3 main.py
```

o

```bash
cd DER
python3 main.py
```

El programa pedirá una expresión por consola, ejemplo:

```
Ingrese una expresión (o 'exit' para salir): 2+3*4
Resultado: 14
```

Para salir escribe:

```
exit
```

---

## Gramáticas

### 1. Asociatividad por izquierda (IZQ)

```antlr
grammar Expr;

prog: expr EOF;

expr
    : expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # AddSub
    | NUM                      # Num
    | '(' expr ')'             # Parens
    ;

NUM: [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
```

### 2. Asociatividad por derecha (DER)

```antlr
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
    : NUM                               # Num
    | '(' expr ')'                      # Parens
    ;

NUM: [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
```

---

## Ejemplos de prueba

A continuación los ejemplos probados y sus resultados en **IZQ** (normal) y **DER** (asociatividad derecha):

| Expresión     | IZQ (normal) | DER (derecha) |
| ------------- | ------------ | ------------- |
| `2+3*4`       | 14           | 14 ✅          |
| `2+3-4`       | 1            | 1             |
| `2+3*(4-5)`   | -1           | -1            |
| `10-5-2`      | 3            | **7** 🔄      |
| `20/5/2`      | 2            | **8.0** 🔄    |
| `(2+3)*(4+5)` | 45           | 45            |
| `8/(4/2)`     | 4            | **1.0** 🔄    |
| `7-(3-2)`     | 6            | 2             |

Como se observa, **la precedencia se mantiene igual** (\*/ tienen más fuerza que +-),
pero la **asociatividad cambia** en operaciones con `-` y `/`.

---

## Autor

* **Nombre:** Paula Alejandra
* **Curso:** Lenguajes de Programación
* **Tema:** Precedencia y asociatividad en gramáticas ANTLR4

```
---


