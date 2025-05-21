def find_solutions(C, n):
    def generate_solutions(current_sum, current_solution, remaining_terms):
        if current_sum == C and len(current_solution) == n:
            solutions.append(current_solution[:])
            return
        if len(current_solution) >= n or current_sum > C:
            return
        for i in range(remaining_terms[0], C - current_sum + 1):
            current_solution.append(i)
            generate_solutions(current_sum + i, current_solution, remaining_terms[1:])
            current_solution.pop()

    solutions = []
    generate_solutions(0, [], list(range(1, C + 1)))  # starting from 1 to avoid 0 unless you want to include 0
    return solutions

if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    C = int(input("Enter value of constant: "))

    all_solutions = find_solutions(C, n)

    print(f"\nAll solutions for {n} terms where the sum is {C}:")
    for solution in all_solutions:
        print(solution)
