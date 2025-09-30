import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M,A,B,K;
    static int[][] graph, newGraph;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        A = Integer.parseInt(token.nextToken());
        B = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());

        graph = new int[N][M];
        for (int k = 0; k < K; k++) {
            token = new StringTokenizer(input.readLine());
            int y = Integer.parseInt(token.nextToken())-1;
            int x = Integer.parseInt(token.nextToken())-1;
            graph[y][x] = 1;
        }
        token = new StringTokenizer(input.readLine());
        int startY = Integer.parseInt(token.nextToken())-1;
        int startX = Integer.parseInt(token.nextToken())-1;
        token = new StringTokenizer(input.readLine());
        int endY = Integer.parseInt(token.nextToken())-1;
        int endX = Integer.parseInt(token.nextToken())-1;
        
        newGraph = makeNewGraph(N,M,A,B,graph);
        int res = getDist(startX, startY, endX, endY);
        System.out.println(res);
        
    }
    static int getDist(int startX, int startY, int endX, int endY) {
        boolean[][] visited = new boolean[N][M];

        Deque<int[]> deq =  new ArrayDeque<>();
        deq.addLast(new int[]{startX,startY,0});
        visited[startY][startX] = true;
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int time = cur[2];
            if (x == endX && y == endY) {
                return time;
            }
            for (int k = 0; k < 4; k++) {
                int dx = x + deltaX[k];
                int dy = y + deltaY[k];
                if (!isValid(dx,dy)) continue;
                if (newGraph[dy][dx] == 1) continue;
                if (visited[dy][dx]) continue;
                deq.addLast(new int[]{dx, dy, time+1});
                visited[dy][dx] = true;
            }
        }
        return -1;
    }
    static boolean isValid(int x, int y) {
        return x >= 0 && x < newGraph[0].length && y >= 0 && y < newGraph.length;
    }
    static int[][] makeNewGraph(int N, int M, int A, int B, int[][] graph) {
        int[][] newGraph = new int[N-A+1][M-B+1];
        for (int i = 0; i < N-A+1; i++) {
            for (int j = 0; j < M-B+1; j++) {
                boolean isOne = false;
                for (int a = 0; a < A; a++) {
                    for (int b = 0; b < B; b++) {
                        if (graph[i+a][j+b] == 1) {
                            isOne = true;
                        }
                    }
                }
                if (isOne) {
                    newGraph[i][j] = 1;
                }else{
                    newGraph[i][j] = 0;
                }
            }
        }
        return newGraph;
    }
}