import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,K,L;
    static int[] directionArr;
    static int[][] graph;
    static boolean[][] snakeGraph;
    static Deque<int[]> snake;

    // 시계 방향
    static int[] deltaX = {1,0,-1,0};
    static int[] deltaY = {0,1,0,-1};

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        graph = new int[N][N];

        K = Integer.parseInt(input.readLine());
        for (int i = 0; i < K; i++) {
            token = new StringTokenizer(input.readLine());
            int y = Integer.parseInt(token.nextToken()) - 1;
            int x = Integer.parseInt(token.nextToken()) - 1;
            graph[y][x] = 1;
        }

        L = Integer.parseInt(input.readLine());
        directionArr = new int[10001];
        for (int i = 0; i < L; i++) {
            token = new StringTokenizer(input.readLine());
            int time = Integer.parseInt(token.nextToken());
            char direction = token.nextToken().charAt(0);
            if (direction == 'L') directionArr[time] = 1;
            else directionArr[time] = 2; // R
        }
        int dir = 20000;

        snake = new ArrayDeque<>();
        snakeGraph = new boolean[N][N];
        snake.addLast(new int[]{0,0});
        snakeGraph[0][0] = true;

        int time = 0;
        while (true) {
            time ++;

            int dx = snake.peekLast()[0] + deltaX[dir%4];
            int dy = snake.peekLast()[1] + deltaY[dir%4];

            if (!isValid(dx, dy) || snakeGraph[dy][dx]) break;

            if (graph[dy][dx] == 0) { // 사과 X
                snake.addLast(new int[]{dx,dy});
                snakeGraph[dy][dx] = true;
                int[] tailIdx = snake.pollFirst();
                snakeGraph[tailIdx[1]][tailIdx[0]] = false;

            }else{ // 사과 O
                snake.addLast(new int[]{dx,dy});
                snakeGraph[dy][dx] = true;
                graph[dy][dx] = 0; // 먹은 사과 처리
            }

            // 방향 돌리기
            if (directionArr[time] == 1) dir--;
            else if (directionArr[time] == 2) dir++;

        }
        System.out.println(time);

    }
    static boolean isValid(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }
}
