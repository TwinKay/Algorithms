import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        char[] chars = s.toCharArray();
        int cnt = 0;
        for (char c : chars) {
            if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}