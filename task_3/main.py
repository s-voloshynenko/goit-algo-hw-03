towers = {
    "A": [3, 2, 1],
    "B": [],
    "C": []
}

def step(source, target):
    towers[target].append(towers[source].pop())
    print(f"New state: {towers}")

def move_hanoi(k, source = "A", mid = "B", target = "C"):
    if k == 1:
        step(source, target)
        return

    move_hanoi(k - 1, source, target, mid)
    step(source, target)
    move_hanoi(k - 1, mid, source, target)

if __name__ == "__main__":
    print(f"Towers: {towers}")
    move_hanoi(k=len(towers["A"]))
    print(f"Result: {towers}")
