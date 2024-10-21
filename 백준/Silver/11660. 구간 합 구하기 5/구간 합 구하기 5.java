import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M;
    static int[][] arr, dp;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        arr = new int[N+1][N+1];
        dp = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 1; j <= N; j++) {
                arr[i][j] = Integer.parseInt(token.nextToken());
                dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j];
            }
        }
        for (int i=0; i<M; i++){
            token = new StringTokenizer(input.readLine());
            int x1 = Integer.parseInt(token.nextToken());
            int y1 = Integer.parseInt(token.nextToken());
            int x2 = Integer.parseInt(token.nextToken());
            int y2 = Integer.parseInt(token.nextToken());
            sb.append(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]).append("\n");
        }
        System.out.println(sb);
    }
}