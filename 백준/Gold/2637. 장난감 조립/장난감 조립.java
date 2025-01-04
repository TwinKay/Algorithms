import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static List<int[]>[] graph;
    static int[] cntArr;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        M = Integer.parseInt(input.readLine());
        graph = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }
        cntArr = new int[N+1];
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            int c = Integer.parseInt(token.nextToken());
            graph[a].add(new int[]{b,c});
            cntArr[b]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            if (cntArr[i] == 0) {
                queue.addLast(i);
            }
        }
        List<Integer> save = new ArrayList<>();
        while (!queue.isEmpty()) {
            int a = queue.pollFirst();
            save.add(a);
            for (int[] temp : graph[a]){
                int b = temp[0];
                cntArr[b]--;
                if (cntArr[b] == 0) {
                    queue.addLast(b);
                }
            }
        }
        int[] resArr = new int[N+1];
        resArr[N] = 1;
        for (int idx : save){
            int num = resArr[idx];
            for (int[] temp : graph[idx]){
                int nextIdx = temp[0];
                int mul = temp[1];
                resArr[nextIdx] += num*mul;
            }
        }
        List<Integer> baseItems = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            if (graph[i].size() == 0){
                baseItems.add(i);
            }
        }
        for (int idx : baseItems){
            sb.append(idx).append(" ").append(resArr[idx]).append("\n");
        }
        System.out.println(sb);

    }
}