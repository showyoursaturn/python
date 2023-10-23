#3,6,9 게임 개수 출력 (출력값이 있는 함수 만들기)
def three(a, b):
    s = []
    for i in range(a, b+1):
        if i % 3 == 0:
            s.append(i)
    return s

def sox(a,b):
    k = []
    for j in range (a, b+1):
        char = str(j)
        for dig in char:
            if dig in ['3', '6', '9']:
                k.append(j)
                break    #중복방지
    return k

a, b = map(int,input().split())
print(len(set(three(a,b) + sox(a,b)))) #three 와 #sox에서 겹치는 요소 제거 및 개수 출력

"""
매개변수에 파일이름과 찾고 싶은 정보의 종류를 입력하면, 파일을 열고 찾고 싶은 정보만 추출하여 출력해주는 함수 만들기
실습에서 test로 사용할 data: Personal_info.txt
personal_info라는 함수 만들기
매개변수 2개
파일이름
찾고 싶은 정보: 예) 이름, 나이, 지역, 전화번호
중첩된 함수로
파일 열고 읽는 함수
찾고 싶은 정보를 처리하는 함수
test run
personal_info("Personal_info.txt", "이름")
personal_info("Personal_info.txt", ＂나이")
"""

def personal_info(name, info): #제일 큰 틀의 함수 정의
    def fileread(name): #파일을 읽어오는 함수
        with open(name, "r") as f: #일단 열어_읽기모드로
            a = f.readlines() #전체 열고, 뉴라인 포함이라 나중에 수정
            b = []
            for s in a:
                b.append(s.strip('\n').split(": ")) #뉴라인 제거 하고 ": " 기준으로 나눠서 b리스트에 각각의 리스트 저장
            b = [item for item in b if item != ""] #만약에 b에 빈 문자열이 있을 경우 저장 안함 - 문서에 있어서 수정해줌
        return b

    def fileinfo(b, info):
        #파일 정보에서 그 파일을 찾아주는 함수, 이렇게 중첩함수에서 각 함수가 큰 틀의 변수를 각각 하나씩 가져가고, 상위 함수의 리턴값을 변수로 가져와도 된다
        c = []
        for i in b:
            if i[0] == info: #만약 b의 중첩된 리스트들의 첫번째 값이 info에 저장된 값과 일치할 때
              c.append(i[1]) #c리스트 에는 그 뒤의 값을 저장해준다.
        return c
    b = fileread(name) #다시 큰 틀의 함수에서 돌아와서 b 변수에 읽어오는 함수를,
    infos = fileinfo(b,info) #infos함수에 그 부분을 찾는 함수를 저장한다.

    if infos != None: #만약 infos에 값이 있을 경우,
        print(f'{info}: {infos}') #예쁘게 출력해준다.
    else:
        print('CANNOT FIND THIS')

personal_info("Personal_info.txt", "Age")
