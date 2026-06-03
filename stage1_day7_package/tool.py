def add(a,b):
    print(a+b)

def get_code():
    import string , random
    s = string.ascii_uppercase +string.digits
    return ''.join(random.choices(s,k = 4))