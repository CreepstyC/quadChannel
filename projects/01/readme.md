# Desarrollo

## Nand
La compueta Nand está creada de manera nativa en las herramientas de nand2tetris, por lo cuál se usar para crear las siguientes compuertas progresivamente.

<p align="center">
<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Truth-table-NAND-gate-417x500.png" width="150">
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
<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Truth-table-NOT-gate.png" width="150">
</p>