import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, min;
    static int[][] graph;
    static boolean[][] visited;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        graph = new int[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        init();

        min = Integer.MAX_VALUE;

        Deque<int[]> deq = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 0) {
                    int id = -1;
                    for (int k = 0; k < 4; k++) {
                        int dx = i + deltaX[k];
                        int dy = j + deltaY[k];
                        if (isValid(dx, dy) && graph[dx][dy] != 0) {
                            id = graph[dx][dy];
                            break;
                        }
                    }
                    if (id == -1) continue;

                    for (int x = 0; x < N; x++) {
                        for (int y = 0; y < N; y++) {
                            visited[x][y] = false;
                        }
                    }

                    deq.clear();
                    deq.addLast(new int[]{i, j, 1});
                    visited[i][j] = true;

                    flag:
                    while (!deq.isEmpty()) {
                        int[] cur = deq.pollFirst();
                        for (int k = 0; k < 4; k++) {
                            int dx = cur[0] + deltaX[k];
                            int dy = cur[1] + deltaY[k];
                            int len = cur[2];
                            if (len >= min) break flag;

                            if (isValid(dx, dy) && !visited[dx][dy]) {
                                if (graph[dx][dy] == 0) {
                                    deq.addLast(new int[]{dx, dy, len + 1});
                                    visited[dx][dy] = true;
                                } else if (graph[dx][dy] != id) {
                                    min = Math.min(min, len);
                                    break flag;
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.println(min);
    }

    public static void init() {
        int[][] newGraph = new int[N][N];
        boolean[][] visited = new boolean[N][N];
        Deque<int[]> deq = new ArrayDeque<>();

        int groupId = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    newGraph[i][j] = groupId;
                    deq.addLast(new int[]{i, j});
                    visited[i][j] = true;
                    while (!deq.isEmpty()) {
                        int[] cur = deq.pollFirst();
                        int x = cur[0];
                        int y = cur[1];

                        for (int k = 0; k < 4; k++) {
                            int dx = x + deltaX[k];
                            int dy = y + deltaY[k];
                            if (isValid(dx, dy) && graph[dx][dy] == 1 && !visited[dx][dy]) {
                                newGraph[dx][dy] = groupId;
                                deq.addLast(new int[]{dx, dy});
                                visited[dx][dy] = true;
                            }
                        }
                    }
                    groupId++;
                }
            }
        }
        graph = newGraph;
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }
}
