n,k = map(int, input().split())

fact_n = 1
for i in range(n):
    fact_n *= i+1

fact_k = 1
for i in range(k):
    fact_k *= i+1
    
fact_nk = 1
for i in range(n-k):
    fact_nk *= i+1
    

print(fact_n//(fact_k*fact_nk))