import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, M, S, E;
    static PriorityQueue<Edge> pq;
    static int[] parent;

    static class Edge implements Comparable<Edge> {
        int a, b, weight;

        Edge(int a, int b, int weight) {
            this.a = a;
            this.b = b;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return o.weight - this.weight;
        }
    }

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        S = Integer.parseInt(token.nextToken());
        E = Integer.parseInt(token.nextToken());

        pq = new PriorityQueue<>();
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(input.readLine());
            int u = Integer.parseInt(token.nextToken());
            int v = Integer.parseInt(token.nextToken());
            int w = Integer.parseInt(token.nextToken());
            pq.add(new Edge(u, v, w));
        }

        parent = new int[N+1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }

        int res = 0;
        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            if (find(edge.a) != find(edge.b)) {
                union(edge.a, edge.b);
            }
            if (find(S)==find(E)){
                res = edge.weight;
                break;
            }
        }
        System.out.println(res);
    }

    static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) parent[y] = x;
    }
}