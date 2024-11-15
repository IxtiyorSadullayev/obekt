class Telefon:
    model:str
    created_date:str

    def __init__(self, telefon_modeli:str, created_date:str):
        self.model=telefon_modeli
        self.created_date=created_date
    
    def __str__(self):
        return self.model  + " " + self.created_date

ayfon=Telefon("13 Pro", "01-01-2018")
samsung=Telefon("S24 ", "01-01-2024")
print(ayfon, samsung)
