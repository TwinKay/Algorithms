import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n, m;
    static int[] deltaX = {0, 0, -1, 1};
    static int[] deltaY = {-1, 1, 0, 0};
    static char[][] graph;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            n = Integer.parseInt(token.nextToken());
            m = Integer.parseInt(token.nextToken());

            graph = new char[n][m];
            Deque<int[]> queue = new LinkedList<>();

            for (int i = 0; i < n; i++) {
                String line = input.readLine();
                for (int j = 0; j < m; j++) {
                    graph[i][j] = line.charAt(j);
                    if (graph[i][j] == 'W') {
                        queue.add(new int[]{j, i, 0});
                    }
                }
            }

            int res = 0;
            int[][] dist = new int[n][m];

            while (!queue.isEmpty()) {
                int[] cur = queue.poll();
                int x = cur[0];
                int y = cur[1];
                int cnt = cur[2];

                for (int i = 0; i < 4; i++) {
                    int dx = x + deltaX[i];
                    int dy = y + deltaY[i];

                    if (isValid(dx, dy) && graph[dy][dx] == 'L' && dist[dy][dx] == 0) {
                        dist[dy][dx] = cnt + 1;
                        res += cnt + 1;
                        queue.add(new int[]{dx, dy, cnt + 1});
                    }
                }
            }

            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && y >= 0 && x < m && y < n;
    }
}