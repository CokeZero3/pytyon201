import re


# https://www.w3schools.com/python/python_regex.asp
p = re.compile("ca.e")
def print_match(m):

    if m:
        print("m.group():",m.group()) #일치하는 문자열 반환
        print("m.string:",m.string) #입력받은 문자열
        print("m.start()",m.start()) #일치하는 문자열의 시작 index
        print("m.end()", m.end()) #일치하는 문자열의 끝 index
        print("m.span():", m.span()) #일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")


# m = p.search("good care")
# print_match(m)

lst = p.findall("careless, cafe") #findall: 일치하는 모든 것을 list형태로 
print(lst)