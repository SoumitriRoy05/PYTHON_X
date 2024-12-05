#Write a programme in Python using function to execute the given tree by displaying the values of statements present in the level1 and whenever the value of n is equals to 0 the function will get exit and return 0 (call the function foo with the value (3042, 0) and foo will call itself by the updated value of n and p).
#[Output of this programme will be the value of K, L, and P for each iteration of function foo until the condition is true.]

def foo(n, P):
    if n == 0:
        return P
    else:
        K = n % 10
        n = n // 10
        P = P + K + n
        print(f"K={K}, n={n}, P={P}")
        return foo(n, P)
result =foo(3042, 0)
print(f"Final P value:{result}")
