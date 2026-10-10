print("===== DAILY ACTIVITY PLANNER =====")
homework_time = int(input("Enter homework time in hours: "))
free_time = int(input("Enter free time in hours: "))
print("===== YOUR DAILY PLAN =====")
if homework_time >= 2:
    print("You have a lot of homework.")
    print("Complete difficult subjects first.")
else:
    print("Your homework load is manageable.")
    print("Finish your homework on time.")
if free_time >= 4:
    print("You have plenty of free time.")
    print("You can play games, read, or enjoy a hobby.")
else:
    print("You have limited free time.")
    print("Choose a short relaxing activity.")
if homework_time + free_time >= 6:
    print("Your day is well planned.")
else:
    print("You have some extra time to organize.")
print("====== PLAN COMPLETE ======")