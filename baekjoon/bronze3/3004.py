'''
최대 조각을 얻기 위해선 계속해서 가로세로 방향을 바꿔가며 잘라야 됨. 
이를 적용하면 아래 규칙을 발견할 수 있음.

자르지 않은 통판에서 바로 다음에 얻을 수 있는 조각을 a로 두었을 때 a는 1로 시작.
(= 첫 번째 한 번 자르면 하나를 추가로 얻음). 

a는 점점 누적되어 커지며, 홀수번째에는 a만큼, 
짝수번째에는 a+1만큼 조각을 더 얻을 수 있음(이때 a += 1). 

코드 자체는 반복문을 홀수인 1부터가 아니라 
0부터 시작하게 짰으므로 조건이 반대가 되겠죠.
'''

cut = int(input())
piece = 1
a = 1
for i in range(cut):
    if i % 2 != 0:
        a += 1
    piece += a
print(piece)