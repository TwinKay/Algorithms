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

    static int TEST_CASE,N,M,O,F,startY,startX,endY,endX;
    static int[][] graph;
    static String res;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        TEST_CASE =  Integer.parseInt(input.readLine());
        for(int tc=0; tc<TEST_CASE; tc++){
            res = "인성 문제있어??";

            token = new StringTokenizer(input.readLine());
            N = Integer.parseInt(token.nextToken());
            M = Integer.parseInt(token.nextToken());
            O = Integer.parseInt(token.nextToken());
            F = Integer.parseInt(token.nextToken());
            startY = Integer.parseInt(token.nextToken())-1;
            startX = Integer.parseInt(token.nextToken())-1;
            endY = Integer.parseInt(token.nextToken())-1;
            endX = Integer.parseInt(token.nextToken())-1;

            graph = new int[N][M];
            for (int i = 0; i < O; i++) {
                token = new StringTokenizer(input.readLine());
                int y = Integer.parseInt(token.nextToken()) - 1;
                int x = Integer.parseInt(token.nextToken()) - 1;
                int height = Integer.parseInt(token.nextToken());
                graph[y][x] = height;
            }

            boolean[][] visited = new boolean[N][M];
            Deque<int[]> deq = new ArrayDeque<>();
            deq.addLast(new int[]{startX, startY, F});
            visited[startY][startX] = true;
            while (!deq.isEmpty()) {
                int[] cur = deq.pollFirst();
                int x = cur[0];
                int y = cur[1];
                int power = cur[2];

                if (x == endX && y == endY) {
                    res = "잘했어!!";
                    break;
                }
                if (power == 0) break;

                for (int k = 0; k < 4; k++) {
                    int dx = x + deltaX[k];
                    int dy = y + deltaY[k];
                    if (!isValid(dx, dy)) continue;
                    if (visited[dy][dx]) continue;
                    if (graph[dy][dx]-graph[y][x] > power) continue;
                    deq.addLast(new int[]{dx, dy, power-1});
                    visited[dy][dx] = true;
                }
            }
            System.out.println(res);
        }
    }

    public static boolean isValid(int x, int y){
        return 0<=x && x<M && 0<=y && y<N;
    }
}