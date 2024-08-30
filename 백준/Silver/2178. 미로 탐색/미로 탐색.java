import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n,m;
    static boolean[][] graph, visited;
    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());

        graph = new boolean[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String s = input.readLine();
            for (int j = 0; j < m; j++) {
                if (s.charAt(j)=='1'){
                    graph[i][j] = true;
                }
            }
        }

        Deque<int[]> deq = new ArrayDeque<>();
        deq.push(new int[]{0,0,1});
        visited[0][0] = true;
        flag:
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int cnt = cur[2];

            for (int i=0; i<4; i++){
                if (isValid(x+deltaX[i],y+deltaY[i]) && graph[y+deltaY[i]][x+deltaX[i]] && !visited[y+deltaY[i]][x+deltaX[i]]){
                    if (x+deltaX[i] == m-1 && y+deltaY[i] == n-1){
                        System.out.println(cnt+1);
                        break flag;
                    }
                    deq.addLast(new int[]{x+deltaX[i],y+deltaY[i],cnt+1});
                    visited[y+deltaY[i]][x+deltaX[i]] = true;
                }
            }
        }
    }
    public static boolean isValid(int x, int y) {
        return x>=0 && x<m && y>=0 && y<n;
    }

}