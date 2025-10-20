import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N = 501;
    static int cntDanger, cntDeath;
    static int[][] graph;
    static boolean[][] visited;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        graph = new int[N][N];
        visited = new boolean[N][N];


        cntDanger = Integer.parseInt(input.readLine());
        for (int i = 0; i < cntDanger; i++) {
            token = new StringTokenizer(input.readLine());
            int x1 = Integer.parseInt(token.nextToken());
            int y1 = Integer.parseInt(token.nextToken());
            int x2 = Integer.parseInt(token.nextToken());
            int y2 = Integer.parseInt(token.nextToken());

            int minX = Math.min(x1, x2);
            int maxX = Math.max(x1, x2);
            int minY = Math.min(y1, y2);
            int maxY = Math.max(y1, y2);

            for (int y = minY; y <= maxY; y++) {
                for (int x = minX; x <= maxX; x++) {
                    graph[x][y] = 1;
                }
            }
        }
        cntDeath = Integer.parseInt(input.readLine());
        for (int i = 0; i < cntDeath; i++) {
            token = new StringTokenizer(input.readLine());
            int x1 = Integer.parseInt(token.nextToken());
            int y1 = Integer.parseInt(token.nextToken());
            int x2 = Integer.parseInt(token.nextToken());
            int y2 = Integer.parseInt(token.nextToken());

            int minX = Math.min(x1, x2);
            int maxX = Math.max(x1, x2);
            int minY = Math.min(y1, y2);
            int maxY = Math.max(y1, y2);

            for (int y = minY; y <= maxY; y++) {
                for (int x = minX; x <= maxX; x++) {
                    graph[x][y] = 2;
                }
            }
        }

        int res = -1;
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[] {0, 0, 0});
        visited[0][0] = true;
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];
            if (x==N-1 && y==N-1) {
                res = cnt;
                break;
            }
            for (int k = 0; k < 4; k++) {
                int dx = x + deltaX[k];
                int dy = y + deltaY[k];
                if (!isValid(dx,dy)) continue;
                if (visited[dy][dx]) continue;
                if (graph[dy][dx] == 2) continue;
                if (graph[dy][dx] == 0) {
                    deq.addFirst(new int[] {dx, dy, cnt});
                    visited[dy][dx] = true;
                }else{
                    deq.addLast(new int[] {dx, dy, cnt+1});
                    visited[dy][dx] = true;
                }
            }
        }
        System.out.println(res);
    }
    static boolean isValid(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }
}