

is_running = True
name = input("Hello there,write your name")
print(f"{name} so signing in,will allow SC.com to have all accsess to what you are doing")
solution = input("Enter y to countinue and n to stop")
if solution.lower == "Y":
    print("Thank you let move on!")
else:
    is_running = False
