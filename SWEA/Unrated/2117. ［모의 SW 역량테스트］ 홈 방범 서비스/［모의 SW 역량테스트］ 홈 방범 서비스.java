import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N, M, numHouse;
    static boolean[][] graph;
    static int[] deltaX = {0, 0, -1, 1};
    static int[] deltaY = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());

        for (int t = 1; t <= T; t++) {
            token = new StringTokenizer(input.readLine());
            N = Integer.parseInt(token.nextToken());
            M = Integer.parseInt(token.nextToken());
            numHouse = 0;
            graph = new boolean[N][N];

            for (int i = 0; i < N; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < N; j++) {
                    int temp = Integer.parseInt(token.nextToken());
                    if (temp == 1) {
                        graph[i][j] = true;
                        numHouse++;
                    }
                }
            }

            int maxHouses = 0;

            // 미리 최댓값 k 계산
            int maxK = 1;
            while (maxK * maxK + (maxK - 1) * (maxK - 1) <= numHouse * M) {
                maxK++;
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    maxHouses = Math.max(maxHouses, bfs(i, j, maxK));
                }
            }

            sb.append("#").append(t).append(" ").append(maxHouses).append("\n");
        }
        System.out.println(sb);
    }

    public static int bfs(int startX, int startY, int maxK) {
        int maxHouses = 0;

        for (int k = 1; k <= maxK; k++) {
            boolean[][] visited = new boolean[N][N];
            Deque<int[]> queue = new ArrayDeque<>();
            queue.add(new int[]{startX, startY});
            visited[startY][startX] = true;

            int houseCount = 0;

            for (int step = 0; step < k; step++) {
                int size = queue.size();

                for (int i = 0; i < size; i++) {
                    int[] cur = queue.poll();
                    int x = cur[0];
                    int y = cur[1];

                    if (graph[y][x]) {
                        houseCount++;
                    }

                    for (int d = 0; d < 4; d++) {
                        int dx = x + deltaX[d];
                        int dy = y + deltaY[d];

                        if (isValid(dx, dy) && !visited[dy][dx]) {
                            visited[dy][dx] = true;
                            queue.add(new int[]{dx, dy});
                        }
                    }
                }
            }

            int cost = k * k + (k - 1) * (k - 1);
            int profit = houseCount * M;

            if (profit >= cost) {
                maxHouses = Math.max(maxHouses, houseCount);
            }
        }
        return maxHouses;
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }
}