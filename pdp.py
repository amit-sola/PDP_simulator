import re

pdp_memory = []

temp_memory = []

Reg_R0 = 0
Reg_R1 = 0
Reg_R2 = 0
Reg_R3 = 0
Reg_R4 = 0
Reg_R5 = 0

Reg_R6_SP = 0
Reg_R7_PC = 0

PC_val = 0
load_ptr = 0

PSW_N = 0
PSW_Z = 0
PSW_V = 0
PSW_C = 0


for memory_iter in range(0,64*1024,2):
    temp_memory = temp_memory + [[memory_iter,0]]
    pdp_memory = pdp_memory + temp_memory
    temp_memory.clear()




#print(pdp_memory)



''' #########  ######### '''

with open('fib.ascii.txt','r') as file_in:

    data = file_in.readlines()

    for line in data:
            if (line[0] == '*'):
                str_addr_temp = str(int(line[1:],8))
                print("Starting address temp is ", str_addr_temp)
                str_addr = int(str_addr_temp)
                print("Starting address is ",line[1:])
                print("Starting address is in deci ",str_addr)
                print("Starting address is binary",bin(str_addr)[-16:])
                PC_val = str_addr

            elif (line[0] == '-'):
                print("Value to be loaded at the curent load address")
                print("Value getting loaded at the current address =",line[1:] )
                pdp_memory_temp = str(int(line[1:], 8))
                print("pdp memory temp is ", pdp_memory_temp)
                pdp_memory_val = int(pdp_memory_temp)
                print("pdp_memory_val is ", pdp_memory_val)
                pdp_memory[load_ptr][1] = pdp_memory_val
                print("pdp_memory is ", pdp_memory[load_ptr][1])
                print("load ptr is ", load_ptr)
                load_ptr = load_ptr + 2

            elif (line[0] == '@'):
                print("Change to the load address")
                print("New load address = ",line[1:])
                load_ptr_temp = str(int(line[1:], 8))
                print("load ptr temp is ", load_ptr_temp)
                load_ptr = int(load_ptr_temp)
                print("load ptr is ", load_ptr)

''' #########  ######### '''


print(pdp_memory)





