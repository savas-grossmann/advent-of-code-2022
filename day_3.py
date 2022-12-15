def getPriority(double):
    return ord(double) - 96 if double.islower() else ord(double) - 38

def task1():
    priority = 0
    with open('day_3_input.txt', 'r') as f:
        rucksacks = f.readlines()
    for rucksack in rucksacks:
        compartments = [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]]
        for item in compartments[0]:
            if item in compartments[1]:
                priority += getPriority(item)
                break
    print(priority)

def task2():
    priority = 0
    with open('day_3_input.txt', 'r') as f:
        rucksacks = f.readlines()
    for i in range(0, len(rucksacks), 3):
        for item in rucksacks[i]:
            if item in rucksacks[i + 1] and item in rucksacks[i + 2]:
                priority += getPriority(item)
                break
    print(priority)

if __name__ == "__main__":
    task1()
    task2()    
# end main
