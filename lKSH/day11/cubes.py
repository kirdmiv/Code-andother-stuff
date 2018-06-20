def cubes(first_set, second_set):
    res_and = list((first_set & second_set))
    res_masha = list((first_set - second_set))
    res_pasha = list((second_set - first_set))
    res_and.sort()
    res_masha.sort()
    res_pasha.sort()
    return [len(res_and)], res_and, [len(res_masha)], res_masha, [len(res_pasha)], res_pasha


cubes_in = open('cubes.in', 'r')
cubes_out = open('cubes.out', 'w')

n, m = map(int, cubes_in.readline().split())
masha_cubes = set()
for i in range(n):
    masha_cubes.add(int(cubes_in.readline().strip()))
pasha_cubes = set()
for i in range(m):
    pasha_cubes.add(int(cubes_in.readline().strip()))
cubes_in.close()

ans = cubes(masha_cubes, pasha_cubes)
for i in ans:
    print(*i, sep=' ', file=cubes_out)
cubes_out.close()
