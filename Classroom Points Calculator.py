team1= 120
team2= 85
team3= 150
team4= 95
team5=110

total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("Total points   :",total)
print("Average per team  :",average)
stars = 30
stars_per_box = 5

boxes = stars // stars_per_box
leftover = stars % stars_per_box

print("Reward star :",stars)
print("Full boxes packed  :",boxes)
print("Leftover stars   :",leftover)

last_week = 500

print("Better than last week? :", total > last_week)
print("Same as last week?    :", total == last_week)
print("Atleast as good?      :", total >= last_week)

total += 30
print("After bonus points    :", total)

total -= 15
print("After penalty points  :", total)

boxes = total // 5
print("Final reward boxes    :", boxes)