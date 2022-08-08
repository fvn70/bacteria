def cut_dna(seq, mask):
    idx = seq.find(mask)
    seq1 = seq[:idx + 1] + ' ' + seq[idx + 1:]
    seq2 = complem_seq(seq)
    idx = seq2.find(complem_seq(mask))
    seq2 = seq2[:idx + 5] + ' ' + seq2[idx + 5:]
    return seq1, seq2

def complem_seq(seq):
    dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([dic[n] for n in seq])

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

def cut_gfp(seq, beg_site, end_site):
    seq1 = seq
    seq2 = complem_seq(seq)
    beg1 = seq1.find(beg_site) + 1
    end1 = seq1.find(end_site) + 1
    seq1 = seq1[beg1:end1]
    beg2 = seq2.find(complem_seq(beg_site)) + 5
    end2 = seq2.find(complem_seq(end_site)) + 5
    seq2 = seq2[beg2:end2]
    return seq1, seq2

def stage4():
    s1 = input()
    s2 = input().split()
    g1, g2 = cut_gfp(s1, s2[0], s2[1])
    print(g1)
    print(g2)

def stage5():
    data = read_data()
    s1 = data[0].split()
    s2 = data[1].split()
    print(s1[0] + s2[0] + s1[1])
    print(s1[2] + s2[1] + s1[3])

def read_data():
    fn = input()
    # fn = 'example6.txt'
    cnt = 0
    data = []
    with open(fn, 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip('\n')
            data.append(line)
            cnt += 1
            line = f.readline()
    if cnt == 1:
        data = data[0].split('\\n')
    return data

def stage6():
    data = read_data()
    dna = data[0]   # The original plasmid strand
    mask = data[1]  # The restriction site for cutting the plasmid
    gfp = data[2]   # The GFP original strand
    gfp_beg = data[3].split()[0]
    gfp_end = data[3].split()[1]

    dna1, dna2 = cut_dna(dna, mask)
    gfp1, gfp2 = cut_gfp(gfp, gfp_beg, gfp_end)

    dna1 = dna1.split()[0] + gfp1 + dna1.split()[1]
    dna2 = dna2.split()[0] + gfp2 + dna2.split()[1]
    print(dna1)
    print(dna2)


stage6()
