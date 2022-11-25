import numpy

def index(moleculefile, indexing):

    f = open(moleculefile, "r")
    lines = f.readlines()
    args = []
    for x in lines:
        if x.split('\t')[1].strip() == indexing:
            required_index = x.split('\t')[0].strip()
            break
    f.close()

    return required_index
