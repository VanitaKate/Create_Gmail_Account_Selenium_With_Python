import string
import random

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length "+str(length)+" is: "+result_str)

get_random_string(8)
get_random_string(8)
get_random_string(6)


