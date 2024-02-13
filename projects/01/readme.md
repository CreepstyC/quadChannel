# Desarrollo

## Nand
La compueta Nand está creada de manera nativa en las herramientas de nand2tetris, por lo cuál se usar para crear las siguientes compuertas progresivamente.

<p align="center">
<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Truth-table-NAND-gate-417x500.png" width="200">
</p>

## Not
Tomando la compuerta Nand como base, se observa que al tener el mismo valor en las entradas, la salida es el opuesto de este, p.ej, cuando a y b son 0, la salida de la Nand es 1 y viceversa. De esta forma y reduciendo la tabla de verdad se obtiene una equivalente a la compueta Not.

```verilog
CHIP Not {
    IN in;
    OUT out;

    PARTS:
    Nand(a=in, b=in, out=out);
}
```

<p align="center">
<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Truth-table-NOT-gate.png" width="250">
</p>

## And
Con la compuerta Nand nativa y la Not creada anteriormente se consigue llegar fácilmente a la compuerta And.

```verilog
CHIP And {
    IN a, b;
    OUT out;
    
    PARTS:
    Nand(a=a, b=b, out=nOut);
    Not(in=nOut, out=out);
}
```

<p align="center">
<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Truth-table-AND-gate-417x500.png" width="200">
</p>

## Or
Para llegar a la compuerta Or se puede implementar la ley de DeMorgan en la compuerta Nand, negando al mismo tiempo sus entradas.

```verilog
CHIP Or {
    IN a, b;
    OUT out;

    PARTS:
    Not(in=a, out=na);
    Not(in=b, out=nb);
    Nand(a=na, b=nb, out=out);
}
```
<p align="center">
<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Truth-table-OR-gate.png" width="200">
</p>

## Xor
Tomando como partida la tabla de verdad de la compuerta or exclusiva, se puede obtener su expresión booleana en términos de And, Or y Not.

Xor = A(¬B) + (¬A)B

<p align="center" text="center">
<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Truth-table-XOR-gate.png" width="200">
</p>

```
CHIP Xor {
    IN a, b;
    OUT out;

    PARTS:
    Not(in=a, out=na);
    Not(in=b, out=nb);
    And(a=na, b=b, out=and1);
    And(a=a, b=nb, out=and2);
    Or(a=and1, b=and2, out=out);
}
```

## Mux
La tabla de verdad de la compuerta Mux se puede reducir (en términos de And, Or y Not) de forma que esta sólo depende de la entrada sel. Cuándo 

Mux = (¬sel) a + sel b

<p align="center">
<img src="img/MuxGateTable.png" width="500">
</p>

```
CHIP Mux {
    IN a, b, sel;
    OUT out;

    PARTS:
    Not(in=sel, out=nsel);
    And(a=a, b=nsel, out=and1);
    And(a=b, b=sel, out=and2);
    Or(a=and1, b=and2, out=out);
}
```