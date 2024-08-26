import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static int T, n;
    static char[][] graph;
    static boolean[][] visited;
    static int[] deltasX = {-1, 0, 1, -1, 1, -1, 0, 1};
    static int[] deltasY = {-1, -1, -1, 0, 0, 1, 1, 1};

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(input.readLine());
            graph = new char[n][n];
            visited = new boolean[n][n];

            for (int i = 0; i < n; i++) {
                graph[i] = input.readLine().toCharArray();
            }

            int cnt = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j] && graph[i][j] == '.' && isZero(i, j)) {
                        BFS(i, j);
                        cnt++;
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j] && graph[i][j] == '.') {
                        cnt++;
                    }
                }
            }
            sb.append("#").append(t).append(" ").append(cnt).append("\n");
        }
        System.out.println(sb);
    }

    public static void BFS(int x, int y) {
        Deque<int[]> deq = new ArrayDeque<>();
        deq.add(new int[]{x, y});
        visited[x][y] = true;

        while (!deq.isEmpty()) {
            int[] cur = deq.poll();
            int cx = cur[0];
            int cy = cur[1];

            for (int i = 0; i < 8; i++) {
                int dx = cx + deltasX[i];
                int dy = cy + deltasY[i];
                if (isValid(dx, dy) && !visited[dx][dy]) {
                    visited[dx][dy] = true;
                    if (isZero(dx, dy)) {
                        deq.add(new int[]{dx, dy});
                    }
                }
            }
        }
    }

    public static boolean isZero(int x, int y) {
        for (int i = 0; i < 8; i++) {
            int nx = x + deltasX[i];
            int ny = y + deltasY[i];
            if (isValid(nx, ny) && graph[nx][ny] == '*') {
                return false;
            }
        }
        return true;
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}