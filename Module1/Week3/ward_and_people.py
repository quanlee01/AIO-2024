class Person: 
    def __init__(self, name, year_of_birth): 
        self.name = name 
        self.year_of_birth = year_of_birth

    def describe(self): # virtual
        pass 


class Student(Person): 
    def __init__(self, name, year_of_birth, grade): 
        super().__init__(name, year_of_birth)
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.year_of_birth} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, year_of_birth, subject):
        super().__init__(name, year_of_birth)
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.year_of_birth} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, year_of_birth, specialist):
        super().__init__(name, year_of_birth)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.year_of_birth} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.residents_list = []

    def add_person(self, person):
        self.residents_list.append(person)

    def describe(self):
        print(f"Ward name: {self.name}")
        for resident in self.residents_list:
            resident.describe()

    def count_doctor(self): 
        cnt = 0
        for resident in self.residents_list:
            if type(resident) == Doctor:
                cnt += 1
        return cnt
    
    def sort_age(self): 
        self.residents_list.sort(key=lambda person: person.year_of_birth, reverse=True)

    def compute_average(self):
        mean_age = 0
        cnt = 0
        for resident in self.residents_list:
            if type(resident) == Teacher: 
                cnt += 1
                mean_age += resident.year_of_birth
        if cnt == 0: 
            return 0
        mean_age = mean_age / cnt
        return mean_age


if __name__ == "__main__":
    print("a)") 
    student1 = Student(name="studentA", year_of_birth=2010, grade="7")
    student1.describe()
    print("\n")

    teacher1 = Teacher(name="teacherA", year_of_birth=1969, subject="Math")
    teacher1.describe()
    print("\n")

    doctor1 = Doctor(name="doctorA", year_of_birth=1945, specialist="Endocrinologist")
    doctor1.describe()
    print("\n")


    print()
    print("b)") 
    teacher2 = Teacher(name="teacherB", year_of_birth=1995, subject="History")
    doctor2 = Doctor(name="doctorB", year_of_birth=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()
    print("\n")

    print()
    print("c)")
    print(f"Number of doctors: {ward1.count_doctor()}")

    print("\nd)")
    print("Ward1 list after sorting by age")
    ward1.sort_age()
    ward1.describe()

    print("\ne)")
    print(f"Average year of birth (teachers): {ward1.compute_average()}")  

