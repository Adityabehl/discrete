class SET:

  def_init__(self, u_set):
  
    self.u_set = u_set
  
  def is_member(self, element):
  
   if element in self.u_set:
  
     return "Element Found"
  
   else:
  
     return "Element Not Found"
  
  def powerset(self):
  
     Ist=[]
    
     length = len(self.u_set)
    
     for i in range(1 << length):
  
         Ist.append({self.u_set[j] for j in range(length) if (i & (1
      
     print("Your Required Powerset Are:: ", Ist)
      
  def subset(self, subset_set):
  
   if subset_set.u_set.issubset(self.u_set):
  
     return "This Is A Subset"
  
   else:
     return "This is Not A Subset"

  def union intersection(self, set2):
  
    print("Intersection Of Your Sets Are:: \n", self u_set.intersection(set2.u_set))
    
    print("Union Of Your Sets Are:: \n", self.u_set.union(set2.u_set))
  
  def complement(self, complement_set):
  
    print("Your Complement Of Set Is:: \n", self.u_set-complement_set.u_set)
  
  def difference_and_symmetric_difference(self, set2):
      
      print("Difference Of Your Sets Are:: \n", self.u_set.difference(set2.u_set))
      
      print("Symmetric Difference of your sets are:: \n",
      
      self.u_set.symmetric_difference(set2.u_set))
  
  def cartesian_product(self, set2):
  
      cartesian_product = {(x, y)for x in self.u_set for y in set2.u_set)
      
      print("Your Cartesian Product Are::", cartesian_product)
  
  def set_create(uni="set"):
  
      u_set set(map(int, input(f"Enter Your Element Of (uni) With A Space:: ").split()))
      
      print(f"Your Given (uni) Are::", u_set)
      
      return u set
  
  def main():
  
      choice = str(input("""Main Menull
      
      1. Check Whether An Element Belongs To The Set Or Not.
      
      2.List All The Elements Of The Power Set Of A Set.
      
      3.Check Whether One Set Is A Subset Of The Other Or Not.
      
      4.Find Union And Intersection Of Two Sets.
      
      5.Find Complement Of Set.
      
      6. Find Difference And Symmetric Difference Between Two Sets.
      
      7.Find Cartesian Product Of Sets.
      
      Enter Your Choice:: """))
  
      if choice == '1':
      
          set1SET(set create())
          
          element int(input("Enter Your Element:"))
          
          print(set1.is_member(element))
          
      elif choice == '2':
      
          set1SET(list(set_create()))
          set1.powerset()

      elif choice == '3':
        
        universal_set = SET(set_create(uni="Universal Set"))
        
        subset_set = SET(set_create(uni="Subset"))
        
        print(universal_set.subset(subset_set))
        
      elif choice == '4'
        
        set1 = SET(set_create(uni="First Set"))
        
        set2 = SET(set_create(uni="Another Set"))
        
        set1.union_intersection(set2)
        
      elif choice == '5':
        
        universal_set = SET(set_create(uni=" Universal Set"))
        
        complement_set = SET(set_create(uni="Set"))
        
        universal_set.complement(complement_set)
        
      elif choice == '6':
        
        universal_set = SET(set_create("Universal Set Or Main"))
        
        another_set = SET(set_create("Another Set"))
        
        universal_set.difference_and_symmetric_difference(another_set)
        
      elif choice == '7':
        
        set1 = SET(set_create("First set"))
        
        set2 = SET(set_create("Another set"))
        
        set1.cartesian_product(set2)
        
      else:
        
        print("Invalid Input!!\nPlease Try Again")

        main()

if name =="main":

for i in range(8):

main()  
