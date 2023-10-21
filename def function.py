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
        if j // 10 in [3,6,9] or j % 10 in [3,6,9]:
            k.append(j)
    return k

a, b = map(int,input().split())
print(len(set(three(a,b) + sox(a,b))))