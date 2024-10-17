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

    static int M,N,T, idxX, idxY;
    static char[][] graph;
    static int[][] fireTime;
    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};
    static boolean[][] visited;


    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            M = Integer.parseInt(token.nextToken());
            N = Integer.parseInt(token.nextToken());

            graph = new char[N+2][M+2];
            for (char[] g : graph){
                Arrays.fill(g, '!');
            }
            for (int i = 1; i < N+1; i++) {
                String s = input.readLine();
                for (int j = 1; j < M+1; j++) {
                    graph[i][j] = s.charAt(j-1);
                    if (graph[i][j] == '@') {
                        idxX = j;
                        idxY = i;
                        graph[i][j] = '.';
                    }
                }
            }
            N = N+2; M = M+2;
            fireTime = new int[N][M];
            for (int i = 0; i < N; i++) {
                Arrays.fill(fireTime[i], -1);
            }
            Deque<int[]> deq = new ArrayDeque<>();
            for(int i=0; i<N; i++){
                for (int j=0; j<M; j++){
                    if (graph[i][j]=='*'){
                        deq.addLast(new int[]{j,i,0});
                        fireTime[i][j] = 0;
                        graph[i][j] = '.';
                    }
                }
            }
            while (!deq.isEmpty()){
                int[] cur = deq.pollFirst();
                int x = cur[0];
                int y = cur[1];
                int cnt = cur[2];
                for (int i=0; i<4; i++){
                    int dx = x+deltaX[i];
                    int dy = y+deltaY[i];
                    if (graph[dy][dx]=='.' && fireTime[dy][dx]==-1){
                        deq.addLast(new int[]{dx,dy,cnt+1});
                        fireTime[dy][dx] = cnt+1;
                    }
                }
            }

            int res = -1;
            deq = new ArrayDeque<>();
            visited = new boolean[N][M];
            deq.addLast(new int[]{idxX,idxY,0});
            visited[idxY][idxX] = true;
            flag:
            while (!deq.isEmpty()){
                int[] cur = deq.poll();
                int x = cur[0];
                int y = cur[1];
                int cnt = cur[2];
                for (int i=0; i<4; i++){
                    int dx = x+deltaX[i];
                    int dy = y+deltaY[i];
                    if (graph[dy][dx]=='!'){
                        res = cnt+1;
                        break flag;
                    }
                    if (graph[dy][dx]=='.' && !visited[dy][dx] && (fireTime[dy][dx]>cnt+1 || fireTime[dy][dx]==-1)){
                        deq.addLast(new int[]{dx,dy,cnt+1});
                        visited[dy][dx] = true;
                    }
                }
            }

            if(res==-1){
                System.out.println("IMPOSSIBLE");
            }else{
                System.out.println(res);
            }
        }
    }
}