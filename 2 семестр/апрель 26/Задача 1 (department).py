class Department:

    def __init__(self, name: str, code: int):
        self._name = name
        self._code = code
        self._courses = []

    def add_course(self, title, code, credits):
        crs = CourseTemplate(title, code, credits, self)
        return crs

    def append_course(self, crs):
        if crs in self._courses:
            print(f"Курс {crs} уже существует")
            #assert ValueError("курс уэе существует")
        else:   self._courses.append(crs)

    def __repr__(self):
        return f"{self._name} -> {self._courses}"

class CourseTemplate:

    def __init__(self, title: str, code: int, credits: int, department):
        self._title = title
        self._code = code
        self._credits = credits
        self._department = department
        self._offerings = []
        department.append_course(self)

    def add_offering(self, template: str, year: int):
        ofr = CourseOffering(template, year)
        self._offerings.append(ofr)
        return ofr

    def __repr__(self):
        return f"{self._title} -> {self._offerings}"


class CourseOffering:

    def __init__(self, template, year):
        self._template = template
        self._year = year
        self._students = []

    def enrol(self, student):
        self._students.append(student)

    def __repr__(self):
        return f"{self._template} -> {self._students}"

class Student:
    def __init__(self, name, stud_no):
        self._name = name
        self._stud_no = stud_no

    def enrol(self, course):
        course.enrol(self)

    def __repr__(self):
        return f"{self._name}"


if __name__ == "__main__":
    FCPT = Department("fcpt", 6309106)
    a = CourseTemplate("counter-strike-2",1,2,FCPT)
    FCPT.append_course(a)
    math = FCPT.add_course("math", 123, 10)
    economy = CourseTemplate("economy", 13223, 33, FCPT)
    # my_group = math.add_offering("20121", 1)
    # Oleg = Student("Oleg", 228)
    # Oleg.enrol(my_group)
    # Ivan = Student("Ivan",  777)
    # my_group.enrol(Ivan)
    #
    print(FCPT)
    print(math)
    print(economy)
    #print(my_group)
    # print(Oleg)
    # print(Ivan)