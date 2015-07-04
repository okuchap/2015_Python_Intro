import datetime

class Person(object):
    
    def __init__(self, name):
        self.name = name
        
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank +1:]
        except:
            self.lastName = name
        self.birthday = None
    
    def getName(self):
        return self.name
    
    def getLastname(self):
        return self.lastName
    
    def setBirthday(self, birthdate):
        self.birthday = birthdate
    
    def getAge(self):
        
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

class MITPerson(Person):
    
    nextIdNum = 0
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    def isStudent(self):
        return isinstance(self, Student)
    
    def __lt__(self, other):
        return self.idNum < other.idNum
        
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(Student):
    pass

class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student is not in maping')
    
    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('student not in mapping')
    
    def getStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

def gradeReport(course):
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n' + str(s) + '\'smean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n' + str(s) + ' has no grades'
    
    return report

ug1 = UG('Taro Tanaka', 2014)
ug2 = UG('Hanako Yamada', 2015)
ug3 = UG('Ichiro Suzuki', 2003)
g1 = Grad('Billy Buvkner')
g2 = Grad('Bucky F. Dent')

sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
#sixHundred.addStudent(ug3)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)

for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)

sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)

print gradeReport(sixHundred)



'''
p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')
p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)

print p1 < p2
print p3 < p2
print p4 < p1
print p4.__lt__(p1)
print p5, 'is a graduate student is', type(p5) == Grad
print p5, 'is an undergraduate student is', type(p5) == UG
print p5, 'is a student is', p5.isStudent()
print p6, 'is a student is', p6.isStudent()
print p3, 'is a student is', p3.isStudent()
'''

