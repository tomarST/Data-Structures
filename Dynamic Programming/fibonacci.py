def fibo(n,memo):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    else:
        memo[n]=fibo(n-1,memo)+fibo(n-2,memo)
    return memo[n]
    
n=994
memo={}
print(fibo(n,memo))
