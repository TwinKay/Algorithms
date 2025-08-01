import sys
from collections import deque

S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_apla_num(c):
    return S.find(c)

def init_graph(to,st):
    a = find_apla_num(to)
    for c in st:
        graph[a].append(find_apla_num(c))

def calc_dist(start, end):
    visited = [False]*len(S)
    start = find_apla_num(start)
    end = find_apla_num(end)
    deq = deque()
    deq.append([start,0])
    visited[start] = True
    while deq:
        cur = deq.popleft()
        num = cur[0]
        time = cur[1]

        if num == end:
            return time

        for n in graph[num]:
            if not visited[n]:
                deq.append([n,time+1])
                visited[n] = True

graph = []
for _ in range(len(S)):
    graph.append([])
init_graph("Q","WA")
init_graph("W","QASE")
init_graph("E","WSDR")
init_graph("R","EDFT")
init_graph("T","RFGY")
init_graph("Y","TGHU")
init_graph("U","YHJI")
init_graph("I","UJKO")
init_graph("O","IKLP")
init_graph("P","OL")
init_graph("A","QWSZ")
init_graph("S","WAZXDE")
init_graph("D","ESXCFR")
init_graph("F","RDCVGT")
init_graph("G","TFVBHY")
init_graph("H","YGBNJU")
init_graph("J","UHNMKI")
init_graph("K","IJMLO")
init_graph("L","POK")
init_graph("Z","ASX")
init_graph("X","SDCZ")
init_graph("C","DFVX")
init_graph("V","FGBC")
init_graph("B","GHNV")
init_graph("N","HJMB")
init_graph("M","NJK")

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    st = sys.stdin.readline().rstrip()
    for i in range(len(st)-1):
        cnt += calc_dist(st[i],st[i+1])*2
    cnt += len(st)
    print(cnt)

