import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n,m;
    static int[] parent;
    static List<int[]> paths;
    static int weights;
    static int maxWeight;
    
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());

        parent = new int[n+1];
        for (int i=0; i<n+1; i++) {
            parent[i] = i;
        }
        paths = new ArrayList<>();
        for (int i=0; i<m; i++){
            token = new StringTokenizer(input.readLine());
            paths.add(new int[]{Integer.parseInt(token.nextToken()), Integer.parseInt(token.nextToken()), Integer.parseInt(token.nextToken())});
        }
        Collections.sort(paths, (o1, o2)->{
            if (o1[2]==o2[2]){
                if (o1[0]==o2[0]){
                    return o1[1]-o2[1];
                }
                return o1[0]-o2[0];
            }
            return o1[2]-o2[2];
        });
        weights=0;
        maxWeight=0;
        for (int[] path: paths){
            int a = path[0];
            int b = path[1];
            int c = path[2];

            if (find(a)==find(b)) continue;
            union(a,b);
            weights += c;
            maxWeight = Math.max(maxWeight,c);
        }
        System.out.println(weights-maxWeight);
    }
    public static int find(int x){
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }
    public static void union(int x,int y){
        x = find(x);
        y = find(y);
        if(x==y) return;
        parent[y] = x;
    }
}