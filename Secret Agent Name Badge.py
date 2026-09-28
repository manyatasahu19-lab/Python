name= input("Enter your real name,Agent:")
gadget= input("Enter your favourite gadget:")
agent_number = 7
speed_rating= 9.5
mission_count= 12
height_m= 1.65
is_active= True
print("Name:", name,"-> type:",type(name))
print("gadget:",gadget,"->type:",type(gadget))
print("agent number:", agent_number,"->type:",type(agent_number))
print("speed rating:",speed_rating,"->type:", type(speed_rating))
print("Mission count:",mission_count,"->type:",type(mission_count))
print("height (m):",height_m,"->type:",type(height_m))
print("is active:", is_active,"->type:",type(is_active))
agent_number_text= str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text= str(is_active)
print("Agent number as text:", agent_number_text,"->type:",type(agent_number_text))
print("Mission count as text:",mission_count_text,"->type:",type(mission_count_text))
print("speed rating as text:",speed_rating_text,"->type:",type(speed_rating_text))
print("status as text:",status_text,"->type:",type(status_text))
first_three= name[0:3]
last_letter=name[-1:]
code_name= first_three+last_letter
print("first three letters of name:",first_three)
print("last letters of name:",last_letter)
print("secret code name:",code_name)
reversed_gadget= gadget[::-1]
print("reversed gadget name:",reversed_gadget)
badge_line_1="AGENT"+code_name.upper()
badge_line_2="ID:"+ agent_number_text+"|MISSIONS:"+ mission_count_text
badge_line_3="SPEED:"+speed_rating_text+"|ACTIVE:"+ status_text
badge_line_4="SECRET GADGET CODE:"+reversed_gadget.upper()
print("")
print("======SECRET AGENT BADGE=====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("===============")