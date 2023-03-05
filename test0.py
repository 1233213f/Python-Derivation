import sympy as sp

t, r = sp.symbols('t r')
fuc = t**r*(1+t**r)**(-r)
fuc_x = sp.diff(fuc, t)
print("对x求导结果 : ", fuc_x)

# 赋值
# fun_x_value = float(fuc_x.evalf(
#     subs={
#         x: 10,
#         y: 5,
#         z: 3}))
#
# print(fun_x_value)