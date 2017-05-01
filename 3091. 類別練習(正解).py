na = input()
ge = input()
g1 = eval(input())
g2 = eval(input())
g3 = eval(input())
lst = [g1,g2,g3]

class student:
    def __init__(self,name,gender,lst):

        self.name = na
        self.gender = ge
        self.grades = lst
    def avg(self):
        return sum(self.grades)/len(self.grades)
    def add (self,score):
        self.grades.append(score)
    def fcount(self):
        fct = 0
        for i in range(len(self.grades)):
            if self.grades[i] < 60:
                fct += 1
        return fct                           #這裡return不然你下面又print一次，會變成print兩次


x = student(na,ge)
print(x.name)
print(x.avg())
print(x.fcount())
