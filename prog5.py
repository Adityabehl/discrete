#Write a Program to evaluate a polynomial function. (For example store f(x) = 4n2 + 2n + 9 in an array 
#and for a given value of n, say n = 5, compute the value of f(n)).
def solve_polynomial():
    func = list(map(int, input("Enter your function coefficients (separated with space): ").split()))
    num = int(input("Enter value of your variable: "))

    value = 0
    degree = len(func) - 1

    for i in range(len(func)):
        value += func[i] * (num ** (degree - i))

    return value

print(solve_polynomial())
