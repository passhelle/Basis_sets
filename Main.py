from Find_Elements import FindEl
from Make_Link import make_link
import requests


def copy_file(file_in, file_out):
    with open(file_in) as f:
        with open(file_out, "w") as f1:
            for line in f:
                f1.write(line)


name = input("type in filename")
bas = input("type in basis set") # issue with default parameters
soft = input("type in software name") # issue with default parameters

"""
name = "test1.gjf"
bas = ""
soft = ""
"""

if bas == "":
    bas = "def2-tzvp"
if soft == "":
    soft = "gaussian94"
element_list = FindEl(name)
link = make_link(element_list, bas, soft)
r = requests.get(link)
text = r.text
text_list = []
text_list = text.split("\n")
text_list = text_list[10::]

parts = name.split(".")
name_out = parts[0]  + "_mod." + parts[1]
copy_file(name, name_out)

for_out = "\n".join(text_list)
with open(name_out, "a") as ouf:
    ouf.write(for_out)
