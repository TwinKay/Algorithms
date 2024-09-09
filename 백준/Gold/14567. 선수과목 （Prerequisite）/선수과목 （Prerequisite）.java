import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static List<Integer>[] graph;
    static boolean[] visited;
    static int[] cntArr;
    static int[] save;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new List[N+1];
        for (int i = 0; i < N+1; i++) {
            graph[i] = new ArrayList<>();
        }
        visited = new boolean[N+1];
        cntArr = new int[N+1];

        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            graph[a].add(b);
            cntArr[b]++;
        }

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            if (cntArr[i] == 0) {
                deque.add(i);
                visited[i] = true;
            }
        }
        save = new int[N+1];
        int cnt = 1;
        boolean flag = true;
        while (flag) {
            flag = false;
            while (!deque.isEmpty()) {
                int a = deque.pollFirst();
                save[a] = cnt;
                for (int b :graph[a]) {
                    if (!visited[b]) {
                        cntArr[b]--;
                    }
                }
            }
            for (int i=1; i<=N; i++) {
                if (cntArr[i] == 0 && !visited[i]) {
                    deque.add(i);
                    visited[i] = true;
                    flag = true;
                }
            }
            cnt++;
        }
        for (int i=1; i<=N; i++) {
            sb.append(save[i]).append(" ");
        }
        System.out.println(sb);
    }
}