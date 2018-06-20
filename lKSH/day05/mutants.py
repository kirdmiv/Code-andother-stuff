def mutants(lst, num):
    left, right = -1, len(lst)
    while left + 1 != right:
        middle = (left + right) // 2
        if lst[middle] < num:
            left = middle
        else:
            right = middle
    return left


mutants_in = open('mutants.in', 'r')
mutants_out = open('mutants.out', 'w')

num_of_mutants = int(mutants_in.readline())
mutants_nums = list(map(int, mutants_in.readline().split()))
num_of_simple_mutants = int(mutants_in.readline())
simple_mutants_nums = list(map(int, mutants_in.readline().split()))
mutants_in.close()

ans = [0] * num_of_simple_mutants
for i in range(num_of_simple_mutants):
    ans[i] = str(mutants(mutants_nums, simple_mutants_nums[i] + 1) - mutants(mutants_nums, simple_mutants_nums[i]))
print('\n'.join(ans), file=mutants_out)
mutants_out.close()
