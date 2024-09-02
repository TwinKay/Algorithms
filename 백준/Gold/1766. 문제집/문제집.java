import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n,m;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());

        int[] cntArr = new int[n+1];
        List<Integer>[] graph = new List[n+1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i=0; i<m; i++){
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());

            graph[a].add(b);
            cntArr[b]++;
        }
        List<Integer> res = new ArrayList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i=1; i<=n; i++){
            if (cntArr[i] == 0) pq.add(i);
        }
        while (!pq.isEmpty()){
            int a = pq.poll();
            res.add(a);
            for (int b : graph[a]){
                cntArr[b]--;
                if (cntArr[b] == 0) pq.add(b);
            }
        }
        for (int i:res){
            sb.append(i).append(" ");
        }
        System.out.println(sb);
    }
}