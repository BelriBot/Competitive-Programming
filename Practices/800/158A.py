
n, k = map(int, input().split())
scores = [*map(int, input().split())]
print(sum(x >= scores[k - 1] > 0 for x in scores))
