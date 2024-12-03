import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        char[] chars= input.readLine().toCharArray();
        for (int i = N-5; i < N; i++) {
            sb.append(chars[i]);
        }
        System.out.println(sb);
    }
}