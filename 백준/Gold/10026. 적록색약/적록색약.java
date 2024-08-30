import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static int n;
    static char[][] graph;
    static boolean[][] visited, visitedD;
    static int[] deltaX = {0, 0, -1, 1};
    static int[] deltaY = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(input.readLine());
        graph = new char[n][n];
        for (int i = 0; i < n; i++) {
            String s = input.readLine();
            graph[i] = s.toCharArray();
        }

        visited = new boolean[n][n];
        visitedD = new boolean[n][n];

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    BFS(i, j, graph[i][j]);
                    cnt++;
                }
            }
        }
        sb.append(cnt).append(" ");

        cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visitedD[i][j]) {
                    BFSD(i, j, graph[i][j]);
                    cnt++;
                }
            }
        }
        sb.append(cnt);
        System.out.println(sb);
    }

    public static void BFS(int y, int x, char c) {
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{y, x});
        visited[y][x] = true;
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int curY = cur[0];
            int curX = cur[1];
            for (int i = 0; i < 4; i++) {
                int dx = curX + deltaX[i];
                int dy = curY + deltaY[i];

                if (isValid(dy, dx) && !visited[dy][dx] && graph[dy][dx] == c) {
                    deq.addLast(new int[]{dy, dx});
                    visited[dy][dx] = true;
                }
            }
        }
    }

    public static void BFSD(int y, int x, char c) {
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{y, x});
        visitedD[y][x] = true;
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int curY = cur[0];
            int curX = cur[1];
            for (int i = 0; i < 4; i++) {
                int dx = curX + deltaX[i];
                int dy = curY + deltaY[i];

                if (c == 'G' || c == 'R') {
                    if (isValid(dy, dx) && !visitedD[dy][dx] && (graph[dy][dx] == 'G' || graph[dy][dx] == 'R')) {
                        deq.addLast(new int[]{dy, dx});
                        visitedD[dy][dx] = true;
                    }
                } else {
                    if (isValid(dy, dx) && !visitedD[dy][dx] && graph[dy][dx] == c) {
                        deq.addLast(new int[]{dy, dx});
                        visitedD[dy][dx] = true;
                    }
                }
            }
        }
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}