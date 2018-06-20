def recover():
    for i in range(1, n + 1):
        tmp = i % 2
        for balance in range(tmp, n // 2 + 1, 2):
            if string[i - 1] == '(':
                dp[tmp][balance] = dp[(i + 1) % 2][balance - 1]
            elif string[i - 1] == ')':
                dp[tmp][balance] = dp[(i + 1) % 2][balance + 1]
            else:
                dp[tmp][balance] = (dp[(i + 1) % 2][balance + 1] + dp[(i + 1) % 2][balance - 1]) % MOD
    return dp


MOD = 10 ** 9 + 7

recover_in = open('recover.in', 'r')
recover_out = open('recover.out', 'w')

# Читаем
string = recover_in.readline().rstrip()
n = len(string)
dp = [[0] * (n + 1) for i in range(2)]
dp[0][0] = 1
recover_in.close()

print(recover()[n % 2][0], file=recover_out)
recover_out.close()
