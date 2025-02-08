import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(input.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            String s = input.readLine();
            char[] chars = s.toCharArray();
            int a = 0; int b = 0;
            for (char c : chars) {
                if (c=='a') a++;
                else b++;
            }
            sb.append(Math.min(a,b)).append("\n");
        }
        System.out.println(sb);
    }
}