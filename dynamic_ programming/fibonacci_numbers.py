
import sys
input = sys.stdin.readline

n = int(input())
cnt_fib = 0
cnt_fibonacci = 0

def fib(n):
    global cnt_fib
    if n == 1 or n==2 :
        cnt_fib += 1
        return 1
    else:
        return (fib(n-1) + fib(n-2))


f = [0 for _ in range(n+1)] 
f[1] = 1
f[2] = 1
def fibonacci(n):
    global cnt_fibonacci
    for  i in range(3,n+1):
        cnt_fibonacci += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib(n)
fibonacci(n)

print(cnt_fib, end = ' ')
print(cnt_fibonacci)
