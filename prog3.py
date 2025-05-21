from itertools import permutations, product

def generate_permutations(Set, repetition):
    if repetition:
        return list(product(Set, repeat=len(Set)))  # With repetition
    else:
        return list(permutations(Set))  # Without repetition

if __name__ == "__main__":
    Set = set(map(int, input("Enter all elements of the set (space-separated): ").split()))

    with_repetition = generate_permutations(Set, repetition=True)
    without_repetition = generate_permutations(Set, repetition=False)

    print("\nPermutations with repetition:")
    for perm in with_repetition:
        print(perm)

    print("\nPermutations without repetition:")
    for perm in without_repetition:
        print(perm)

    print(f"\nTotal with repetition: {len(with_repetition)}")
    print(f"Total without repetition: {len(without_repetition)}")
