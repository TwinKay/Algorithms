import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static int[][] graph;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws Exception {
        N = Integer.parseInt(input.readLine());
        graph = new int[N][N];
        for (int i = 0; i < N; i++) {
            String line = input.readLine();
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(line.charAt(j) + "");
            }
        }

        boolean[][] visited = new boolean[N][N];
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{0, 0, 0});
        visited[0][0] = true;
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x =  cur[0];
            int y = cur[1];
            int cnt  = cur[2];

            if (x == N-1 && y == N-1) {
                System.out.println(cnt);
                break;
            }

            for (int k = 0; k < 4; k++) {
                int dx = x + deltaX[k];
                int dy = y + deltaY[k];
                if (!isValid(dx,dy)) continue;
                if (visited[dy][dx]) continue;
                if (graph[dy][dx] == 1){
                    deq.addFirst(new int[]{dx, dy, cnt});
                }else{
                    deq.addLast(new int[]{dx, dy, cnt+1});
                }
                visited[dy][dx] = true;
            }
        }

    }
    public static boolean isValid(int x, int y) {
        return 0<=x && x<N && 0<=y && y<N;
    }
}
