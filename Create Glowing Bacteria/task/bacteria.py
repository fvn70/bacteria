dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def stage1():
    first = input()
    second = [dic[x] for x in first]
    print(''.join(second))

def stage2():
    dna = input().split(' ')
    fr1 = dna[0].replace("CTGCAG", "C TGCAG")
    fr2 = dna[1].replace("GACGTC", "GACGT C")
    print(fr1)
    print(fr2)

stage2()
