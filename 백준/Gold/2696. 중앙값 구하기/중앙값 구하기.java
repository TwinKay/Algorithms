import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int T, M;
    static PriorityQueue<Integer> pqLeft, pqRight;
    static List<Integer> medians;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t = 0; t < T; t++) {
            M = Integer.parseInt(input.readLine());
            pqLeft = new PriorityQueue<>((a, b) -> b - a);
            pqRight = new PriorityQueue<>();
            medians = new ArrayList<>();

            int cnt = 0;
            for (int i = 0; i < (M+9)/10; i++) {
                token = new StringTokenizer(input.readLine());
                while (token.hasMoreTokens()) {
                    int num = Integer.parseInt(token.nextToken());

                    if (pqLeft.isEmpty() || num <= pqLeft.peek()) {
                        pqLeft.add(num);
                    } else {
                        pqRight.add(num);
                    }

                    if (pqLeft.size() > pqRight.size()+1) {
                        pqRight.add(pqLeft.poll());
                    } else if (pqRight.size() > pqLeft.size()) {
                        pqLeft.add(pqRight.poll());
                    }

                    if (++cnt%2 == 1) {
                        medians.add(pqLeft.peek());
                    }
                }
            }

            sb.append(medians.size()).append("\n");
            for (int i = 0; i < medians.size(); i++) {
                sb.append(medians.get(i)).append(" ");
                if ((i+1)%10 == 0) sb.append("\n");
            }
            if (medians.size()%10 != 0) sb.append("\n");
        }

        System.out.print(sb);
    }
}
