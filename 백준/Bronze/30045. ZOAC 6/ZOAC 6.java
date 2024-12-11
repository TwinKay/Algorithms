import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        int res = 0;
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            char[] chars = s.toCharArray();
            for (int j = 0; j < chars.length-1; j++) {
                if ((chars[j] == '0' && chars[j+1] == '1') || (chars[j] == 'O' && chars[j+1] == 'I')) {
                    res ++;
                    break;
                }
            }
        }
        System.out.println(res);
    }
}
