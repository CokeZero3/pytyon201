import re

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case(0)|caffe(x)
# ^ (^de)  : 문자열의 시작 > desk, destination > (d) | fade(x)
# $ (se$)  : 문자열의 끝 > case, base (o) | face(x)

def print_match(m):

    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

m= p.match("careless") #match :
print_match(m)