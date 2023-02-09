# WHILE LOOP

x = 0
while x <= 5:
    print(x)
    x += 1

y = 90
while y <= 100:
    print(y)
    y += 1

z = 50
while z >= 40:
    print(z)
    z -= 1


counter = 1
while counter <= 100:
    if (counter%2) == 0:
        print(counter)
        counter += 2
    else:
        counter += 1

#FOR IN LOOP
cars = ["BMW","Range","Tesla","Toyota","Noah"]
print(cars[1])
print(cars[3])
cars.append("landrover")

for gari in cars:
    print(gari)

# How many names do you have?
    # 5
# Enter the five names

    #
    #
    #
    #
    #
    # Logic print all the entered names
num = input("Enter your number\n")
jina = input("Enter your name\n")
print("Hello",jina,"you entered number",num)

nam = input("How many names do you have?")
print("Enter the",num,"numbers\n")
numbers = []
counter_two = 5
while counter_two <= nam:
    numbers.append(input())
    counter_two += 1
    print("Enter the correct number")