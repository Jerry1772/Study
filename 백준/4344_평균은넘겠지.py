iterations = int(input())

for _ in range(iterations):
    _input = list(map(int, input().split()))
    
    scores = _input[1:]

    mean = sum(scores)/_input[0]
    
    over_mean = sum([1 if val>mean else 0 for val in scores])

    percentile = round(over_mean/_input[0]*100, 3)

    print(f"{percentile:.3f}%")