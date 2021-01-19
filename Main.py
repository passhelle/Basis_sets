import Parser
import sys
name = sys.argv[1]
bas = sys.argv[2]
if len(sys.argv) == 4:
    soft = sys.argv[3]
else:
    soft = "gaussian94"

#name = input("type in filename")
#bas = input("type in basis set") # issue with default parameters
#soft = input("type in software name") # issue with default parameters


Parser.main(name, bas, soft)