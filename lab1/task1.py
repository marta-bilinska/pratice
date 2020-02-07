import math


def is_palindrome(n):
    """
    (int) -> bool
    This function checks if the number is palindrome.
    """
    x = str(n)
    l = len(x)
    mid = l // 2
    for i in range(mid):
        if x[i] != x[l-i]:
            return False
    return True

def is_kaprekar(n):
    """
    (int) -> bool
    This function checks if the number is
    a kaprekar number.
    """
    square = n*n
    s = str(square)
    l =len(s)
    for i in range(l-1):
        if int(s[:i]) + int(s[i:]) == square:
            return True
    return False

def square_search(x):
    root = int(math.sqrt(x))
    lst = []
    for i in range(root):
        item = math.sqrt(x - i**2)
        if type(item) == int:
            lst.append(i,item)
    return lst

def product(n):
    num = 1000
    end_point = 9999*9999
    root = math.sqrt(n)
    if n < 1000000 or n > end_point:
        return False

    for i in range(root):
        if not is_kaprekar(i):
            continue
        if is_kaprekar(n/i):
            return True
    return False
def five_digit_layland():
    lst = []
    i, j = 2, 2
    while i < 99998:
        j = 2
        while j < i:
            z = j**i + i**j
            if 0 < z//10000 < 10:
                lst.append(z)
            j += 1
        i += 1
    return lst
def sorted_digits(n):
    remainder = 9
    while n > 0:
        temp = n%10
        if temp >= remainder:
            return False
        n = n // 10
        remainder = temp
    return True
def power_morphic(n, power):
    cube = pow(n, power)
    num = n
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    for i in digits:
        if i != cube % 10:
            return False
        cube = cube // 2
    return True
def lishrel(n):

def main():
    task = input("task:")



if __name__ == "__main__":
