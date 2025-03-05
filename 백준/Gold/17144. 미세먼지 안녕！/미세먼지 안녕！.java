import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int R,C,T;
    static int[][] graph;
    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};
    static int upCleanerX, upCleanerY, downCleanerX, downCleanerY;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        R = Integer.parseInt(token.nextToken());
        C = Integer.parseInt(token.nextToken());
        T = Integer.parseInt(token.nextToken());
        graph = new int[R][C];
        for (int i = 0; i < R; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < C; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
                if (graph[i][j] == -1) {
                    upCleanerX = 0; upCleanerY = i-1; downCleanerX = 0; downCleanerY = i;
                }
            }
        }
        
        for (int t=0; t<T; t++) {
            spread();
            clean();
        }
        
        int cnt = 2;
        for (int[] row : graph) {
            for (int e : row) {
                cnt += e;
            }
        }
        System.out.println(cnt);
    }
    static void clean() {
        // up
        for (int i = upCleanerY-1; i > 0; i--) {
            graph[i][0] = graph[i-1][0];
        }
        for (int i = 0; i < C-1; i++) {
            graph[0][i] = graph[0][i+1];
        }
        for (int i = 0; i < upCleanerY; i++) {
            graph[i][C-1] = graph[i+1][C-1];
        }
        for (int i = C-1; i > 1; i--) {
            graph[upCleanerY][i] = graph[upCleanerY][i-1];
        }
        graph[upCleanerY][upCleanerX+1] = 0;

        // down
        for (int i = downCleanerY+1; i < R-1; i++) {
            graph[i][0] = graph[i+1][0];
        }
        for (int i = 0; i < C-1; i++) {
            graph[R-1][i] = graph[R-1][i+1];
        }
        for (int i = R-1; i > downCleanerY; i--) {
            graph[i][C-1] = graph[i-1][C-1];
        }
        for (int i = C-1; i > 1; i--) {
            graph[downCleanerY][i] = graph[downCleanerY][i-1];
        }
        graph[downCleanerY][downCleanerX+1] = 0;
    }

    static void spread() {
        int[][] newGraph = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (graph[i][j] == -1) continue;
                int moveCnt = graph[i][j]/5;

                int cnt = 0;
                for (int k = 0; k < 4; k++) {
                    int ny = i + deltaY[k];
                    int nx = j + deltaX[k];
                    if (isValid(nx, ny) && graph[ny][nx] != -1) {
                        newGraph[ny][nx] += moveCnt;
                        cnt++;
                    }
                }
                newGraph[i][j] -= cnt * moveCnt;
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                graph[i][j] += newGraph[i][j];
            }
        }
    }
    
    static boolean isValid(int x, int y) {
        return x >= 0 && x < C && y >= 0 && y < R;
    }
}