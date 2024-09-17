import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, K;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());

        visited = new boolean[100001];
        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{N, 0});
        visited[N] = true;

        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int cnt = cur[1];

            if (x == K) {
                System.out.println(cnt);
                break;
            }

            if (isValid(x*2) && !visited[x*2]) {
                deq.addFirst(new int[]{x*2, cnt});
                visited[x*2] = true;
            }

            if (isValid(x-1) && !visited[x-1]) {
                deq.addLast(new int[]{x-1, cnt+1});
                visited[x-1] = true;
            }

            if (isValid(x+1) && !visited[x+1]) {
                deq.addLast(new int[]{x+1, cnt+1});
                visited[x+1] = true;
            }
        }
    }

    public static boolean isValid(int x) {
        return x >= 0 && x <= 100000;
    }
}