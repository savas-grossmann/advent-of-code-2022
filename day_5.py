def task1():
    cargo = [
        [],
        list("RPCDBG"),
        list("HVG"),
        list("NSQDJPM"),
        list("PSLGDCNM"),
        list("JBNCPFLS"),
        list("QBDZVGTS"),
        list("BZMHFTQ"),
        list("CMDBF"),
        list("FCQG")
    ]
    with open('day_5_input.txt', 'r') as f:
        moves = [move.strip() for move in f.readlines()]
    for move in moves:
        move = move.split(" ")
        n, start, end = int(move[1]), int(move[3]), int(move[5])
        for _ in range(n):
            cargo[end].append(cargo[start].pop(-1))
    solution = ""
    for i in range(1, len(cargo)):
        solution += cargo[i].pop()
    print(solution)

def task2():
    cargo = [
        [],
        list("RPCDBG"),
        list("HVG"),
        list("NSQDJPM"),
        list("PSLGDCNM"),
        list("JBNCPFLS"),
        list("QBDZVGTS"),
        list("BZMHFTQ"),
        list("CMDBF"),
        list("FCQG")
    ]
    with open('day_5_input.txt', 'r') as f:
        moves = [move.strip() for move in f.readlines()]
    for move in moves:
        move = move.split(" ")
        n, start, end = int(move[1]), int(move[3]), int(move[5])
        cargo[end].extend(cargo[start][-n:])
        del cargo[start][-n:]
    solution = ""
    for i in range(1, len(cargo)):
        solution += cargo[i].pop()
    print(solution)

if __name__ == "__main__":
    task1()
    task2()
# end main