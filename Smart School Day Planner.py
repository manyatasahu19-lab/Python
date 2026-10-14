
print("=== Swimming Pool Entry Checker ===")
print("Answer 3 quick questions to check pool entry!\n")

age = int(input("How old are you? "))
can_swim = input("Can you swim? (yes / no): ").strip().lower()
adult = input("Is an adult with you? (yes / no): ").strip().lower()

print()
print("=== Your Pool Entry Result ===")
print("-" * 35)

# Check swimming ability first
if can_swim == "no":
    print("Pool access : Shallow pool only with adult supervision.")
    print("Deep pool   : Not allowed.")

elif can_swim == "yes" and age >= 12:
    print("Pool access : Deep pool, subject to pool rules.")

elif can_swim == "yes" and (adult == "yes" or age < 12):
    print("Pool access : Shallow pool with supervision.")

else:
    print("Pool access : Entry denied until safety requirements are met.")

# Additional safety checks
if can_swim == "no" and not (adult == "yes"):
    print("Safety tip  : An adult must accompany you.")

elif can_swim == "yes" or adult == "yes":
    print("Safety tip  : Follow the lifeguard's instructions.")

else:
    print("Safety tip  : Ask pool staff for assistance.")

print()
print("Pool entry check complete!")
