import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int[] parent, cost;

    static int n, m, k;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());
        k = Integer.parseInt(token.nextToken());

        parent = new int[n + 1];
        cost = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        token = new StringTokenizer(input.readLine());
        for (int i = 1; i <= n; i++) {
            cost[i] = Integer.parseInt(token.nextToken());
        }

        for (int i = 0; i < m; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            union(a, b);
        }

        int totalCost = 0;
        boolean[] visited = new boolean[n + 1];

        for (int i = 1; i <= n; i++) {
            int root = find(i);
            if (!visited[root]) {
                totalCost += cost[root];
                visited[root] = true;
            }
        }

        if (totalCost <= k) {
            System.out.println(totalCost);
        } else {
            System.out.println("Oh no");
        }
    }

    public static int find(int x) {
        if (x==parent[x]) return x;
        return parent[x]=find(parent[x]);
    }

    public static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            if (cost[x] < cost[y]) {
                parent[y] = x;
            } else {
                parent[x] = y;
            }
        }
    }
}