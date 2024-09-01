import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int n,m;
    static int[] cntArr;
    static List<Integer>[] graph;
    static List<Integer> save;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());

        graph = new List[n+1];
        for (int i=0; i<=n; i++){
            graph[i] = new ArrayList<>();
        }
        cntArr = new int[n+1];
        for (int i=0; i<=n; i++){
            cntArr[i] = 0;
        }

        for (int i=0; i<m; i++){
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            graph[a].add(b);
            cntArr[b]++;
        }

        Deque<Integer> queue = new LinkedList<>();
        for (int i=1; i<=n; i++){
            if (cntArr[i] == 0){
                queue.addLast(i);
            }
        }
        save = new ArrayList<>();
        while (!queue.isEmpty()){
            int a = queue.pollFirst();
            save.add(a);
            for (int b : graph[a]){
                cntArr[b]--;
                if (cntArr[b] == 0){
                    queue.addLast(b);
                }
            }
        }
        for (int s : save) {
            sb.append(s).append(" ");
        }
        System.out.println(sb);
    }
}