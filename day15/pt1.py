def sequence(length):
    seq = [2, 15, 0, 9, 1, 20]
    lookup = {x: [i] for i, x in enumerate(seq, 1)}
    n = seq[-1]
    for i in range(len(seq) + 1, length + 1):
        seen = lookup[n] if n in lookup else None
        if seen is not None and len(seen) > 1:
            n = i - 1 - seen[1]
        else:
            n = 0

        if n in lookup:
            lookup[n] = [i, lookup[n][0]]
        else:
            lookup[n] = [i]
    return n


if __name__ == "__main__":
    print(sequence(2020))
