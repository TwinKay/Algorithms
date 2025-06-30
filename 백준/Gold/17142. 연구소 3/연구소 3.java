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

    static int N,M,blankCnt;
    static int[][] graph;

    static int[][] virusIdxs;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    static int res = Integer.MAX_VALUE;


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new int[N][N];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }
        int virusCnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 2) {
                    virusCnt++;
                }
            }
        }
        virusIdxs = new int[virusCnt][2];
        int idx = 0;
        blankCnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 2) {
                    virusIdxs[idx][0] = j;
                    virusIdxs[idx][1] = i;
                    idx++;
                }else if (graph[i][j] == 0){
                    blankCnt++;
                }
            }
        }

        boolean[] visited = new boolean[virusCnt];
        combination(visited, 0, virusCnt, M);

        if (res == Integer.MAX_VALUE) {
            System.out.println(-1);
        }else if (blankCnt == 0) {
            System.out.println(0);
        }else{
            System.out.println(res);
        }
    }

    static void combination(boolean[] arr, int start, int n, int r) {
        if (r == 0) {
            int[] activeIds = new int[M];
            int temp = 0;
            for (int i = 0; i < n; i++) {
                if (arr[i]) {
                    activeIds[temp] = i;
                    temp++;
                }
            }

            boolean[][] visited = new boolean[N][N];
            Deque<int[]> deq = new ArrayDeque<>();

            for (int i = 0; i < activeIds.length; i++) {
                deq.addLast(new int[] {virusIdxs[activeIds[i]][0], virusIdxs[activeIds[i]][1], 1});
                visited[virusIdxs[activeIds[i]][1]][virusIdxs[activeIds[i]][0]] = true;
            }

            int changeCnt = 0;
            while (!deq.isEmpty()) {
                int[] cur = deq.pollFirst();
                int x = cur[0];
                int y = cur[1];
                int time = cur[2];
                for (int i = 0; i < 4; i++) {
                    int dx = x + deltaX[i];
                    int dy = y + deltaY[i];

                    if (isValid(dx, dy) && !visited[dy][dx] && graph[dy][dx] != 1) {
                        deq.addLast(new int[] {dx, dy, time + 1});
                        visited[dy][dx] = true;
                        if (graph[dy][dx] == 0) changeCnt++;
                    }
                }
                if (changeCnt == blankCnt) {
                    res = Math.min(res, time);
                }
            }
            return;
        }

        for (int i = start; i < n; i++) {
            arr[i] = true;
            combination(arr, i + 1, n, r - 1);
            arr[i] = false;
        }
    }
    static boolean isValid(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }
}
