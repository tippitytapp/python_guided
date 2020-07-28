'''
CPU
    Executing Instructions
    Gets them out of RAM
    Registers (Like variables)
        Fixed names -- R0 - R7
        Fixed number of them -- 8 of them
        Fixed size -- 8 bits

Memory (RAM)
    A big array of bytes
    Each memory slot has an index, and a value stored at that index
    That index in memory is AKA:
        pointer
        location
        address
'''
# 0b00000000 == 0
# 0b11111111 == 255
import sys

memory = [0] * 256
address = 0
with open(sys.argv[1]) as f:
    for line in f:
        try:
            line = line.strip()
            line = line.split("#", 1)[0]
            line = int(line, 10) # make sure to specify the base
            memory[address] = line
            address += 1
        except ValueError:
            pass
# sys.exit(0)

register = [0] * 8
pc = 0 # program counter, index into memory of the current instruction
        # AKA a pointer to the current intruction
running = True
while running:
    inst = memory[pc]
    if inst == 1:
        print("Marc")
        pc += 1
    elif inst == 2:
        running = False
    elif inst == 3:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        pc += 3
    elif inst == 4:
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 2
    else:
        print(f"Unknown instruction {inst}")
        running = False