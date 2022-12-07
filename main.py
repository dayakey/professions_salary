class Teacher:
    def __init__(self, hour):
        self.hour = hour

    def salary(self):
        return (self.hour * 60) * 30

    def __str__(self):
        return f"teacher"


class Doctor:
    def __init__(self, hours, clients):
        self.hours = hours
        self.clients = clients

    def salary(self):
        return (((self.clients * 1200) * 0.8) + self.hours * 1000) * 30

    def __str__(self):
        return f"doctor"


class Consultant:
    def __init__(self, customer):
        self.customer = customer

    def salary(self):
        return ((self.customer * 2000) * 0.4) * 30

    def __str__(self):
        return f"consultant"


teacher = Teacher(6)
doctor = Doctor(8, 10)
consultant = Consultant(10)

professions = [teacher, doctor, consultant]

for profession in professions:
    print(profession, 'salary is', profession.salary())