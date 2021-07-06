class solution(object):

    def power(self, x, n=0):
        if n==0:
            return 1
        return x**n


pow = solution()
val = pow.power(2.0000, 10)
print(f"{val:.4f}")

