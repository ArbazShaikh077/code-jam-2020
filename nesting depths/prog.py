T = int(input())
for test_case in range(1, T + 1):
    S = input()
    prev = 0
    final_res = ''
    for i in range(len(S)):
        num = int(S[i])
        diff = num - prev
        if diff == 0:
            final_res += S[i]
        elif diff > 0:
            final_res += diff * '(' + S[i]
        else:
            final_res += (-diff) * ')' + S[i]
        prev = num
    if prev > 0:
        final_res += prev * ')'
    print("Case #{}: {}".format(test_case, final_res))
