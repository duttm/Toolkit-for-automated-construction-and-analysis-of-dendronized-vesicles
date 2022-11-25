import numpy

def indices(moleculefile, indexing):

    f = open(moleculefile, "r")
    lines = f.readlines()
    required_indices = []
    for x in lines:
        if x.split('\t')[1].strip() == indexing:
            required_indices.append(x.split('\t')[0].strip())
    f.close()

    return required_indices
