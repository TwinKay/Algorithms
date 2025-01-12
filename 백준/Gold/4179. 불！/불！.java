import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

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
        graph = new char[N+2][M+2];
        for (int col = 0; col < M+2; col++) {
            graph[0][col] = 'E';
            graph[N+1][col] = 'E';
        }

        for (int row = 0; row < N+2; row++) {
            graph[row][0] = 'E';
            graph[row][M+1] = 'E';
        }

        for (int i = 1; i < N+1; i++) {
            String s = input.readLine();
            for (int j = 1; j < M+1; j++) {
                graph[i][j] = s.charAt(j-1);
            }
        }

        List<int[]> jList = new ArrayList<>();
        for (int i = 0; i < N+2; i++) {
            for (int j = 0; j < M+2; j++) {
                if (graph[i][j] == 'J') {
                    jList.add(new int[]{j,i});
                }
            }
        }
        List<int[]> fList = new ArrayList<>();
        for (int i = 0; i < N+2; i++) {
            for (int j = 0; j < M+2; j++) {
                if (graph[i][j] == 'F') {
                    fList.add(new int[]{j,i});
                }
            }
        }

        int cnt = 0;
        flag:
        while (!jList.isEmpty()){
            cnt ++;

            List<int[]> jNextList = new ArrayList<>();
            for (int[] j : jList) {
                int x = j[0];
                int y = j[1];
                if (graph[y][x] != 'J') continue;
                for (int i=0; i<4; i++){
                    int dx = x+deltaX[i];
                    int dy = y+deltaY[i];

                    if (graph[dy][dx]=='.'){
                        graph[dy][dx] = 'J';
                        jNextList.add(new int[]{dx,dy});
                    } else if (graph[dy][dx] == 'E') {
                        break flag;
                    }
                }

            }

            List<int[]> fNextList = new ArrayList<>();
            for (int[] f : fList) {
                int x = f[0];
                int y = f[1];
                for (int i=0; i<4; i++){
                    int dx = x+deltaX[i];
                    int dy = y+deltaY[i];

                    if (graph[dy][dx]=='.' || graph[dy][dx]=='J') {
                        graph[dy][dx] = 'F';
                        fNextList.add(new int[]{dx,dy});
                    }
                }
            }
            jList = jNextList;
            fList = fNextList;
        }
        if (jList.isEmpty()){
            System.out.println("IMPOSSIBLE");
        }else{
            System.out.println(cnt);
        }
    }
}