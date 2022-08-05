
n, V = map(int, input().split())
v = [int(x) for x in input().split()]

mid = n // 2

def solve(len, step):
    arr = []
    for i in range(len):
        arr.append(v[i + step])

    F = [0] * len
    s = []
    def snp(i):
        if i == len:
            sum = 0
            for j in range(len):
                if F[j] == 1:
                    sum += arr[j]
            s.append(sum)
            return
        F[i] = 0
        snp(i+1)
        F[i] = 1
        snp(i+1)
    snp(0)
    return s

sum1 = solve(mid, 0)
sum2 = solve(n - mid, mid)
Max = 0

for i in range(len(sum1)):
    for j in range(len(sum2)):
        if sum1[i] + sum2[j] <= V:
            Max = max(Max, sum1[i] + sum2[j])

print(Max)

# F = [0] * n
# Max = 0
#
# def snp(i):
#     global Max
#     s = []
#     if i == n:
#         sum = 0
#         for j in range(n):
#             if F[j] == 1:
#                 sum += v[j]
#         if sum <= V:
#             Max = max(Max, sum)
#         return
#     F[i] = 0
#     snp(i+1)
#     F[i] = 1
#     snp(i+1)
#
# snp(0)
# print(Max)