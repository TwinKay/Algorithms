import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static boolean[] visited;
    static Map<Integer, List<int[]>> map;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());

        map = new HashMap<>();
        for (int i = 0; i < N-1; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            int l = Integer.parseInt(token.nextToken());

            if (map.containsKey(a)) {
                map.get(a).add(new int[]{b, l});
            }else{
                List<int[]> list = new ArrayList<>();
                list.add(new int[]{b, l});
                map.put(a,list);
            }
            if (map.containsKey(b)) {
                map.get(b).add(new int[]{a,l});
            }else{
                List<int[]> list = new ArrayList<>();
                list.add(new int[]{a,l});
                map.put(b,list);
            }
        }
        for (int i = 0; i < M; i++) {
            token = new StringTokenizer(input.readLine());
            findLen(Integer.parseInt(token.nextToken()), Integer.parseInt(token.nextToken()));
        }
        System.out.println(sb);

    }
    public static void findLen(int start, int end){
        visited = new boolean[N+1];

        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{start,0});
        visited[start] = true;
        flag:
        while(!deq.isEmpty()){
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int totalLen = cur[1];

            List<int[]> list = map.get(x);
            for (int[] node : list) {
                int next = node[0];
                int len = node[1];

                if(!visited[next]){
                    deq.addLast(new int[]{next,totalLen+len});
                    visited[next] = true;
                    if(next==end){
                        sb.append(totalLen+len).append("\n");
                        break flag;
                    }
                }
            }
        }
    }
}