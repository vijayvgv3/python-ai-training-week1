def add(a, b):
    return a + b


def average(numbers):
    return sum(numbers) / len(numbers)



if __name__ == "__main__":
    print("Addition:", add(10, 20))

    numbers = [10, 20, 30, 40, 50]
    print("Average:", average(numbers))
    