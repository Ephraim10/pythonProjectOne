x = 10
y = 20
if x > y:
    print("TRUE")
else:
    print("FALSE")
# Writen a logic to calculate a grading system
# With the following
# 0-----40-----E
# 40.1-----50-----D
# 50.1-----60-----C
# 60-----70-----B
# 70.1-----100----A
marks= 90
if marks < 0 or marks >100:
    print("please enter valid marks")
elif marks <=40:
    print("E")
elif marks <= 50:
    print("D")
elif marks <= 60:
    print("C")
elif marks <= 70:
    print("B")
else:
    print("A")