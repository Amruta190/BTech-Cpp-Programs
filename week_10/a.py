class person:
    def _init_(self, name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def get_bmi(self):
        bmi=float(self.weight/((self.height*0.3048)**2))
        if bmi<18.5:
            return "Underweight"
        elif bmi>=18.5 and bmi<25:
            return "Healthy"
        else:
            return "Obese"

p= person("Hari", 25, 6, 30)
print(p.get_bmi())
p= person("Hari", 25, 6, 200)
print(p.get_bmi())
p= person("Hari", 25, 6, 75)
print(p.get_bmi())