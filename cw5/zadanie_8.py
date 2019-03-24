def samogloski(data):
    if not isinstance(data, str):
        raise TypeError("zly typ")
    for d in data.lower():
        if d in ['a', 'e', 'y', 'i', 'o', 'u']:
            yield d


for i in samogloski("wIzUaLiZaCjA DaNyCh"):
    print(i)