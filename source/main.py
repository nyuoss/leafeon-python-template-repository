from source.utility.component import add


def hello():
    print("Hello World!")
    result = add(1, 2)
    result += 1
    print("Result incremented is {result}")
