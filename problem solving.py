n, k = map(int, input().split())

scores = list(map(int, input().split()))

threshold_score = scores[k-1]

count = 0

for s in scores:
    if s >= threshold_score and s > 0:
        count += 1
    else:
       
        break

print(count)