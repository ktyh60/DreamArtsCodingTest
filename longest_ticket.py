from collections import defaultdict
data = []

print("入力の最後に空行を入れて実行してください")
#入力を受けとってdataという二次元配列に格納
while True:
    line = input()
    if line == "":
        break
    row = [float(x.strip()) for x in line.split(',')]
    data.append(row)


#始点と終点を整数型に直す
edges = [[int(a), int(b), w] for a, b, w in data]

def find_longest_path(edges):
    
    # 指向性のグラフ作成　graphは始点とそこからいける駅の辞書　nodesは存在する駅の番号の配列
    graph = defaultdict(list)
    nodes = set()
    for u, v, w in edges:
        graph[u].append((v, w))
        nodes.add(u); nodes.add(v)

    best_length = 0
    best_path = []

    def dfs(current, visited, path, total, start):
        nonlocal best_length, best_path

        # —— 経路を記録 —— 
        if len(path) >= 2 and total > best_length:
            best_length = total
            best_path = path[:]   # 今の path をコピーして保存

        # —— 隣接ノードを巡る —— 
        for nbr, w in graph[current]:
            # （A） 未訪問なら通常の再帰探索
            if nbr not in visited:
                visited.add(nbr)
                dfs(nbr, visited, path + [nbr], total + w, start)
                visited.remove(nbr)

            # （B） ただし「始点に戻る」場合だけ特別に許可 → 経路記録のみ
            elif nbr == start and len(path) >= 2:
                new_total = total + w
                new_path = path + [nbr]
                if new_total > best_length:
                    best_length = new_total
                    best_path = new_path[:]
                # —— ここで再帰はせず、さらに先へは行かない —— 

    # 全ノードを「始点」として試す
    for start in nodes:
        dfs(start, {start}, [start], 0, start)

    return best_path, best_length


#関数実行
path, length = find_longest_path(edges)


#結果出力
for station in path:
    print(station)

