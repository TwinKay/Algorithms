import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static int[][] graph;
    static boolean[][] visited;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new int[N][M];
        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = s.charAt(j) - '0';
            }
        }

        // bfs 후 좌표들 한번에 pop만큼 +=
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph[i][j] == 0 && !visited[i][j]) {
                    bfs(j,i);
                }
            }
        }
        for (int[] g : graph) {
            for (int n : g){
                sb.append(n%10);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
    public static void bfs(int firstX, int firstY){
        int zeroCnt = 0;
        HashSet<Integer> oneSet = new HashSet<>();
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{firstX, firstY});
        visited[firstY][firstX] = true;
        while(!deq.isEmpty()){
            zeroCnt++;
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            for (int i=0; i<4; i++){
                int dx = x+deltaX[i];
                int dy = y+deltaY[i];
                if (isValid(dx,dy) && !visited[dy][dx]){
                    if (graph[dy][dx] == 0){
                        deq.addLast(new int[]{dx,dy});
                        visited[dy][dx] = true;
                    }else{
                        oneSet.add(dx+dy*M);
                    }
                }
            }
        }
        for (int os : oneSet) {
            int x = os%M;
            int y = os/M;
            graph[y][x] += zeroCnt;
            graph[y][x] = graph[y][x];
        }

    }
    public static boolean isValid(int x, int y){
        return x >= 0 && x < M && y >= 0 && y < N;
    }
}