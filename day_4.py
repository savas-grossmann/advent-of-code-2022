def task1():
    with open('day_4_input.txt', 'r') as f:
        plan = f.readlines()
    double = 0
    for pairs in plan:
        sections = pairs.strip().replace("-", ",").split(",")
        if ((int(sections[0]) >= int(sections[2]) and int(sections[1]) <= int(sections[3]))
        or (int(sections[0]) <= int(sections[2]) and int(sections[1]) >= int(sections[3]))):
            double += 1
    print(double)

def task2():
    with open('day_4_input.txt', 'r') as f:
        plan = f.readlines()
    double = 0
    for pairs in plan:
        sections = pairs.strip().replace("-", ",").split(",")
        section1 = list(range(int(sections[0]), int(sections[1]) + 1))
        section2 = list(range(int(sections[2]), int(sections[3]) + 1))
        if (int(sections[0]) in section2 or int(sections[1]) in section2
        or int(sections[2]) in section1 or int(sections[3]) in section1):
            double += 1
    print(double)
    
if __name__ == "__main__":
    task1()
    task2()
# end main