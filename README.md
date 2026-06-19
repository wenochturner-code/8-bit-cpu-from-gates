# 8-bit CPU — built from logic gates

An 8-bit CPU design based on reading *Code* by Charles Petzold. Everything is built from the logic gates up, initially using AND, OR, NAND, NOT, NOR, and XOR. It contains 256 x 8 RAM, registers, an ALU built from adders, and a control unit.

---

As a Mechanical Engineering and Math student I have learned a decent bit of code, yet I never knew what was actually happening under the hood. So I took it upon myself to figure it out. This summer I decided to read *Code*, and while reading I figured the best way to solidify it in my memory was to make a project out of it.

---

## Design Choices

While making this CPU simulator I tried to stay as true to Petzold's build in the book as I could.

I started with the logic gates. From the logic gates I made the half-adder. Two half-adders and another logic gate gave me a full-adder. Eight full-adders chained together gave me an eight-bit adder. Then from the eight-bit adder and a little more logic I built the ALU.

Up to this point I had followed the book almost perfectly, but when I reached the next section I made a design choice to step away from pure gates to simulate the rest of the CPU. This is because flip-flops in hardware act differently than they do in software. In order to preserve a state I opted for classes.

So I finished the design keeping that in mind. RAM, registers, flags, and the control unit were all created using classes.

One thing to note: this is a logical simulation of how a CPU computes, not a timing-accurate one. There is no clock signal — it focuses on the logic, not the electrical timing.

## Instruction Set

Each instruction is two bytes in memory: an **opcode** and an **operand** (usually a memory address). The opcode is held in the low 3 bits of the byte and is decoded by gate logic.

| Opcode | Name | Effect |
| --- | --- | --- |
| 1 | `LOAD addr` | A ← value stored at `addr` |
| 2 | `STORE addr` | value at `addr` ← A |
| 3 | `ADD addr` | A ← A + value at `addr` |
| 4 | `SUB addr` | A ← A − value at `addr` |
| 5 | `JUMP addr` | jump to `addr` |
| 6 | `JZ addr` | jump to `addr` if the last result was zero |
| 7 | `HALT` | stop execution |

`A` is the single working register (the accumulator). `JZ` (jump-if-zero) reads the zero flag set by the previous arithmetic operation, which is what makes loops and decisions possible.

## Programs

In `main.py` there are already two programs coded — addition and multiplication. You can run them as-is or alter them to change the outputs. Keep in mind the program has to be properly coded or it won't run. The multiply example works by adding a number to itself in a loop, using `SUB` to count down and `JZ` to end the loop once the counter hits zero.

## Running it

```
python main.py
```

---

*Built by working through Charles Petzold's* Code *(2nd edition), from the logic gates up.*