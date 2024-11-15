class Oquvchi:
    name: str
    fam: str
    age: int
    manzil: str

    def __init__(self, name:str, fam:str, age:int, manzil:str):
        self.name=name
        self.fam=fam
        self.age=age
        self.manzil=manzil
    def __str__(self) -> str:
        return self.name

rasul=Oquvchi("Rasul", "Baxtiyorov", 16, "O'zbekiston")
# rasul.name="Rasul"
# rasul.fam="Baxtiyorov"
# rasul.age=16
# rasul.manzil="O'zbekiston OFY"

bexruz=Oquvchi("Bexruz", "Erimbetov", 16, "MFY and OFY")
# bexruz.name="Bexruz"
# bexruz.fam="Erimbetov"
# bexruz.age=16
# bexruz.manzil="MFY and OFY"

print(rasul.name,bexruz.name)
yunus = Oquvchi("Yunus", "Jumanazarov", 17, "Istiqlol")
mohinur = Oquvchi("Mohinur", "Aitboyeva", 15, "Mustaqillik MFY")
print(yunus.fam, mohinur.fam)
print(yunus)