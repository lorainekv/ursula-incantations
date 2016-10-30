import random
from first_line.beluga_sevruga import beluga_sevruga 

first_line = random.sample(beluga_sevruga, 2)
first_line = [word.title() for word in first_line]
print ", ".join(first_line)


