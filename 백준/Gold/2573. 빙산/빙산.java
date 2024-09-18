import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[][] graph;
    static int N,M;

    static int[] deltaX = {-1,1,0,0};
    static int[] deltaY = {0,0,1,-1};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new int[N][M];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < M; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        int res = 0;
        while (true){
            res ++;
            melting();
            int cntIce = countIce();
            if (cntIce == 0){
                res = 0;
                break;
            } else if (cntIce >= 2){
                break;
            }
        }
        System.out.println(res);

    }
    public static void melting(){
        int[][] tempGraph = new int[N][M];
        for (int i = 1; i < N-1; i++){
            for (int j = 1; j < M-1; j++){
                if (graph[i][j] == 0) continue;
                int cntZero = countZero(j,i);
                int val = graph[i][j]-cntZero;
                if (val>=0){
                    tempGraph[i][j] = val;
                }else{
                    tempGraph[i][j] = 0;
                }
            }
        }
        graph = tempGraph;
    }
    public static int countIce(){
        int cnt = 0;
        boolean[][] visited = new boolean[N][M];
        for (int i = 1; i < N-1; i++){
            for (int j = 1; j < M-1; j++){
                if (graph[i][j] != 0 && !visited[i][j]) {
                    Deque<int[]> deq = new ArrayDeque<>();
                    deq.addLast(new int[]{j,i});
                    visited[i][j] = true;
                    while (!deq.isEmpty()){
                        int[] cur = deq.pollFirst();
                        int x = cur[0];
                        int y = cur[1];
                        for (int k = 0; k < 4; k++){
                            int dx = x+deltaX[k];
                            int dy = y+deltaY[k];
                            if (!visited[dy][dx] && graph[dy][dx] != 0){
                                deq.addLast(new int[]{dx,dy});
                                visited[dy][dx] = true;
                            }
                        }
                    }
                    cnt++;
                }
            }
        }
        return cnt;
    }


    public static int countZero(int x, int y){
        int cnt = 0;
        for (int i=0; i<4; i++){
            int dx = x + deltaX[i];
            int dy = y + deltaY[i];
            if (graph[dy][dx] == 0){
                cnt++;
            }
        }
        return cnt;
    }

}