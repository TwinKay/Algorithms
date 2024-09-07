import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int R, C;
    static char[][] graph;
    static boolean[][] visited;
    static List<Character> save;
    static int res = 0;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        R = Integer.parseInt(token.nextToken());
        C = Integer.parseInt(token.nextToken());

        graph = new char[R][C];
        for (int i = 0; i < R; i++) {
            graph[i] = input.readLine().toCharArray();
        }
        visited = new boolean[R][C];

        save = new ArrayList<>();
        save.add(graph[0][0]);
        visited[0][0] = true;

        dfs(0, 0);
        System.out.println(res);
    }

    public static void dfs(int x, int y) {
        res = Math.max(res, save.size());
        for (int i = 0; i < 4; i++) {
            int dx = x + deltaX[i];
            int dy = y + deltaY[i];
            if (isValid(dx, dy) && !visited[dx][dy] && !save.contains(graph[dx][dy])) {
                save.add(graph[dx][dy]);
                visited[dx][dy] = true;
                dfs(dx, dy);
                save.remove(save.size() - 1);
                visited[dx][dy] = false;
            }
        }
    }

    public static boolean isValid(int x, int y) {
        return x >= 0 && x < R && y >= 0 && y < C;
    }
}