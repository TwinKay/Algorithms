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

    static int N,M;
    static char[][] graph;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new char[N][M];
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            graph[i] = s.toCharArray();
        }
        int res = 0;
        for (int i=0; i<N; i++){
            for (int j=0; j<M; j++){
                if (graph[i][j]=='L'){
                    res = Math.max(res,bfs(j,i));
                }
            }
        }
        System.out.println(res);

    }
    public static int bfs(int firstX, int firstY){
        int max = 0;
        boolean[][] visited = new boolean[N][M];
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{firstX, firstY, 0});
        visited[firstY][firstX] = true;
        while (!deq.isEmpty()){
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];
            max = Math.max(max, cnt);
            for (int i=0; i<4; i++){
                int dx = x+deltaX[i];
                int dy = y+deltaY[i];
                if (isValid(dx,dy) && graph[dy][dx]=='L' && !visited[dy][dx]){
                    deq.addLast(new int[]{dx,dy,cnt+1});
                    visited[dy][dx] = true;
                }
            }
        }
        return max;
    }
    public static boolean isValid(int x, int y){
        return x>=0 && x<M && y>=0 && y<N;
    }
}