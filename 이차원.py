#배열 - 파이썬의 리스트와는 다르다
#     - 인덱싱을 사용한다는 차원에서는 같으나 원래 배열은 프로그램 시작전에 메모리가 확정된다.
#     - 데이터 추가나 삭제를 못한다.
#     - 데이터를 추가하거나 삭제가 가능하도록 list라는 타입을 따로 만들어야
#     - 파이썬은 배열이 아예 없다
#     - 2차원 또 3차원      1, 2, 3,     1, 2, 3


#list 안에 list를 또 둔다 => 머신러닝 파이썬은 list => 넘파이의 ndarray라는 타입으로 전환해야한다
#ndarray타입이 c언어 구조이다
#2차원 : list of list
matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

#2차원 : list of list
array = [    
            [
                [1,2,3],
                [4,5,6]
            ],
            [   
                [7,8,9],
                [10,11,12 ]
            ]
        ]

print(matrix)
print(matrix[0]) #1행
print(matrix[1]) #2행

print(matrix[0][0]) #1행 1열
print(matrix[0][1]) #1행 2열
print(matrix[0][2]) #1행 3열

for i in range (0, 3):
    for j in range(0,3):
        print( matrix[i][j], end=' ')
    print()
    
for i in range (0, 2):
    for j in range(0,2):
        for k in range(0,3):
            print( array[i][j][k], end=' ')
        print()
    print()
