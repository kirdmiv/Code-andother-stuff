def genome(n):
    a = 1
    c = 0
    t = 1
    g = 1
    MOD = 10 ** 9 + 7
    for i in range(n - 1):
        a, c, t, g = (t + g) % MOD, (a + c + t) % MOD, (c + t + g) % MOD, (a + c + t + g) % MOD
    return (a + g) % MOD


genome_in = open('genome.in', 'r')
genome_out = open('genome.out', 'w')

n = int(genome_in.readline())
genome_in.close()

print(genome(n), file=genome_out)
genome_in.close()