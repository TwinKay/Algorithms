import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokens;
    private static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(input.readLine());
        for (int tc=1; tc<testCase+1; tc++) {
            sb = new StringBuilder();
            sb.append("#").append(tc).append(" ");
            tokens = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(tokens.nextToken());
            int b = Integer.parseInt(tokens.nextToken());
            int c = Integer.parseInt(tokens.nextToken());

            if (a<1 || b<2 || c<3) {
                sb.append(-1);
            } else {
                int cnt = 0;
                if (b >= c) {
                    cnt += b-c+1;
                    b = c-1;
                }
                if (a >= b) {
                    cnt += a-b+1;
                    a = b-1;
                }
                sb.append(cnt);
            }
            System.out.println(sb.toString());
        }
    }
}