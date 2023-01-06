def task1():
    with open("day_6_input.txt", "r") as f:
        message = f.read()
    for i in range(0, len(message) - 4):
        if len(set(message[i:i+4])) == 4:
            print(i + 4)
            return

def task2():
    with open("day_6_input.txt", "r") as f:
        message = f.read()
    for i in range(0, len(message) - 14):
        if len(set(message[i:i+14])) == 14:
            print(i + 14)
            return

if __name__ == "__main__":
    task1()
    task2()
# end main