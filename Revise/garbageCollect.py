def solution(garbage, travel) -> int:
    travel_cum = [0]
    last = defaultdict(list)
    res = 0
    for i in range(0, len(travel)):
        travel_cum.append(travel_cum[-1] + travel[i])
    
    for i, bags in enumerate(garbage):
        res += len(bags)

        for bag_type in bags:
            last[bag_type] = i

    # print(last)
    res += sum(travel_cum[i] for i in last.values())
    
    return res