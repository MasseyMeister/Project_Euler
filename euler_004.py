def check_palindrome(number):

    list = []

    for digit in str(number):
        list.append(digit)

    for x in range(len(list)):
        if list[x] == list[len(list) - 1 - x]:
            continue
        else:
            return(False)
    return(True)


list_of_palindromes = []

for i in range(999, 1, -1):
    for j in range(999, 1, -1):
        if check_palindrome(i*j):
            list_of_palindromes.append(i*j)

print(max(list_of_palindromes))
