import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int T, N, res;
    static int[][] graph;
    static boolean[][] visited;
    static boolean[] dessertVisited;
    static int[] dx = {1, 1, -1, -1};
    static int[] dy = {1, -1, -1, 1};

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());

        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(input.readLine());
            graph = new int[N][N];
            visited = new boolean[N][N];
            res = -1;

            for (int i = 0; i < N; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < N; j++) {
                    graph[i][j] = Integer.parseInt(token.nextToken());;
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dessertVisited = new boolean[101];
                    DFS(i, j, i, j, 0, 0);
                }
            }
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);

    }

    static void DFS(int startX, int startY, int x, int y, int dir, int cnt) {
        if (dir == 4) {
            return;
        }

        if (dir == 3 && x == startX && y == startY && cnt >= 4) {
            res = Math.max(res, cnt);
            return;
        }

        for (int d = dir; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[ny][nx] && !dessertVisited[graph[ny][nx]]) {
                visited[ny][nx] = true;
                dessertVisited[graph[ny][nx]] = true;
                DFS(startX, startY, nx, ny, d, cnt + 1);
                visited[ny][nx] = false;
                dessertVisited[graph[ny][nx]] = false;
            }
        }
    }
}