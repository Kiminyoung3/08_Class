
class Money:
    def __init__(self, len, m1, m2):
        self.Money_len = len
        self.Money_m1 = m1
        self.Money_m2 = m2

    def check(self, message):
        len_messge = len(message)

        if len_messge < self.Money_len:
            result = self.Money_m1
            return result
        else:
            result= self.Money_m2
            return result


x = Money(10, "500원", "1000원")
print(x.check("안녕하세요, 저의 이름은 김인영입니다."))