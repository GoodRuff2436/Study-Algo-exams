# バブルソート
# 隣同士を比較して、順序が逆なら交換する

data = [5, 3, 8, 4, 2]
要素数 = len(data)

    for i in range(0, 要素数 - 1):
        for j in range(要素数 - 1, i, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]

    print(f"整列後：{data}")

# バブルソート（令和5年問60）
# 手続printArrayは，配列integerArrayの要素を並べ替えて出力する。手続printArrayを呼び出したときの出力はどれか。ここで，配列の要素番号は1から始まる。

○printArray()
整数型：n, m
整数型の配列：integerArray() ← {2, 4, 1, 3}
for(nを1から(integerArrayの要素数－1)まで1ずつ増やす)
　for(mを1から(integerArrayの要素数－1)まで1ずつ増やす)
　　if(integerArray[m] > integerArray[m+1])
　　　integerArray[m]とintegerArray[m+1]の値を入れ替える
　　endif
　endfor
endfor
integerArrayの全ての要素を先頭から順にコンマ区切りで出力する
