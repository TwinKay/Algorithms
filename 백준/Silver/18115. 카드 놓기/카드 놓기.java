import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static int[] order;
    static Deque<Integer> deq;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        order = new int[N];
        for (int i = N-1; i >= 0; i--) {
            order[i] = Integer.parseInt(token.nextToken());
        }
        deq = new ArrayDeque<>();
        for (int i=1; i<=N; i++) {
            int skill = order[i-1];
            if (skill==1) deq.addLast(i);
            else if (skill==3) deq.addFirst(i);
            else{
                int temp = deq.pollLast();
                deq.addLast(i);
                deq.addLast(temp);
            }
        }
        while (!deq.isEmpty()) {
            sb.append(deq.pollLast()).append(" ");
        }
        System.out.println(sb);



    }
}