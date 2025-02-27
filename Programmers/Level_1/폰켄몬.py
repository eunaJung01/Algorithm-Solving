def solution(nums):
    pokemons = dict()
    for num in nums:
        if num not in pokemons:
            pokemons[num] = 1

    get_cnt = len(nums) // 2
    type_cnt = len(pokemons.keys())
    if type_cnt <= get_cnt:
        return type_cnt
    return get_cnt
