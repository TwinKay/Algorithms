import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n;
    static double[][] starIdx;
    static List<double[]> paths;
    static int[] parent;
    static double res;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(input.readLine());

        starIdx = new double[n+1][2];
        for(int i = 1; i <= n; i++) {
            token = new StringTokenizer(input.readLine());
            starIdx[i][0] = Double.parseDouble(token.nextToken());
            starIdx[i][1] = Double.parseDouble(token.nextToken());
        }
        paths = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            for (int j = i+1; j <= n; j++) {
                paths.add(new double[]{i, j, Math.sqrt(Math.pow(starIdx[i][0]-starIdx[j][0],2)+Math.pow(starIdx[i][1]-starIdx[j][1],2))});
            }
        }
        Collections.sort(paths, (o1,o2)->{
            if(o1[2]==o2[2]){
                if(o1[0]==o2[0]){
                    return (int) (o1[1]-o2[1]);
                }
                return (int) (o1[0]-o2[0]);
            }
            return (int) (o1[2]-o2[2]);
        });

        parent = new int[n+1];
        for(int i = 1; i <= n; i++) {
            parent[i] = i;
        }
        res = 0.0;

        for (double[] path : paths) {
            int a = (int) path[0];
            int b = (int) path[1];
            double c = path[2];

            if (find(a)==find(b)) continue;
            union(a,b);
            res += c;
        }
        System.out.println(String.format("%.2f",res));

    }
    public static int find(int x){
        if(parent[x]==x) return x;
        return parent[x] = find(parent[x]);
    }
    public static void union(int x, int y){
        x = find(x);
        y = find(y);
        if (x==y) return;
        parent[y]=x;
    }
}