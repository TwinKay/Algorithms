import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M;
    static List<Integer>[] graph;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        M = Integer.parseInt(input.readLine());
        graph = new List[N+1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 1; i <= N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 1; j <= N; j++) {
                int temp = Integer.parseInt(token.nextToken());
                if (temp==1) graph[i].add(j);
            }
        }
        parent = new int[N+1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }
        for (int i = 1; i <= N; i++) {
            List<Integer> neighbours = graph[i];
            for (int n : neighbours) {
                union(n, i);
            }
        }
        int[] cities = new int[M];
        token = new StringTokenizer(input.readLine());
        for (int i=0; i<M; i++){
            cities[i] = Integer.parseInt(token.nextToken());
        }
        int cnt = 1;
        int groupId = find(cities[0]);
        for (int i = 1; i < M; i++) {
            int id = find(cities[i]);
            if (id==groupId) cnt++;
        }
        if (cnt==M) System.out.println("YES");
        else System.out.println("NO");
    }
    public static int find(int x){
        if (x==parent[x]) return x;
        return parent[x] = find(parent[x]);
    }
    public static void union(int x,int y){
        x = find(x);
        y = find(y);
        parent[y] = x;
    }
}