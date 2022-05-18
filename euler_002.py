def list_of_f_numbers_less_than_n(n):
    f_numbers = [1, 1]
    f1 = 1
    f2 = 1
    fn = 0
    while fn < n:
        fn = f1 + f2
        f_numbers.append(fn)
        f1 = f2
        f2 = fn
    return(f_numbers)


sum = 0

for item in list(list_of_f_numbers_less_than_n(4000000)):
    if item % 2 == 0:

        sum += item
        print(item, sum)
