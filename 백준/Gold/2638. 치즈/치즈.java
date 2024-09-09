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

    static int N,M,chzCnt;
    static int[][] graph;
    static boolean[][] visited;
    static Deque<int[]> deq;

    static int[] deltaX = {0,0,1,-1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        chzCnt = 0;
        graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(token.nextToken());
                graph[i][j] = num;
                if (num==1){
                    chzCnt++;
                }
            }
        }
        int time = 0;
        while (chzCnt!=0){
            visited = new boolean[N][M];
            deq = new ArrayDeque<>();
            deq.addLast(new int[]{0,0});
            visited[0][0] = true;
            while (!deq.isEmpty()){
                int[] cur = deq.pollFirst();
                int x = cur[0];
                int y = cur[1];
                for (int i=0; i<4; i++){
                    int dx = x+deltaX[i];
                    int dy = y+deltaY[i];
                    if (isValid(dx,dy) && !visited[dy][dx]){
                        if (graph[dy][dx]==0){
                            deq.addLast(new int[]{dx,dy});
                            visited[dy][dx] = true;
                        }else{
                            graph[dy][dx] ++;
                        }
                    }
                }
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (graph[i][j]>=3){
                        graph[i][j] = 0;
                        chzCnt--;
                    } else if (graph[i][j]==2){
                        graph[i][j] = 1;
                    }
                }
            }
            time++;
        }
        System.out.println(time);
    }
    public static boolean isValid(int x, int y){
        return x>=0 && x<M && y>=0 && y<N;
    }
}