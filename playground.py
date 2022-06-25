class PartyAnimal:
    x=0

    def party(self) :
        self.x = self.x + 1
        print("so far", self.x)
        print(self)

an =PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
print(self)
