print("""
*************************

Random Password Generator

*************************
""")

import random

lower = "qwertyuıopasdfghjklizxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "#$/*?!,.%&"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all, length))
print("The password which you generated: ", password)