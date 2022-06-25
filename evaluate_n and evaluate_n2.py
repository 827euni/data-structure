import time, random

def evaluate_n2(A, x):
	result = 0
	k = 1
	g = 0
	
	for i in range(n):
		k= 1
		g=A[i]
		for _ in range(i):
			k*=x
		result += g*k
	return result
	
def evaluate_n(A, x):
	result = 0
	k = 1
	g = 0
	
	for i in range(n):
		g=A[i]
		if i == 0:
			k=1
		else :
			k *=x
		result += g*k
	return result
	
random.seed()		# random 함수 초기화

n = int(input())
A = []

for _ in range(n):
	a = random.randint(-1000,1000)
	A.append(a)

x = random.randint(-1000,1000)

s1 = time.process_time()
print(evaluate_n2(A,x))
e1 = time.process_time()
print("수행시간 =",e1-s1)
s2 = time.process_time()
print(evaluate_n(A,x))
e2 = time.process_time()
print("수행시간 =",e2-s2)

