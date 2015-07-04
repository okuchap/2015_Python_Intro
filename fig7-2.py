def getRatios(vect1, vect2):
    ratios = []

    if len(vect1)!=len(vect2):
        raise ValueError('bad arguments')

    for index in range(len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]

        if (type(vect1Elem) not in (int, float)) or (type(vect2Elem) not in (int, float)):
            raise ValueError('bad arguments')
        if vect2Elem == 0.0:
            ratios.append(float('nan')) #nan = not a number
        else:
            ratios.append(vect1Elem/vect2Elem)
    
    return ratios

v0 = [2,2,2]
v1 = [1,2,3]
v2 = [1,0,0]
v3 = [1,2,2,3]

try:
    print getRatios(v0, v1)
    print getRatios(v1, v2)
    print getRatios(v3, v1)
except ValueError, msg:
    print msg