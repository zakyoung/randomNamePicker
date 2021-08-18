import random
def RandomNamePickerSingle(listOfNames):
  return random.choice(listOfNames)

def RandomNamePickerList(listOfNames):
  order = []
  while listOfNames:
    randomName = RandomNamePickerSingle(listOfNames)
    listOfNames.remove(randomName)
    order.append(randomName)
  return list(tuple(zip(range(1,len(order)+1),order)))

def run():
  NumberOfNames = int(input("How many names would you like to enter: "))
  listOfNames = [input(f"Enter name {number}: ") for number in range(1, NumberOfNames+1)]
  order = RandomNamePickerList(listOfNames)
  print(f"\nThe first choice is {order[0][1]}\n")
  print("The full order is: ")
  for value in order:
    print(f"{value[0]}. {value[1]}")
  
if __name__ == "__main__":
  run()

