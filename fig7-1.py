def getRatios(vect1, vect2):
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('getRatios called with bad arguments')
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