class Tortburchak:
    a:int
    b:int

    def __init__(self, a:int,b:int):
        self.a=a
        self.b=b
    
    def peremetr(self):
        print((self.a+self.b)*2)
    def yuzasi(self):
        print(self.a*self.b)
    
    def __str__(self) -> str:
        return f"To'rtburchak a tomoni {self.a} b tomoni {self.b}"

birinchi = Tortburchak(3,4)
print(birinchi)
birinchi.peremetr()