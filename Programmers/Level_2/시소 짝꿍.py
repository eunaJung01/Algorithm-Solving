def solution(weights):
    weight_dict = dict()
    for w in weights:
        if w not in weight_dict:
            weight_dict[w] = 1
            continue
        weight_dict[w] += 1

    weights = list(set(weights))
    weights.sort()
    n = len(weights)

    answer = 0
    for i in range(n):
        weight = weights[i]
        if weight_dict[weight] > 1:
            answer += weight_dict[weight] * (weight_dict[weight] - 1) // 2
        for j in range(i + 1, n):
            if has_answer(weight, weights[j]):
                answer += (weight_dict[weight] * weight_dict[weights[j]])
    return answer


def has_answer(a, b):
    if a * 3 == b * 2:
        return True
    if a * 4 == b * 2:
        return True
    if a * 4 == b * 3:
        return True
    return False
