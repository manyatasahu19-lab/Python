name = input("Enter your name: ")
club = input("Enter your favourite school club: ")
member_number = 7
points = 9.5
activities = 12
height_m = 1.65
is_active = True
print("Name:", name, "-> type:", type(name))
print("Club:", club, "-> type:", type(club))
print("Member number:", member_number, "-> type:", type(member_number))
print("Points:", points, "-> type:", type(points))
print("Activities:", activities, "-> type:", type(activities))
print("Height (m):", height_m, "-> type:", type(height_m))
print("Is active:", is_active, "-> type:", type(is_active))
member_number_text = str(member_number)
activities_text = str(activities)
points_text = str(points)
status_text = str(is_active)
print("Member number as text:", member_number_text, "-> type:", type(member_number_text))
print("Activities as text:", activities_text, "-> type:", type(activities_text))
print("Points as text:", points_text, "-> type:", type(points_text))
print("Status as text:", status_text, "-> type:", type(status_text))
first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First three letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Club code name:", code_name)
reversed_club = club[::-1]
print("Reversed club name:", reversed_club)
badge_line_1 = "MEMBER " + code_name.upper()
badge_line_2 = "ID:" + member_number_text + "|ACTIVITIES:" + activities_text
badge_line_3 = "POINTS:" + points_text + "|ACTIVE:" + status_text
badge_line_4 = "CLUB CODE:" + reversed_club.upper()
print("")
print("====== SCHOOL CLUB BADGE ======")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===============================")