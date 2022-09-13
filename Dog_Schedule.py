# finding out the exact time the dog will stay till (dogs don't stay more than a month usually)
def length_of_stay(month, day, year, stay, num_of_dogs, time_dog):
    for i in range(num_of_dogs):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
            if day + stay[i] <= 31:
                stay[i] += day
                time_dog[i] = str(month) + "/" + str(stay[i]) + "/" + str(year)
            else:
                stay[i] = (stay[i] + day) - 31
                time_dog[i] = str(month + 1) + "/" + str(stay[i]) + "/" + str(year)
        elif month == 12:
            if day + stay[i] <= 31:
                stay[i] += day
                time_dog[i] = str(month) + "/" + str(stay[i]) + "/" + str(year)
            else:
                stay[i] = (stay[i] + day) - 31
                time_dog[i] = "1/" + str(stay[i]) + "/" + str(year + 1)
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day + stay[i] <= 30:
                stay[i] += day
                time_dog[i] = str(month) + "/" + str(stay[i]) + "/" + str(year)
            else:
                stay[i] = (stay[i] + day) - 30
                time_dog[i] = str(month + 1) + "/" + str(stay[i]) + "/" + str(year)
        elif month == 2:
            if day + stay[i] <= 28:
                stay[i] += day
                time_dog[i] = str(month) + "/" + str(stay[i]) + "/" + str(year)
            else:
                stay[i] = (stay[i] + day) - 28
                time_dog[i] = str(month + 1) + "/" + str(stay[i]) + "/" + str(year)

dog_name_list = [" "] * 20
dog_breed_list = [" "] * 20
dog_gender_list = [" "] * 20
dog_age_list = [" "] * 20
dog_ns_list = [" "] * 20
dog_stay_list = [0] * 20

continue_schedule = "yes"
num_dogs = 0

print("DOG SCHEDULER\n-------------")

current_month = int(input("Month (as a #): "))
current_day = int(input("Day (as a #): "))
current_year = int(input("Year: "))

dog_time = [" "] * 20

# user input for schedule
while(continue_schedule == "yes"):
    dog_name_list[num_dogs] = (input("-------------\nDog Name: "))
    dog_breed_list[num_dogs] = (input("Dog Breed: "))
    dog_gender_list[num_dogs] = (input("Dog Gender (Male or Female): "))
    dog_age_list[num_dogs] = (input("Dog Age (Ex. 5 years or 8 months): "))
    dog_ns_list[num_dogs] = (input("Is the dog neutered/spayed? (Yes or No): "))
    dog_stay_list[num_dogs] = (int(input("# of days staying: ")))

    continue_schedule = input("-------------\nNext dog? (Yes or No): ").lower()

    num_dogs = num_dogs + 1

length_of_stay(current_month, current_day, current_year, dog_stay_list, num_dogs, dog_time)

for i in range(num_dogs):
    print(f"-------------\nDOG {i + 1}")
    print(f"Name: {dog_name_list[i]}")
    print(f"Breed: {dog_breed_list[i]}")
    print(f"Gender: {dog_gender_list[i]}")
    print(f"Age: {dog_age_list[i]}")
    print(f"Neutered/Spayed: {dog_ns_list[i]}")
    print(f"Staying till {dog_time[i]}")