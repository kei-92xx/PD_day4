#파이썬이 제공하는 데이터 타입은 아주 많다.
#변수를 미리 선언할 필요가 없다. 아무데서나 만들어서 쓰면 그때부터 사용가능하다.
#다른언어에서는 변수 자체가 특정타입만 저장가능하다.
#파이썬에서는 변수에는 아무 타입이나 저장이 가능하다.
#다른 언어에서는 변수에 타입을 주고 그타입만 저장가능하다.
#인터프리터 : 한줄 읽고 한줄 번역해서 실행하는 언어류들은 원래 변수에 특정 데이터 특정 데이터 타입만 저장
#하지 않고 아무타입이나 다 넣을 수 있다.

a1 = 4
print( a1, type(a1))

a1 = 4.5
print( a1, type(a1))

a1 = "4"
print( a1, type(a1))

#컬렉션류들 - 데이터를 담아두는 데이터 타입, list, tuple, dict, set(집합타입)
a1 = list()
a1.append("1")
a1.append("2")
print( a1, type(a1))

a1 = [1,2,3]
print( a1, type(a1))

#tuple은 한번 만들어지면 내부 데이터 수정이 되지 않는다. read-only
#list보다 속도가 빠르고 파이썬 내부에서 데이터를 대충 묶어서 데리고 다닐때 필요하다
#함수에서 값 반환시 많이 사용한다.
a1 = [1,2,3]
print( a1, type(a1))

a1 = dict()
a1["school"] = "학교"
a1["rain"] = "비"
print( a1, type(a1))

a1 = {"school":"학교", "rain":"비"}
print( a1, type(a1))

"""
a1 : 변수            다른언어들은 변수에 값을 저장하거나 참조를 저장한다
a1 : 100 - 실 데이터 일수도 있고 실 데이터가 있는 곳의 주소가 될수도 있다
주소 : 컴퓨터의 메모리 공간을 관리하기 쉽게 0, 1,2 숫자를 붙여나가고
이걸 번지(address), 주소라고 한다

주소 부여 방식이 1.직접 부여  2.간접부여
1. 직접주소방식 : 주소를 찾아갔더니 거기에 데이터가 존재하면         - 값타입
2. 간접주소방식 : 주소를 찾아갔더니 거기에 데이터의 주소가 들어있다  - 참조타입, 포인터 타입

C
int a;   //값타입
int *pA; //포인터타입

자바
배열, 클래스 - 참조타입 나머지는 다 값타입

파이썬
전부 참조다 값타입 존재 안함
전부 참조라서 실제 데이터 크기는 상관없이 변수에는 값 자체가 아니고 번지만 저장된다.
"""

