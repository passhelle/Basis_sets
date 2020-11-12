# This module finds elements present in the input file


def parse_file(filename):
    full = []
    with open(filename, "r") as inp:
        for line in inp:
            full.append(line)
    return full


def get_geom_line_num(data):
    for i in range(len(data)):
        if data[i][0].isdigit():
            geom_line_number = i + 1
            return geom_line_number

def FindEl(filename):
    full = parse_file(filename)
    geom_line_number = get_geom_line_num(full)
    elements = set()
    full = full[geom_line_number::]
    for j in full:
        parts = j.split(" ")
        elements.add(int(parts[0]))

    elements = sorted(elements)
    elements = list(map(lambda item: str(item), elements))
    elements = ",".join(elements)
    return elements

