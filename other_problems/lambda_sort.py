def index_sort(array, idx):
    array.sort(
        key=lambda item: [
            item[index] if direction == 0 else -item[index] for index, direction in idx
        ]
    )


if __name__ == "__main__":
    with open("input004.txt", "r") as f:
        n, m = map(int, f.readline().split())
        arr = []

        for _ in range(n):
            arr.append(list(map(int, f.readline().split())))

        k = int(f.readline())
        indices = []

        for _ in range(k):
            indices.append(list(map(int, f.readline().split())))

        index_sort(arr, indices)

        for row in arr:
            print(" ".join(map(str, row)))
