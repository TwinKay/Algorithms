import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M,y, x,d;
    static int[][] graph;

    static int[] deltaX = {0,1,0,-1};
    static int[] deltaY = {-1,0,1,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        y = Integer.parseInt(token.nextToken());
        x = Integer.parseInt(token.nextToken());
        d = Integer.parseInt(token.nextToken());
        graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        int cnt = 0;
        while (true) {
            // #1
            if (graph[y][x] == 0) {
                graph[y][x] = -1;
                cnt++;
            }

            // #2
            if (isClean(x,y)){
                int dx = x + deltaX[(d+2)%4];
                int dy = y + deltaY[(d+2)%4];
                if (isValid(dx,dy) && graph[dy][dx] != 1) {
                    x = dx;
                    y = dy;
                }else{
                    break;
                }
                
            // #3
            }else {
                d = (d+3)%4;
                int dx = x + deltaX[d];
                int dy = y + deltaY[d];
                if (isValid(dx,dy) && graph[dy][dx] == 0) {
                    x = dx;
                    y = dy;
                }
            }
        }
        System.out.println(cnt);
    }

    static boolean isClean(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int dx = x+deltaX[i];
            int dy = y+deltaY[i];
            if (isValid(dx,dy) && graph[dy][dx] == 0) {
                return false;
            }
        }
        return true;
    }

    static boolean isValid(int x, int y) {
        return x >= 0 && x < M && y >= 0 && y < N;
    }
}