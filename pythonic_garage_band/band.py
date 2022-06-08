class Musician ():
    def __init__(self,name,members ,play_solos ):
        self.name=name
        self.members=members
        self.play_solos=play_solos


class Band :

    def __init__(self, name,members):
        self.name = name
        self.members = members

    def __str__(self):
        return f'My name is {self.name} and I play {self.members}'

    def __repr__(self):
        return f'{type(self).__name__} instance. Name = {self.name}'

    def get_instrument(self):
        return f'{self.members}'



class Guitarist(Band):
    def __init__(self, name, members="guitar"):
        # self.name = name
        # self.members = members
        super().__init__(name, members)



class Drummer(Band):
    def __init__(self, name, members="drums"):

        super().__init__(name, members)


class Bassist(Band):
    def __init__(self, name, members="bass"):
        super().__init__(name, members)

a=Guitarist("Nirvana")
print(str(a))
print(repr(a))
print((a.get_instrument()))




