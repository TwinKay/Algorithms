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

    static int N,M,res,enterX,enterY,exitX,exitY;
    static int[][] graph;
    static boolean[][][] visited;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        enterY = Integer.parseInt(token.nextToken())-1;
        enterX = Integer.parseInt(token.nextToken())-1;
        token = new StringTokenizer(input.readLine());
        exitY = Integer.parseInt(token.nextToken())-1;
        exitX = Integer.parseInt(token.nextToken())-1;

        graph = new int[N][M];
        visited = new boolean[N][M][2];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        res = Integer.MAX_VALUE;

        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{enterX, enterY, 0, 1}); // x y magic len
        visited[enterY][enterX][0] = true;
        flag:
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int magic = cur[2];
            int len = cur[3];

            for (int i = 0; i < 4; i++) {
                int dx = x + deltaX[i];
                int dy = y + deltaY[i];
                if (isValid(dx,dy)){
                    if (graph[dy][dx] == 0 && !visited[dy][dx][magic]){
                        deq.addLast(new int[]{dx,dy,magic,len+1});
                        visited[dy][dx][magic] = true;
                        if (isExit(dx,dy)){
                            res = Math.min(res,len);
                            break flag;
                        }
                    }else if (graph[dy][dx] == 1 && magic==0  && !visited[dy][dx][magic+1]){
                        deq.addLast(new int[]{dx,dy,magic+1,len+1});
                        visited[dy][dx][magic] = true;
                        if (isExit(dx,dy)){
                            res = Math.min(res,len);
                            break flag;
                        }
                    }
                }
            }
        }
        if (res == Integer.MAX_VALUE) {
            System.out.println(-1);
        }else{
            System.out.println(res);
        }
    }
    public static boolean isExit (int x, int y){
        return x==exitX && y==exitY;
    }

    public static boolean isValid (int x, int y){
        return x >= 0 && x < M && y >= 0 && y < N;
    }
}
