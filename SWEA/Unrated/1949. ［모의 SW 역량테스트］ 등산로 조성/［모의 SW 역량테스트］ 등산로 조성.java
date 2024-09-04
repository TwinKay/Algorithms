import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N, K;
    static int[][] graph;
    static boolean[][] visited;
    static int maxLength;

    static int[] deltaX = {-1, 1, 0, 0};
    static int[] deltaY = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());

        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            N = Integer.parseInt(token.nextToken());
            K = Integer.parseInt(token.nextToken());
            graph = new int[N][N];
            visited = new boolean[N][N];
            int maxHeight = 0;
            maxLength = 0;

            for (int i = 0; i < N; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(token.nextToken());
                    maxHeight = Math.max(maxHeight, graph[i][j]);
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (graph[i][j] == maxHeight) {
                        visited[i][j] = true;
                        dfs(j, i, 1, false);
                        visited[i][j] = false;
                    }
                }
            }

            sb.append("#").append(t).append(" ").append(maxLength).append("\n");
        }
        System.out.println(sb);
    }
    public static void dfs(int x, int y, int length, boolean isConst) {
        maxLength = Math.max(maxLength, length); // 최장 경로 갱신

        for (int i = 0; i < 4; i++) {
            int dx = x+deltaX[i];
            int dy = y+deltaY[i];

            if (isValid(dx,dy) && !visited[dy][dx]) {
                if (graph[dy][dx] < graph[y][x]) { // 현재보다 낮은 지형으로 이동
                    visited[dy][dx] = true;
                    dfs(dx, dy, length + 1, isConst);
                    visited[dy][dx] = false;
                } else if (!isConst && graph[dy][dx] - K < graph[y][x]) { // 공사 가능
                    int beforeHeight = graph[dy][dx];
                    graph[dy][dx] = graph[y][x] - 1; // 가능한 가장 높은 height
                    visited[dy][dx] = true;
                    dfs(dx, dy, length + 1, true); // 공사 후 DFS
                    visited[dy][dx] = false;
                    graph[dy][dx] = beforeHeight; // 원상복구
                }
            }
        }
    }
    public static boolean isValid(int x, int y) {
        return x>=0 && x<N && y>=0 && y<N;
    }
}