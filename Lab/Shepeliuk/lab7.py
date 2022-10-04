# Task 1
import random
import string
def random_char(y):
    return ' '.join(random.choice(string.ascii_letters) for x in range(y))
str = (random_char(25))
file = open('e:\\Lab\\Repository_33_35\\Lab\\Shepeliuk\\random_string.txt','w')
str = file.write(str)
file.close()

#Task 2
import random
import datetime
import pickle
users = [
    ['Артур',random.choice(range(1,99)) ], 
    ['Кейт',random.choice(range(1,99))], 
    ['Аліса',random.choice(range(1,99))],
    ['Майк',random.choice(range(1,99))],
] 
newUsers = dict(users)
params = {
    'data': newUsers,
    'created_at': datetime.datetime.now(),
}
# print(params)
with open('e:\\Lab\\Repository_33_35\\Lab\\Shepeliuk\\users_data.txt', 'wb') as f:
    pickle.dump(params, f)
