import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static List<int[]> paths;
    static int[] parent;
    static long res = 0;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int v = Integer.parseInt(token.nextToken());
        int e = Integer.parseInt(token.nextToken());

        paths = new ArrayList<>();
        for (int i = 0; i < e; i++) {
            token = new StringTokenizer(input.readLine());
            paths.add(new int[]{Integer.parseInt(token.nextToken()), Integer.parseInt(token.nextToken()), Integer.parseInt(token.nextToken())});
        }
        paths.sort((o1, o2) -> {
            if (o1[2] == o2[2]) {
                if (o1[1] == o2[1]) {
                    return o1[0] - o2[0];
                }
                return o1[1] - o2[1];
            }
            return o1[2] - o2[2];
        });

        parent = new int[v+1];
        for (int i = 0; i< parent.length; i++) {
            parent[i] = i;
        }

        for (int[] path : paths) {
            int a = path[0];
            int b = path[1];
            int c = path[2];

            if (find(a)==find(b)) continue;
            union(a,b);
            res+=c;
        }

        System.out.println(res);
    }
    public static int find(int x){
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }
    public static void union(int x, int y){
        x = find(x);
        y = find(y);
        if (x == y) return;
        parent[y] = x;
    }
}