import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input =  new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int A,B,N,M;
    static int[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        A = Integer.parseInt(token.nextToken());
        B = Integer.parseInt(token.nextToken());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new int[100001];
        visited = new boolean[100001];
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{N,0});
        visited[N] = true;
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int cnt = cur[1];
            if (x==M){
                System.out.println(cnt);
                break;
            }
            if(isValid(x-1)&&!visited[x-1]){
                deq.addLast(new int[]{x-1,cnt+1});
                visited[x-1] = true;
            }
            if(isValid(x+1) && !visited[x+1]){
                deq.addLast(new int[]{x+1,cnt+1});
                visited[x+1] = true;
            }
            if(isValid(x-A) && !visited[x-A]){
                deq.addLast(new int[]{x-A,cnt+1});
                visited[x-A] = true;
            }
            if(isValid(x-B) && !visited[x-B]){
                deq.addLast(new int[]{x-B,cnt+1});
                visited[x-B] = true;
            }
            if(isValid(x+A) && !visited[x+A]){
                deq.addLast(new int[]{x+A,cnt+1});
                visited[x+A] = true;
            }
            if(isValid(x+B) && !visited[x+B]){
                deq.addLast(new int[]{x+B,cnt+1});
                visited[x+B] = true;
            }
            if(isValid(x*A) && !visited[x*A]){
                deq.addLast(new int[]{x*A,cnt+1});
                visited[x*A] = true;
            }
            if(isValid(x*B) && !visited[x*B]){
                deq.addLast(new int[]{x*B,cnt+1});
                visited[x*B] = true;
            }
        }

    }
    public static boolean isValid(int x){
        return x>=0 && x<=100000;
    }
}