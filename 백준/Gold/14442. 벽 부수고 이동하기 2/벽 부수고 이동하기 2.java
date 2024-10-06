import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, M, K;
    static int[][] graph;
    static int[][] visited;

    static int[] deltaX = {0, 0, -1, 1};
    static int[] deltaY = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        graph = new int[N][M];
        visited = new int[N][M];

        for (int i = 0; i < N; i++) {
            Arrays.fill(visited[i], Integer.MAX_VALUE);
            String s = input.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{0, 0, 1, 0});
        visited[0][0] = 0;

        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int firstX = cur[0];
            int firstY = cur[1];
            int cnt = cur[2];
            int crush = cur[3];

            if (firstX == M-1 && firstY == N-1) {
                System.out.println(cnt);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int dx = firstX + deltaX[i];
                int dy = firstY + deltaY[i];
                if (isValid(dx, dy)) {
                    int newCrush = crush + (graph[dy][dx] == 1 ? 1 : 0);
                    if (newCrush <= K && newCrush < visited[dy][dx]) {
                        visited[dy][dx] = newCrush;
                        deq.addLast(new int[]{dx, dy, cnt+1, newCrush});
                    }
                }
            }
        }
        System.out.println(-1);
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < M && y >= 0 && y < N;
    }
}