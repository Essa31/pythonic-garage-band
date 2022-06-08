# class Band ():
#     def __init__(self,name,members ,play_solos ):
#         self.name=name
#         self.members=members
#         self.play_solos=play_solos


class Musician :
    def __init__(self, name,members):
        self.name = name
        self.members = members

    def __str__(self):
        return f'My name is {self.name} and I play {self.members}'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'



class Guitarist(Musician):
    def __init__(self, name,members):
        self.name = name
        self.members = members



    # def __str__ (self):
    #     return f'My name is {self.name} and I play guitar'

    def __repr__(self):

        return  f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return "guitar"

class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def __str__ (self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return "drums"

class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return "bass"
# a=Guitarist("Nirvana","drums")
# print(str(a))
# print(a.__class__)
# print(a)
def sum_matrix(arr):
    cont=0
    rslt=[]


    for i in range(len(arr)):
        for l in arr[i]:
            cont=cont+l
        rslt=rslt+[cont]
        cont=0
    return rslt

print(sum_matrix([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]))



