class Uquvchi:
    name: str
    fam: str
    age: int
    def __init__(self, name, fam, age):
        self.name=name
        self.fam=fam
        self.age=age
    def __str__(self) -> str:
        return f"O'quvchining ismi: {self.name}\nFamiliyasi: {self.fam}\nYoshi: {self.age}\n Shu paytgacha ochilgan sinf soni: {self.soni}\n\n"

n=int(input("Siz nechta o'quvchi kiritmoqchisiz."))
uquvchilar = []
print("O'quvchi kiritish jarayoni boshlandi \n")

for x in range(n):
    ism=input("O'quvchining ismini kiriting: ")
    fam=input("O'quvchining familiyasini kiriting:")
    age=int(input("O'quvchining yoshini kiriting: "))
    newuquvchi=Uquvchi(ism, fam , age)
    uquvchilar.append(newuquvchi)

print("Siz kiritgan o'quvchilar ro'yxati")
for x in uquvchilar:
    print(x)