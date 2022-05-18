def list_of_f_numbers(n):
    f_numbers = [1, 1]
    f1 = 1
    f2 = 1
    fn = 0
    while len(f_numbers) < n:
        fn = f1 + f2
        f_numbers.append(fn)
        f1 = f2
        f2 = fn
    return(f_numbers)


n = 10000


for number in list_of_f_numbers(n):
    digits = len(str(number))
    print("number: " + str(number))
    print("digits: " + str(digits))
    print("index: " + str(list_of_f_numbers(n).index(number)))

    if digits == 1000:
        print(number)
        print(list_of_f_numbers(n).index(number))
        break
