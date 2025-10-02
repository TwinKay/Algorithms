import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M;
    static int[][] graph;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        M = Integer.parseInt(token.nextToken());
        N = Integer.parseInt(token.nextToken());
        graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line =  input.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(line.charAt(j)+"");
            }
        }
        boolean[][] visited = new boolean[N][M];

        Deque<int[]> deq = new ArrayDeque<>();
        deq.add(new int[]{0,0,0});
        visited[0][0] = true;
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];
            if (x == M-1 && y == N-1) {
                System.out.println(cnt);
                break;
            }
            for (int k = 0; k < 4; k++) {
                int dx = x + deltaX[k];
                int dy = y + deltaY[k];
                if (!isValid(dx,dy)) continue;
                if (visited[dy][dx]) continue;
                if (graph[dy][dx] == 1){
                    deq.addLast(new int[]{dx, dy, cnt+1});
                    visited[dy][dx] = true;
                }else{
                    deq.addFirst(new int[]{dx, dy, cnt});
                    visited[dy][dx] = true;
                }
            }
        }
    }
    public static boolean isValid(int x, int y){
        return 0<=x && x<M && 0<=y && y<N;
    }
}