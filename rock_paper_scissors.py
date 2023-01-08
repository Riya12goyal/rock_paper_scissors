import random
choice = int(input("type 0 for rock, 1 for scissors, 2 for paper"))
comp =random.randint(0, 2)
print(f"computer chooses: {comp}")

if comp == 0 and choice == 1:
      print("you loose")
elif comp == 1 and choice == 2:
        print("you loose")
elif comp == 2 and choice == 0:
        print("you loose")
elif choice == comp:
        print("draw")
else:
       print("you win")






