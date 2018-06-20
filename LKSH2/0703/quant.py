MOD = 10 ** 9 + 7

quant_in = open('quant.in', 'r')
quant_out = open('quant.out', 'w')

# Читаем
n = int(quant_in.readline())
quant_in.close()

catalan_nums = [0] * (n + 1)
dp = [0] * (n + 1)

catalan_nums[0] = 1
dp[0] = 1

for i in range(n + 1):
    for j in range(i):
        catalan_nums[i] += (catalan_nums[j] * catalan_nums[i - j - 1])
        dp[i] += (catalan_nums[j] * dp[i - j - 1])
        dp[i] += (dp[j] * dp[i - j - 1])
    dp[i] %= MOD
    catalan_nums[i] %= MOD

print(dp[n], file=quant_out)
quant_out.close()
