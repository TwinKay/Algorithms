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
    static int N,K;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        String s = input.readLine();

        Deque<Character> deq = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            while (!deq.isEmpty() && K > 0 && deq.peekLast() < c) {
                deq.pollLast();
                K--;
            }
            deq.addLast(c);
        }

        while (deq.size() > K) {
            sb.append(deq.pollFirst());
        }
        System.out.println(sb);
    }
}