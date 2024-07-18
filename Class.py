#객체 지향 프로그래밍
#복습

#사용자에게 수를 입력받아 홀수, 짝수를 판별하는 함수 제작
#
# def my_num(num):
#     x = ""
#     if num%2 == 0:
#         x = "짝수"
#     else:
#         x = "홀수"
#     return x
#
# a = int(input("수를 입력하세요: "))
# print(my_num(a))

#-------------------------------------------------

#랜덤 리스트의 요소들의 평균을 구하는 함수
#
# def my_list(list):
#     b = 0
#     c = len(list)
#     for a in list:
#         b = b+a
#     x = b/c
#     return x
#
# list3 = [1,2,3,4,5]
#
# print(my_list(list3))

#-----------------------------------------

#비어있는 리스트에 요소 추가

numbers = [1, 2, 3, 4, 5]
numbers.append(6) # "." 은 리스트 클래스만이 사용할 수 있는 함수를 사용하겠다는 표시
print(type(numbers))

string = "집에 가고싶어요. 당장 가고싶어요"
print(type(string))
print(string.count("가")) #count는 해당 변수 내의 문자열에 해당 문자가 몇 번 포함되어있는지 세는 것

class Dog: #class 클래스명->첫글자 대문자!(매개변수 불필요) ->클래스 선언->초기화->속성과 함수를 기입하면 된다.
    def __init__(self, name, breed): #초기화: 데이터를 담을 그릇을 미리 만들겠다고 선언.__init__(self, 속성1매개변수, 속성2매개변수):
        self.dog_name = name #
        self.dog_beed = breed
        self.dog_sex = "여"

    def bark(self):
        print(self.dog_name + "개가 짖습니다.")

print(Dog("나비", "말티즈").dog_name) #"나비"는 Dog 클래스의 dog_name에 할당되고, "말티즈"는 dog_name에 할당됨
Dog("나비", "푸들").bark()

my_dog  = Dog("뽀비", "사모예드")
my_dog.bark()