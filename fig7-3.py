def getGrades(fname):
    try:
        gradesFile = open(fname, 'r')
    except IOError:
        raise ValueError('getGrades could not open ' + fname)
    
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')

    return grades


try:
    grades = getGrades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print 'Median grade is', median
except ValueError, errorMsg:
    print 'Whoops.', errorMsg