import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n,r,q;
    static HashMap<Integer,List<Integer>> graph;
    static boolean[] visited;
    static int[] cntArr;


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        r = Integer.parseInt(token.nextToken());
        q = Integer.parseInt(token.nextToken());

        graph = new HashMap<>();
        for (int i = 0; i <= n; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int i = 0; i<n-1; i++){
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        cntArr = new int[n+1];
        visited = new boolean[n+1];
        subCnt(r);
        for(int i=0; i<q; i++){
            int queryNode = Integer.parseInt(input.readLine());
            sb.append(cntArr[queryNode]).append("\n");
        }
        System.out.println(sb);
    }
    public static int subCnt(int x) {
        visited[x] = true;
        int cnt = 1;
        for (int a : graph.get(x)) {
            if (!visited[a]) {
                cnt += subCnt(a);
            }
        }
        cntArr[x] = cnt;
        return cnt;
    }
}