import sys
sys.setrecursionlimit(10**5)


def back_track(n,res):
    if n==N-1:
        new_nums = [nums[0]]
        for j in range(1,N):
            if res[j-1] != 2:
                new_nums.append(nums[j])
                continue
            temp = new_nums.pop()
            new_nums.append(temp*10+nums[j])

        val = new_nums[0]
        index = 1
        for r in res:
            if r == 2:
                continue
            elif r == 0:
                val += new_nums[index]
                index += 1
            else:
                val -= new_nums[index]
                index += 1
        if val == 0:
            prt_indi = []
            for i in range(N-1):
                prt_indi.append(nums_str[i])
                prt_indi.append(dic[res[i]])
            prt_indi.append(nums_str[N-1])
            prt.append(''.join(prt_indi))
        return

    for i in range(3):
        back_track(n+1,res+[i])

prt = []
dic = {}
dic[0] = '+'
dic[1] = '-'
dic[2] = ' '
T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    nums = list(range(1,N+1))
    nums_str = list(map(str, nums))

    prt = []
    back_track(0,[])
    prt.sort()
    for p in prt:
        print(p)
    print()
