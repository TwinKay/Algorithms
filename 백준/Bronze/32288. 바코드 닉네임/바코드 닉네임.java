import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int N;
    static String s;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        s = input.readLine();
        for (int i = 0; i < N; i++) {
            if (s.charAt(i) == 'I') {
                sb.append("i");
            }else{
                sb.append("L");
            }
        }
        System.out.println(sb);
    }
}