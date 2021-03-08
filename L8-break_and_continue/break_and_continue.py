# break and continue
# break -- exiting loop
# continue -- skip to next iteration

nums = [21, 52, 23, 10, 59, 30]

nums_less_than_30 = []

for num in nums:
    if num < 30:
        nums_less_than_30.append(num)
        # continue
        break

    print(num)

print(nums_less_than_30)

# robot clean hotel room
# room num: room rating
rooms = {
    "601": 70,
    "602": 55,
    "603": 40,
    "604": 80,
    "605": 90,
    "606": 10,
    "607": 15,
    "608": 80,
}

# if room cleanliness more than 80, robot should skip the room
for room, score in rooms.items():

    if score >= 80:
        print("Skipping Room " + room + ". It is very clean, score: " + str(score))
        continue

    # if the room is between 30 and 80, robot should clean the room
    if 30 <= score < 80:
        print("Cleaning Room " + room + "score: " + str(score))
        continue

    # if less than 30, poor robot can't handle it, should shut it down
    print("Room " + room + " is killing me....reporting score: " + str(score))
    print("Terminating system...")
    break
