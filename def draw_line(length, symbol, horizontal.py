#1
def draw_line(length, symbol, horizontal=True):
    if horizontal:
        print(symbol * length)
    else:
        for _ in range(length):
            print(symbol)

#2
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


#3
def average_of_list(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)
