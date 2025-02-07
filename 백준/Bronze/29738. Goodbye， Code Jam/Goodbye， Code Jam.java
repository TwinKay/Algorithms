import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(input.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i <= T; i++) {
            int N = Integer.parseInt(input.readLine());

            sb.append("Case #").append(i).append(": ");
            if (N <= 25) {
                sb.append("World Finals");
            } else if (N <= 1000) {
                sb.append("Round 3");
            } else if (N <= 4500) {
                sb.append("Round 2");
            } else {
                sb.append("Round 1");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}