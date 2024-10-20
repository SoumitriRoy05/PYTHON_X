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
