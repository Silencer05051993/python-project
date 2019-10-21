def gen_fibonaci(n):
    star_val = 0
    next_val = 1
    for i in range(n):
        yield star_val
        star_val, next_val = next_val, star_val + next_val

if __name__ == '__main__':
    fibonaci_arr = []

    for fn in gen_fibonaci(20):
        fibonaci_arr.append(fn)
    print(fibonaci_arr)