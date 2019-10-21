def generator(n):
    index = 0
    for i in range(n):
        index += 5
        yield i, index


def calculator(n):
    index = 0
    for i in range(n):
        index += 5
        return i, index


if __name__ == '__main__':
    gen_obj = generator(5)
    print(iter(gen_obj))
    print(next(gen_obj))
    print(len(gen_obj))