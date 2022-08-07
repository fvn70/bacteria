
def stage1():
    first = input()
    second = complem_seq(first)
    print(second)

def stage2():
    dna = input().split(' ')
    fr1 = dna[0].replace("CTGCAG", "C TGCAG")
    fr2 = dna[1].replace("GACGTC", "GACGT C")
    print(fr1)
    print(fr2)

def stage3():
    first = input()
    second = complem_seq(first)
    print(first)
    print(second)

def complem_seq(seq):
    dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([dic[n] for n in seq])

def gfp(seq, beg_site, end_site):
    seq1 = seq
    seq2 = complem_seq(seq)
    beg1 = seq1.find(beg_site) + 1
    end1 = seq1.find(end_site) + 1
    seq1 = seq1[beg1:end1]
    beg2 = seq2.find(complem_seq(beg_site)) + 5
    end2 = seq2.find(complem_seq(end_site)) + 5
    seq2 = seq2[beg2:end2]
    return seq1 +'\n' + seq2

def stage4():
    s1 = input()
    s2 = input().split()
    print(gfp(s1, s2[0], s2[1]))

def stage5():
    fn = input()
    txt = []
    with open(fn, 'r') as f:
        for s in f:
            txt.append(s)
    s1 = txt[0].split()
    s2 = txt[1].split()
    print(s1[0] + s2[0] + s1[1])
    print(s1[2] + s2[1] + s1[3])

stage5()
