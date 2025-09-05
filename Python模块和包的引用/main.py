import math_utils


print(math_utils.factorial(4))

#
# import math_utils
#
# print(math_utils.factorial(5))  # 输出 120

# 导入方式 1（通过 __init__.py）
from string_tools import reverse_string, count_vowels

print(reverse_string.reverse_string("Hello"))      # 输出 "olleH"
print(count_vowels.count_vowels("Hello World"))  # 输出 3
