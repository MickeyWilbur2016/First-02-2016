for i in range(1, 101):
    if i % 5 == 0 and i%3 == 0:
        print "{} is FizBuzz".format(i)
    elif i % 5 == 0:
        print "{} is Fizz".format(i)
    elif i % 3 == 0:
        print "{} is Buzz".format(i)
    else:
        print "{} is not fiz or buzz and definitely not FizzBuzz".format(i)