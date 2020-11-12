def make_link(elements, basis = "def2-tzvp", software = "gaussian94"): # elements as string sep = ","
    link = "https://www.basissetexchange.org/api/basis/{}/format/{}/?version=1&elements={}"
    link = link.format(basis, software, elements)
    return link
