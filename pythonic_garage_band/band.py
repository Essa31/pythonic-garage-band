




class Musician ():

    def __init__(self, name,member):
        self.name = name
        self.member = member

    def __str__(self):
        return f'My name is {self.name} and I play {self.member}'

    def __repr__(self):
        return f'{type(self).__name__} instance. Name = {self.name}'


    def get_instrument(self):
        return f'{self.member}'


    def play_solo(self):
            if  self.member == "guitar":
                return "face melting guitar solo"
            elif   self.member== "drums":
                return "rattle boom crash"
            elif self.member == "bass":
                return "bom bom buh bom"



class Band (Musician):
    instances = []
    def __init__(self,name,members=[]):
        self.name=name

        self.members=members
        self.instances.append(self)



    # def __str__(self):
    #     return self.name
    #
    # def __repr__(self):
    #     return self.name


      



    def play_solos(self):
        output=[]
        for member in self.members:
            output.append(member.play_solo())
        return output
    @classmethod
    def to_list(cls):
        output = []
        for i in cls.instances:
            output.append(i)
        return output

        return











class Guitarist(Musician):
    def __init__(self, name, member="guitar"):
        # self.name = name
        # self.members = members
        super().__init__(name, member)



class Drummer(Musician):
    def __init__(self, name, member="drums"):

        super().__init__(name, member)


class Bassist(Musician):
    def __init__(self, name, member="bass"):
        super().__init__(name, member)

# a=Bassist("Nirvana")
# print(str(a))
# print(repr(a))
# print((a.get_instrument()))
# print((a.play_solo()))
b=Band("Nirvana",[Guitarist("Kurt Cobain"),Bassist("Dave Grohl"),Drummer("Kurt Cobain")])
print(b.play_solos())
