# Start by asking for the number of numbers the user has
number = input("How many numbers do you have?\n")
# Convert the received number into integer
int_number = int(number)
# Direct user to start entering numbers
print("Enter the", int_number, "numbers")
# prepare an empty list to start entering the numbers
betting_numbers = []
# Write loop to receive the numbers
count = 0
while count < int_number:
    betting_numbers.append(input())
    count += 1
# Ask user for number they wish to bet with
bet_number = input("Enter the number you wish to bet with\n")
# Write a loop to check if the bet number exists on the pool
# Of the betting numbers
for nambari in betting_numbers:
    if nambari == bet_number:
        print("bet Successful")
        break
