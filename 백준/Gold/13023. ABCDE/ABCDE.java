import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n, m;
    static HashMap<Integer, List<Integer>> map;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());

        map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            token = new StringTokenizer(input.readLine());
            int p1 = Integer.parseInt(token.nextToken());
            int p2 = Integer.parseInt(token.nextToken());
            map.get(p1).add(p2);
            map.get(p2).add(p1);
        }

        visited = new boolean[n];
        boolean found = false;

        for (int i = 0; i < n; i++) {
            if (DFS(i, 1)) {
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    public static boolean DFS(int node, int cnt) {
        if (cnt == 5) {
            return true;
        }

        visited[node] = true;
        for (int neighbor : map.get(node)) {
            if (!visited[neighbor]) {
                if (DFS(neighbor, cnt+1)) {
                    return true;
                }
            }
        }

        visited[node] = false;
        return false;
    }
}