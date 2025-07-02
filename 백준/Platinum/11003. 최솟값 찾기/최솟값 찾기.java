import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int N = Integer.parseInt(token.nextToken());
        int L = Integer.parseInt(token.nextToken());

        int[] arr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }

        Deque<Integer> deq = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            while (!deq.isEmpty() && arr[deq.peekLast()] > arr[i]) {
                deq.pollLast();
            }

            deq.addLast(i);

            if (deq.peekFirst() < i-L+1) {
                deq.pollFirst();
            }

            sb.append(arr[deq.peekFirst()]).append(" ");
        }

        System.out.println(sb);
    }
}