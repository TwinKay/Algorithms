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

        cntArr = new int[n+1];
        graph = new List[n+1];
        for (int i=0; i<n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i=0; i<m; i++){
            token = new StringTokenizer(input.readLine());
            int eachN = Integer.parseInt(token.nextToken());
            int[] tempArr = new int[eachN];
            for (int j=0; j<eachN; j++){
                tempArr[j] = Integer.parseInt(token.nextToken());
            }
            for (int j=0; j<eachN-1; j++){
                int a = tempArr[j];
                int b = tempArr[j+1];

                graph[a].add(b);
                cntArr[b]++;
            }
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
        if (save.size()==n){
            for (int s : save){
                sb.append(s).append("\n");
            }
        }else{
            sb.append(0);
        }
        System.out.println(sb);
    }
}