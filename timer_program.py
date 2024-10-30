import time

# <<<<<< 1 >>>>>
my_time = int(input("Enter time in seconds: "))

for i in range(my_time):
    time.sleep(1)
    print(i + 1)
print("Time is up!")

