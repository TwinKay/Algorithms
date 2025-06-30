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

    static int K,W,H;
    static int res = -1;
    static int[][] graph;
    static boolean[][][] visited;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};
    static int[] jumpX = {-2,-1,1,2,2,1,-1,-2};
    static int[] jumpY = {-1,-2,-2,-1,1,2,2,1};

    public static void main(String[] args) throws IOException {
        K = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        W = Integer.parseInt(token.nextToken());
        H = Integer.parseInt(token.nextToken());
        graph = new int[H][W];
        visited = new boolean[K+1][H][W];
        for (int i = 0; i < H; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < W; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        
        if (W == 1 && H == 1) res = 0;

        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{0, 0, 0, 1}); // jump, W, H, cnt
        visited[0][0][0] = true;
        flag:
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int jumpCnt = cur[0];
            int x = cur[1];
            int y = cur[2];
            int cnt = cur[3];
            for (int k = 0; k < 4; k++) {
                int dx = x + deltaX[k];
                int dy = y + deltaY[k];
                if (isValid(dx, dy)) {
                    if (dx == W-1 && dy == H-1) {
                        res = cnt;
                        break flag;
                    }
                    if (graph[dy][dx] == 0 && !visited[jumpCnt][dy][dx]) {
                        deq.addLast(new int[]{jumpCnt, dx, dy, cnt+1});
                        visited[jumpCnt][dy][dx] = true;
                    }
                }
            }
            if (jumpCnt < K){
                for (int k = 0; k < 8; k++) {
                    int dx = x + jumpX[k];
                    int dy = y + jumpY[k];
                    if (isValid(dx, dy)) {
                        if (dx == W-1 && dy == H-1) {
                            res = cnt;
                            break flag;
                        }
                        if (graph[dy][dx] == 0 && !visited[jumpCnt+1][dy][dx]) {
                            deq.addLast(new int[]{jumpCnt+1, dx, dy, cnt+1});
                            visited[jumpCnt+1][dy][dx] = true;
                        }
                    }
                }
            }
        }
        System.out.println(res);

    }
    static boolean isValid(int x, int y) {
        return x >= 0 && x < W && y >= 0 && y < H;
    }
}
