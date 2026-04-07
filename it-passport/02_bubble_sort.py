# バブルソート

data = [5, 3, 8, 4, 2]
要素数 = len(data)

    for i in range(0, 要素数 - 1):
        for j in range(要素数 - 1, i, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]

    print(f"整列後：{data}")