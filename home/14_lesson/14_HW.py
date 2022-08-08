"""Test new commit"""
def logger(func):

    def wrapper(*args):
        result = func(*args)
        print(result)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

def main():
    add(4, 5)
    square_all(4, 5)

if __name__ == '__main__':
    main()