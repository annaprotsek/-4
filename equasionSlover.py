import sympy as sp
x = sp.symbols('x')
y1 = 3*x/sp.log(x) - sp.exp(2*x)
y1_prime = sp.diff(y1, x)
y2 = sp.sqrt(x**2 + 1) - sp.sin(x)
y2_prime = sp.diff(y2, x)

print("Похідна першої функції:")
print(y1_prime)

print("\nПохідна другої функції:")
print(y2_prime)