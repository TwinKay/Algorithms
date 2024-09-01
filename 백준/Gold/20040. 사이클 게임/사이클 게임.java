import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n,m,res;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());
        res = 0;

        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (int i=1; i<=m; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            if (find(a)==find(b)){
                res = i;
                break;
            }
            union(a,b);
        }
        System.out.println(res);

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