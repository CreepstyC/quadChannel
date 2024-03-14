# Desarrollo (Práctica 3)

## Proyecto 05

### Memory

Permite la lectura de las entradas proporcionadas por el usuario y la generación de salidas correspondientes, mediante el manejo del espacio de memoria. 

```
CHIP Memory {
    IN in[16], load, address[15];
    OUT out[16];

    PARTS:
    DMux4Way(in=load, sel=address[13..14], a=loadRam1, b=loadRam2, c=loadScreen, d=loadKeyBoard);

    Or(a=loadRam1, b=loadRam2, out=loadRam);
    RAM16K(in=in, load=loadRam, address=address[0..13], out=outRam);
    Screen(in=in, load=loadScreen, address=address[0..12], out=outScreen);
    Keyboard(out=outKeyBoard);
    Mux4Way16(a=outRam, b=outRam, c=outScreen, d=outKeyBoard, sel=address[13..14], out=out);
}
```
### CPU
Se implementa el diseño de un procesador simple con entradas para datos de memoria RAM, instrucciones y señales de reinicio, y salidas para datos hacia la RAM, señales de escritura en la RAM, dirección en la memoria de datos y la próxima instrucción a ejecutar. Luego, se definen componentes clave del procesador: un registro A y un registro D, una ALU para realizar operaciones aritméticas y lógicas, y un contador de programa (PC). Además, se controla el flujo del programa basado en las instrucciones recibidas, determinando operaciones de carga, ejecución y escritura en la memoria RAM.

```
CHIP CPU {

    IN  inM[16],         // M value input  (M = contents of RAM[A])
        instruction[16], // Instruction for execution
        reset;           // Signals whether to restart the current
                         // program (reset==1) or continue executing
                         // the current program (reset==0).

    OUT outM[16],        // M value output
        writeM,          // Write to M? 
        addressM[15],    // Address in data memory (of M)
        pc[15];          // Address of next instruction

    PARTS:
     // A Register
    Not(in=instruction[15], out=a-command);
    Mux16(a=alu-output, b[15]=false, b[0..14]=instruction[0..14], sel=a-command, out=a-register-input);
    Or(a=a-command, b=instruction[5], out=a-register-load);
    ARegister(in=a-register-input, load=a-register-load, out=a-register-output, out[0..14]=addressM);
    
    // D Register
    And(a=instruction[4], b=instruction[15], out=load-d-register);
    DRegister(in=alu-output, load=load-d-register, out=alu-x-input);

    // ALU
    Mux16(a=a-register-output, b=inM, sel=instruction[12], out=alu-y-input);
    ALU(x=alu-x-input, zx=instruction[11], nx=instruction[10], y=alu-y-input, zy=instruction[9], ny=instruction[8], f=instruction[7], no=instruction[6], out=alu-output, out=outM);

    // PC
    PCController(data=alu-output, jmp=instruction[0..2], type=instruction[15], inc=inc-pc, load=load-pc);
    PC(in=a-register-output, load=load-pc, inc=inc-pc, reset=reset, out[0..14]=pc);

    // writeM
    And(a=instruction[3], b=instruction[15], out=writeM);
}

```
## COMPUTER
Para llevar a cabo la construcción de este chip, se implementa una ROM de 32 KB (ROM32K), una CPU y una memoria de datos. La ROM32K lee instrucciones del programa basadas en la dirección del contador de programa (PC), alimentando la instrucción a la CPU. La CPU, a su vez, recibe instrucciones del programa y datos de la memoria de datos, generando datos para escribir en la memoria de datos, señales de escritura, direcciones de memoria y la próxima dirección de instrucción. Finalmente, la memoria de datos recibe datos para escribir, señales de escritura, y direcciones de memoria, devolviendo los datos solicitados para ser leídos por la CPU.

```
CHIP Computer {
    IN reset;

    PARTS:

    ROM32K(address=pc-output, out=program-memory-output);
    CPU(inM=data-memory-output, instruction=program-memory-output, reset=reset, outM=data-memory-input, writeM=write-data-memory, addressM=data-memory-address, pc=pc-output);
    Memory(in=data-memory-input, load=write-data-memory, address=data-memory-address, out=data-memory-output);
}

```


## Preguntas adicionales

1. **¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?**

    Principalmente, el lenguaje de máquina puede ser interpretado por la CPU y la computadora para realizar las instrucciones que aunque se puedan dar en lenguajes de alto nivel, terminan traduciéndose a este. De esta forma se puede tener una comunicación entre el hardware y la computadora que permite trabajar correctamente.

2. **¿Qué diferencia ven entre arquitectura computacional, arquitectura de software y arquitectura del sistema? Justifique su respuesta.**

    La arquitectura computacional se centra en el nivel más bajo de la computadora, conteniendo la estructura física (CPU, memoria, etc). Al pasar a la arquitectura de software, se estudia la estructura lógica y cómo se relacionan los módulos, componentes y subsistemas. Finalmente, la arquitectura del sistemas cubre las dos anteriores, de manera que considera cómo los componentes físicos y lógicos interactúan entre sí.

## Equipo

- [@creepstyC](https://github.com/creepstyC)
- [@DieDev9](https://github.com/DieDev9)
- [@andr3sit011](https://github.com/%20andr3sit011e)
- [@reinaldocardenas23](https://github.com/reinaldocardenas23)

## Bibliografía
[Lenguaje máquina](https://www.euston96.com/lenguaje-maquina/)

[Apéndice 2: Guía HDL](https://drive.google.com/file/d/1dPj4XNby9iuAs-47U9k3xtYy9hJ-ET0T/view?usp=sharing)

[Lectura 4 (Machine Language)](https://drive.google.com/file/d/1HxjPmIZkFHl-BVW3qoz8eD9dqEuEyuBI/view)

[Lectura 5 (Computer arquitecture)](https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf)
