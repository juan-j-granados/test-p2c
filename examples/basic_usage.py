from p2c import build

n1, n2 = 7, 3

a, b, c, p2c, jac_p2c = build(n1, n2)
print("a:", a)
print("b:", b)
print("c:", c)
print("p2c(10):", p2c(10))
print("jac_p2c(10):", jac_p2c(10))