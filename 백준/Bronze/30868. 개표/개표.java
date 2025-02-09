import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(input.readLine());
        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(input.readLine());
            for (int j = 0; j < n/5; j++) {
                sb.append("++++").append(" ");
            }
            for (int j = 0; j < n%5; j++) {
                sb.append("|");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
