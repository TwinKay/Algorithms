import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M,R,score;
    static int[][] graph;
    static boolean[][] visited;

    static int[] deltaX = {1,0,-1,0};
    static int[] deltaY = {0,1,0,-1};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        R = Integer.parseInt(token.nextToken());
        graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        visited = new boolean[N][M];
        score = 0;
        for (int i = 0; i < R; i++) {
            // attack
            token = new StringTokenizer(input.readLine());
            int y = Integer.parseInt(token.nextToken())-1;
            int x = Integer.parseInt(token.nextToken())-1;
            char order = token.nextToken().charAt(0);
            int ord;
            if (order == 'E') ord = 0;
            else if (order == 'S') ord = 1;
            else if (order == 'W') ord = 2;
            else ord = 3;
            int power;
            if (!visited[y][x]) {
                power = graph[y][x];
                visited[y][x] = true;
                power --;
                score ++;
                while (power > 0) {
                    int dx = x+deltaX[ord];
                    int dy = y+deltaY[ord];
                    if (isValid(dx, dy)) {
                        if (visited[dy][dx]) {
                            x = dx;
                            y = dy;
                            power --;
                        }else{
                            power = Math.max(power-1, graph[dy][dx]-1);
                            visited[dy][dx] = true;
                            score ++;
                            x = dx;
                            y = dy;
                        }
                    }
                    else{
                        break;
                    }
                }
            }
            //defence
            token = new StringTokenizer(input.readLine());
            y = Integer.parseInt(token.nextToken())-1;
            x = Integer.parseInt(token.nextToken())-1;
            visited[y][x] = false;
        }
        sb.append(score).append("\n");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visited[i][j]) {
                    sb.append("F ");
                }else{
                    sb.append("S ");
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
    static boolean isValid(int x, int y) {
        return x >= 0 && x < M && y >= 0 && y < N;
    }
}