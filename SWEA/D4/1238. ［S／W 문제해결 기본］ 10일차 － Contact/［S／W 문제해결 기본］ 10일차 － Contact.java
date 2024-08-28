import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();
    static HashMap<Integer,List<Integer>> graph;
    static boolean[] visited;
    static int n, startIdx, maxCnt, max;

    public static void main(String[] args) throws IOException {
        for (int t=1; t<=10; t++){
            token = new StringTokenizer(input.readLine());
            n = Integer.parseInt(token.nextToken());
            startIdx = Integer.parseInt(token.nextToken());

            graph = new HashMap<>();
            for (int i = 0; i < 101; i++) {
                graph.put(i, new ArrayList<>());
            }
            token = new StringTokenizer(input.readLine());
            for (int i = 0; i < n/2; i++) {
                int a = Integer.parseInt(token.nextToken());
                int b = Integer.parseInt(token.nextToken());
                if (!graph.get(a).contains(b)) {
                    graph.get(a).add(b);
                }
            }
            maxCnt = 0;
            max = 0;
            visited = new boolean[101];
            Deque<int[]> deq = new ArrayDeque<>();
            deq.addLast(new int[]{startIdx,0});
            visited[startIdx] = true;
            while (!deq.isEmpty()) {
                int[] temp = deq.pollFirst();
                int cur = temp[0];
                int cnt = temp[1];
                if (cnt>maxCnt){
                    maxCnt = cnt;
                    max = cur;
                }else if (cnt==maxCnt){
                    if (cur>max){
                        max = cur;
                    }
                }
                for (int v: graph.get(cur)) {
                    if (!visited[v]) {
                        deq.addLast(new int[] {v,cnt+1});
                        visited[v] = true;
                    }
                }
            }
            sb.append("#").append(t).append(" ").append(max).append("\n");
        }
        System.out.println(sb);
    }
}