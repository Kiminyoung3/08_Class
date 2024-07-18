class Num:
    def A(self, a, b):
        result = a+b
        return result
    def B(self, a, b):
        result = a-b
        return result
    def C(self, a, b):
        result = a*b
        return result
    def D(self, a, b):
        result = a/b
        return result

number = Num()
print(number.A(100, 20))