import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N;
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
            return this.weight - o.weight;
        }
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(input.readLine());
            pq.add(new Edge(i, i, a));
        }

        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j=0; j<N; j++) {
                int weight = Integer.parseInt(token.nextToken());
                if (j>i){
                    pq.add(new Edge(i, j, weight));
                }
            }
        }

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        boolean[] isDig = new boolean[N];

        int res = 0;
        while (!pq.isEmpty()) {
            Edge edge = pq.poll();

            if (edge.a == edge.b){
                if (isDig[find(edge.a)]){
                    continue;
                }else{
                    isDig[find(edge.a)] = true;
                    res += edge.weight;
                }
            }else{
                if (isDig[find(edge.a)] && isDig[find(edge.b)]){
                    continue;
                }else if (isDig[find(edge.a)] && !isDig[find(edge.b)]){
                    union(edge.a, edge.b);
                    res += edge.weight;
                    isDig[find(edge.b)] = true;
                }else if (!isDig[find(edge.a)] && isDig[find(edge.b)]){
                    union(edge.a, edge.b);
                    res += edge.weight;
                    isDig[find(edge.a)] = true;
                }else{
                    if (find(edge.a) != find(edge.b)) {
                        union(edge.a, edge.b);
                        res += edge.weight;
                    }
                }
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