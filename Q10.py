class Person:
    def __init__(self, name, age, number):
        self.Person_name = name
        self.Person_age = age
        self.Person_number = number

    def check(self):
        print("화면에 입력하신 이름은", self.Person_name,
              "이며, 나이는", self.Person_age,
              ", 그리고 연락처는", self.Person_number, "입니다.")



my_p = Person("김인영", "29세", "0000-0000")

my_p.check()
