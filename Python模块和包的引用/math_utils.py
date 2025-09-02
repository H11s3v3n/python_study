def factorial(n):
    return n**n

# def factorial(n):
#     """递归方式计算 n 的阶乘"""
#     if n < 0:
#         raise ValueError("n 必须是非负整数")
#     if n in (0, 1):
#         return 1
#     return n * factorial(n - 1)
