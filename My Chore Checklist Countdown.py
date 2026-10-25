total_chores= 4
original_count = total_chores
print(f"you have {original_count} chores to finish!\n")
completed_count = 0
chore_num = 1
while chore_num <= total_chores:
    if chore_num ==1: next_chore = "Make your bed"
    elif chore_num ==2: next_chore = "feed the pet"
    elif chore_num ==3: next_chore = "take out the trash"
    else: next_chore= "wash your dishes"
    answer = input(f"Have you finished: {next_chore}? (yes/no):")
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! chores completed!.")
    else:
        print("finish it and check again.")
        print("chores remaining:",total_chores - completed_count)
        print()
        print("=======ALL CHORES COMPLETED======")
        print("great work on finishing all your checklist today\n")
        print("Now lets safely peek at an infinite loop....")
        test_value = 0
        safety_counter = 0
        while test_value <= 0:
            print("this condition never changes, so this would run forever!")
            safety_counter += 1
            if safety_counter == 3:
                print("(Stopping it on purpose- a real infinite loop never stops on its own!)")
                break
            print("\n=======CHORE CHECKLIST SUMMARY=======")
            print("Chores assinged today:", original_count)
            print("chores completed:", completed_count)
            print("chores remaining:", total_chores- completed_count)
            print("===========================================")