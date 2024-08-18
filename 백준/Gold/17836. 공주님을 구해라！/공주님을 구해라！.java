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

        int res = 10002;
        flag:
        while (!deq.isEmpty()){
            int[] temp = deq.poll();
            int x = temp[0];
            int y = temp[1];
            int cnt = temp[2];
            int gum = temp[3];

            if (cnt == t+1) break flag;

            for (int i=0; i<4; i++){
                if (x+deltaX[i]>=0 && x+deltaX[i]<m && y+deltaY[i]>=0 && y+deltaY[i]<n){
                    if (!visited[y+deltaY[i]][x+deltaX[i]]){
                        if (graph[y+deltaY[i]][x+deltaX[i]]==0){
                            deq.add(new int[] {x+deltaX[i],y+deltaY[i],cnt+1,gum});
                            visited[y+deltaY[i]][x+deltaX[i]] = true;
                        } else if (graph[y+deltaY[i]][x+deltaX[i]]==1){
                            continue;
                        } else if (graph[y+deltaY[i]][x+deltaX[i]]==2){
                            visited[y+deltaY[i]][x+deltaX[i]] = true;
                            int cand = cnt + 1 + (n-1-y-deltaY[i]) + (m-1-x-deltaX[i]);
                            if (cand<res && cand<=t){
                                res = cand;
                            }
                        } else if (graph[y+deltaY[i]][x+deltaX[i]]==9){
                            if (cnt+1<res){
                                res = cnt+1;
                            }
                            break flag;
                        }
                    }
                }
            }
        }
        if (res!=10002){
            System.out.println(res);
        } else{
            System.out.println("Fail");
        }
    }
}