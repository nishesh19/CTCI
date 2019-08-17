def permute(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rem = seq[:i] + seq[i+1:]
            for x in permute(rem):
                yield seq[i] + x


for seq in permute(input()):
    print(seq)