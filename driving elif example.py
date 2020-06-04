
print("enter your age")
yourage = int(input())

if yourage>18:
    print("your age is qualified to drive a car")
elif yourage==18:
    print("your age is 18 and we cannot decide. You can go to the RTO office in your city ")
elif yourage<18:
    print("your age is not qualified to drive a car")
else:
    print("you have entered false age")