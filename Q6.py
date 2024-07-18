
class Cha:
    def __init__(self, id, sex, job):
        self.Cha_id = id
        self.Cha_sex = sex
        self.Cha_job = job
    def attack(self, ann):
        print(self.Cha_id, "가, ", ann, "를 공격했다!")
        return ann

my_cha = Cha("뚜비", "남", "고양이")

print(my_cha.Cha_job)
my_cha.attack("몬스터")

