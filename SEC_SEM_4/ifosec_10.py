from hashlib import sha256

def passWord(data):
    if bool(len(data) < 8):
        return print('Введите пароль не менее 8 символов')
    if any(map(lambda x: x.islower(), data)) == False:
        return print('Пароль должен содержать строчные буквы')
    if any(map(lambda x: x.isupper(), data)) == False:
        return print('Пароль должен содержать прописные буквы')
    if any(map(lambda x: x.isdigit(), data)) == False:
        return print('Пароль должен содержать цыфры')
    else: 
        return print(f'Пароль корректен, хэш-значение: {sha256(data.encode()).hexdigest()}')
    
pw = input('Введите пароль: ')
passWord(pw)
