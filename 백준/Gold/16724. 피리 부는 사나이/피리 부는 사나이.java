import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, M;
    static char[][] graph;
    static boolean[][] visited;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        graph = new char[N][M];
        for (int i = 0; i < N; i++) {
            graph[i] = input.readLine().toCharArray();
        }

        parent = new int[N * M];
        for (int i = 0; i < N * M; i++) {
            parent[i] = i;
        }

        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j]) {
                    dfs(j, i);
                }
            }
        }

        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < N * M; i++) {
            set.add(find(i)); // parent[i]가 아님!! parent 배열은 최종 부모를 나타내지 않음!
        }
        System.out.println(set.size());
    }

    public static void dfs(int x, int y) {
        visited[y][x] = true;
        int dx = x;
        int dy = y;

        if (graph[y][x] == 'R') {
            dx++;
        } else if (graph[y][x] == 'L') {
            dx--;
        } else if (graph[y][x] == 'U') {
            dy--;
        } else if (graph[y][x] == 'D') {
            dy++;
        }

        if (isValid(dx, dy)) {
            int current = y * M + x;
            int next = dy * M + dx;

            union(current, next);

            if (!visited[dy][dx]) {
                dfs(dx, dy);
            }
        }
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < M && y >= 0 && y < N;
    }

    public static int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) {
            parent[y] = x;
        }
    }
}