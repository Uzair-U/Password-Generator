import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerics = "0123456789"
sp_chars = "!@#$%&*?"

Use_for = lower_case + upper_case + numerics + sp_chars
length_for_pass = 8

password = "".join(random.sample(Use_for, length_for_pass))

print(password)
