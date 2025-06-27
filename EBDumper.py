#Import Modules
import os
import sys
import time

#Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

if sys.argv[1] == "--help":
	print(BLUE, "Usage : ./EBDumper <elf64-bin> <Function-Object> <Arch-amd64,intel,etc...>")
	print(RED, "NOTE : intel Arch Is Recommended For Beginners")
	exit()
else:
	print(YELLOW, "Hello In ELF64 Binary Dumper")
	

#Varibles
program = sys.argv[1] # program = 1 argv Prameter
func_obj = sys.argv[2] # func_obj = 2 argv Prameter
format_sourcecode = sys.argv[3] # format_sourcecode = 3 argv prameter

command = "readelf --symbols " + program + " | grep " + func_obj #Command Format For Get Information And Find Functions_Objects
source_code = "objdump -M " + format_sourcecode +" -D " + program + " | grep -A20 " + func_obj #Command Format For Get Assembly(x86_x64) Source Code Of Function

#Execution And Outputs
print(GREEN)
print(GREEN, "Information & Function " + func_obj + " : ")
print(BLUE, os.system(command)) #Execute "command" Command
print(BLUE, "The Source-Code Will Show after 10 Seconds from now")
time.sleep(10)

print(" ")
print("=============================================")
print(" ")

print("Assembly(x86_x64) " + func_obj + " Function Source-Code In intel format : ")
time.sleep(0.5)
print(YELLOW)
print(os.system(source_code))
