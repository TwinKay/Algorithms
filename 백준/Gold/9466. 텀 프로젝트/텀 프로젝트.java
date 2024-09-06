import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N, cnt;
    static int[] graph;
    static boolean[] visited;
    static List<Integer> save;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(input.readLine());
            graph = new int[N+1];
            token = new StringTokenizer(input.readLine());
            for (int i = 1; i <= N; i++) {
                graph[i] = Integer.parseInt(token.nextToken());
            }
            visited = new boolean[N+1];

            //경로 저장 리스트 생성
            //dfs !visited 경우만 돌리기 매번 save 새로
            cnt = 0;
            for (int i = 1; i <= N; i++) {
                save = new ArrayList<Integer>();
                if (visited[i]) continue;
                dfs(i);
//            System.out.println("i = " + i);
//            System.out.println(cnt);
//            System.out.println(Arrays.toString(visited));
//            System.out.println(Arrays.toString(save.toArray()));
//            System.out.println("========================================");
            }

//        System.out.println(Arrays.toString(visited));
//        System.out.println("cnt = " + cnt);
            sb.append(N-cnt).append("\n");
        }
        System.out.println(sb);
    }
    public static void dfs(int x){
        if(visited[x]){
            if (save.contains(x)){
                int idx = save.indexOf(x);
//                System.out.println(idx);
                int len = save.size()-idx;
                if (len==1){
                    if (graph[x]==x){
                        cnt ++;
                    }
                }else{
                    cnt += len;
                }

                return;
            }else{
                return;
            }
        }
        save.add(x);
        visited[x] = true;
        dfs(graph[x]);
    }
}