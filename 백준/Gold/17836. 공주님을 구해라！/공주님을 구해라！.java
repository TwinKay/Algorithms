import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[][] graph;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(token.nextToken());
        int m = Integer.parseInt(token.nextToken());
        int t = Integer.parseInt(token.nextToken());

        graph = new int[n][m];
        for (int i=0; i<n; i++){
            token = new StringTokenizer(input.readLine());
            for (int j=0; j<m; j++){
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        graph[n-1][m-1] = 9;

        visited = new boolean[n][m];

        Deque<int[]> deq = new ArrayDeque<>();
        deq.add(new int[] {0,0,0,0}); // x,y,cnt,gum
        visited[0][0] = true;

        int[] deltaX = {1,0,-1,0};
        int[] deltaY = {0,1,0,-1};

        int res = 10001;
        flag:
        while (!deq.isEmpty()){
            int[] temp = deq.poll();
            int x = temp[0];
            int y = temp[1];
            int cnt = temp[2];
            int gum = temp[3];

            if (cnt == t+1) break flag;

            for (int i=0; i<4; i++){
                int dx = x+deltaX[i]; int dy = y+deltaY[i];
                if (dx>=0 && dx<m && dy>=0 && dy<n && !visited[dy][dx]){
                    if (graph[dy][dx]==0){
                        deq.add(new int[] {dx,dy,cnt+1,gum});
                        visited[dy][dx] = true;
                    } else if (graph[dy][dx]==2){
                        visited[dy][dx] = true;
                        int cand = cnt + 1 + (n-1-dy) + (m-1-dx);
                        if (cand<res && cand<=t){
                            res = cand;
                        }
                    } else if (graph[dy][dx]==9){
                        if (cnt+1<res){
                            res = cnt+1;
                        }
                        break flag;
                    }
                }
            }
        }
        if (res!=10001){
            System.out.println(res);
        } else{
            System.out.println("Fail");
        }
    }
}