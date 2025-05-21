def solve_polynomial():
    func = list(map(int, input("Enter your function coefficients (separated with space): ").split()))
    num = int(input("Enter value of your variable: "))

    value = 0
    degree = len(func) - 1

    for i in range(len(func)):
        value += func[i] * (num ** (degree - i))

    return value

print(solve_polynomial())
