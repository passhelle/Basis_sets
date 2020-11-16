from Find_Elements import FindEl
from Make_Link import make_link
import requests


def copy_file(file_in, file_out):
    with open(file_in) as f:
        with open(file_out, "w") as f1:
            for line in f:
                f1.write(line)


def clean_file(filename):
    with open(filename) as f:
        clean_list = []
        for line in f:
            clean_list.append(line)
    last_index = len(clean_list) - 1
    for i in range(len(clean_list) - 1, 0, -1):
        if clean_list[i] != "\n":
            last_index = i
            break
    clean_list[last_index] = clean_list[last_index].strip()
    clean_list = clean_list[0:last_index +1]
    with open(filename, "w") as f1:
        for line in clean_list:
            f1.write(line)


def main(name, bas, soft):
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
    clean_file(name_out)

    for_out = "\n".join(text_list)
    with open(name_out, "a") as ouf:
        ouf.write(for_out)

