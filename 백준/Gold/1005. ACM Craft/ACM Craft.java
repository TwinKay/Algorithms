import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int T,n,m,w;
    static int[] timeArr,cntArr,dp;
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());

        for (int t = 0; t < T; t++) {
            token = new StringTokenizer(input.readLine());
            n = Integer.parseInt(token.nextToken());
            m = Integer.parseInt(token.nextToken());

            timeArr = new int[n+1];
            cntArr = new int[n+1];
            dp = new int[n+1];
            graph = new ArrayList[n+1];

            for (int i = 0; i <= n; i++) {
                graph[i] = new ArrayList<>();
            }

            token = new StringTokenizer(input.readLine());
            for (int i = 1; i <= n; i++) {
                timeArr[i] = Integer.parseInt(token.nextToken());
            }

            for (int i = 0; i < m; i++) {
                token = new StringTokenizer(input.readLine());
                int a = Integer.parseInt(token.nextToken());
                int b = Integer.parseInt(token.nextToken());

                graph[a].add(b);
                cntArr[b]++;
            }

            w = Integer.parseInt(input.readLine());

            Queue<Integer> queue = new LinkedList<>();
            for (int i = 1; i <= n; i++) {
                if (cntArr[i] == 0) {
                    queue.add(i);
                    dp[i] = timeArr[i];
                }
            }

            while (!queue.isEmpty()) {
                int curr = queue.poll();

                for (int next : graph[curr]) {
                    dp[next] = Math.max(dp[next], dp[curr] + timeArr[next]);
                    cntArr[next]--;

                    if (cntArr[next] == 0) {
                        queue.add(next);
                    }
                }
            }
            sb.append(dp[w]).append("\n");
        }
        System.out.println(sb);
    }
}