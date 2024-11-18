import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        flag:
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            char[] chars = s.toCharArray();
            for (char c : chars) {
                if (c == 'S'){
                    System.out.println(s);
                    break flag;
                }
            }
        }
    }
}