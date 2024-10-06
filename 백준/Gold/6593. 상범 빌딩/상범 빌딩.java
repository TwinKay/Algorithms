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

    static int L,N,M;
    static char[][][] graph;
    static boolean[][][] visited;

    static int[] deltaX = {0,0,1,-1,0,0};
    static int[] deltaY = {1,-1,0,0,0,0};
    static int[] deltaZ = {0,0,0,0,1,-1};

    public static void main(String[] args) throws IOException {
        while (true){
            token = new StringTokenizer(input.readLine());
            L = Integer.parseInt(token.nextToken());
            N = Integer.parseInt(token.nextToken());
            M = Integer.parseInt(token.nextToken());
            if (L==0) break;
            graph = new char[L][N][M];

            for (int i = 0; i < L; i++) {
                for (int j = 0; j < N; j++) {
                    String s = input.readLine();
                    graph[i][j] = s.toCharArray();
                }
                input.readLine();
            }
            visited = new boolean[L][N][M];
            int indX = 0, indY = 0, indZ = 0;
            for (int i = 0; i < L; i++) {
                for (int j = 0; j < N; j++) {
                    for (int k = 0; k < M; k++) {
                        if (graph[i][j][k]=='S'){
                            indX = k; indY = j; indZ = i;
                            break;
                        }
                    }
                }
            }
            Deque<int[]> deq = new ArrayDeque<>();
            deq.addLast(new int[]{indX,indY,indZ,0});
            visited[indZ][indY][indX] = true;
            boolean isFind = false;
            while (!deq.isEmpty()) {
                int[] cur = deq.pollFirst();
                int x = cur[0];
                int y = cur[1];
                int z = cur[2];
                int cnt = cur[3];

                if (graph[z][y][x]=='E'){
                    sb.append("Escaped in ").append(cnt).append(" minute(s).\n");
                    isFind = true;
                    break;
                }

                for (int i=0; i<6; i++){
                    int dx = cur[0]+deltaX[i];
                    int dy = cur[1]+deltaY[i];
                    int dz = cur[2]+deltaZ[i];

                    if (isValid(dx,dy,dz) && graph[dz][dy][dx]!='#' && !visited[dz][dy][dx]){
                        deq.addLast(new int[]{dx,dy,dz,cnt+1});
                        visited[dz][dy][dx] = true;
                    }
                }
            }
            if (!isFind){
                sb.append("Trapped!\n");
            }
        }
        System.out.println(sb);
    }
    public static boolean isValid(int x, int y, int z) {
        return x>=0 && x<M && y>=0 && y<N && z>=0 && z<L;
    }
}