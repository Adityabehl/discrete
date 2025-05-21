#Create a class SET , Create member functions to perform the following SET operation.

class SET:
    def __init__(self, u_set):
        self.u_set = u_set

    def is_member(self, element):
        if element in self.u_set:
            return "Element Found"
        else:
            return "Element Not Found"

    def powerset(self):
        result = []
        length = len(self.u_set)
        u_list = list(self.u_set)
        for i in range(1 << length):
            subset = {u_list[j] for j in range(length) if (i & (1 << j))}
            result.append(subset)
        print("Your Required Powerset Is:", result)

    def subset(self, subset_set):
        if subset_set.u_set.issubset(self.u_set):
            return "This Is A Subset"
        else:
            return "This Is Not A Subset"

    def union_intersection(self, set2):
        print("Intersection Of Your Sets Are:", self.u_set.intersection(set2.u_set))
        print("Union Of Your Sets Are:", self.u_set.union(set2.u_set))

    def complement(self, complement_set):
        print("Complement Of Given Set Is:", self.u_set - complement_set.u_set)

    def difference_and_symmetric_difference(self, set2):
        print("Difference Of Your Sets Are:", self.u_set.difference(set2.u_set))
        print("Symmetric Difference Of Your Sets Are:", self.u_set.symmetric_difference(set2.u_set))

    def cartesian_product(self, set2):
        cartesian_product = {(x, y) for x in self.u_set for y in set2.u_set}
        print("Cartesian Product Of Your Sets Is:", cartesian_product)


def set_create(uni="Set"):
    u_set = set(map(int, input(f"Enter Elements Of {uni} (space-separated): ").split()))
    print(f"Your Given {uni} Is:", u_set)
    return u_set


def main():
    choice = input("""\nMain Menu:
1. Check Whether An Element Belongs To The Set Or Not.
2. List All The Elements Of The Power Set Of A Set.
3. Check Whether One Set Is A Subset Of The Other Or Not.
4. Find Union And Intersection Of Two Sets.
5. Find Complement Of Set.
6. Find Difference And Symmetric Difference Between Two Sets.
7. Find Cartesian Product Of Sets.
Enter Your Choice (1-7): """)

    if choice == '1':
        set1 = SET(set_create())
        element = int(input("Enter The Element To Search: "))
        print(set1.is_member(element))

    elif choice == '2':
        set1 = SET(set_create())
        set1.powerset()

    elif choice == '3':
        universal_set = SET(set_create("Universal Set"))
        subset_set = SET(set_create("Subset"))
        print(universal_set.subset(subset_set))

    elif choice == '4':
        set1 = SET(set_create("First Set"))
        set2 = SET(set_create("Another Set"))
        set1.union_intersection(set2)

    elif choice == '5':
        universal_set = SET(set_create("Universal Set"))
        complement_set = SET(set_create("Set"))
        universal_set.complement(complement_set)

    elif choice == '6':
        universal_set = SET(set_create("Universal Set Or Main"))
        another_set = SET(set_create("Another Set"))
        universal_set.difference_and_symmetric_difference(another_set)

    elif choice == '7':
        set1 = SET(set_create("First Set"))
        set2 = SET(set_create("Another Set"))
        set1.cartesian_product(set2)

    else:
        print("Invalid Input!! Please Try Again")
        main()


if __name__ == "__main__":
    for i in range(8):
        main()
