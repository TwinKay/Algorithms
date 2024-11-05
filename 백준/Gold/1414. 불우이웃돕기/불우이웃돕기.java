import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
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
            char[] chars = input.readLine().toCharArray();
            for (int j = 0; j < N; j++) {
                if(chars[j]=='0') continue;
                int len;
                if (Character.isUpperCase(chars[j])) {
                    len = (int) chars[j] - 38;
                }else{
                    len = (int) chars[j] - 96;
                }
                pq.add(new Edge(i, j, len));
            }
        }
        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        int res = 0;
        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            if (find(edge.a) != find(edge.b)) {
                union(edge.a, edge.b);
            }else{
                res += edge.weight;
            }
        }
        if (isAllSame(parent)){
            System.out.println(res);
        }else{
            System.out.println(-1);
        }
    }
    
    static boolean isAllSame(int[] arr){
        int first = find(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if (first != find(arr[i])) return false;
        }
        return true;
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