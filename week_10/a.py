class person(object):
    def __init__(self, name_5B9,age_5B9,height_5B9,weight_5B9):
        self.name_5B9=name_5B9
        self.age_5B9=age_5B9
        self.height_5B9=height_5B9
        self.weight_5B9=weight_5B9
    def get_bmi(self):
        bmi=float(self.weight_5B9/((self.height_5B9*0.3048)**2))
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