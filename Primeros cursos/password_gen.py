import random
def gen_password():
    mayus=['A', 'B', 'C', 'D', 'E', 'F','G']
    minus=['a','b','c','d','e','f']
    sym=['!', '#','$','&','(',')']
    num=['1','2','3','4','5','6','7','8','9','0']

    caracteres=mayus+minus+sym+num

    password=[]

    for i in range(15):
        caracter_random=random.choice(caracteres)
        password.append(caracter_random)

    password= ''.join(password)
    return password

def run():
    password=gen_password()
    print('Your password is: '+password)

        




if __name__ == "__main__":
    run()