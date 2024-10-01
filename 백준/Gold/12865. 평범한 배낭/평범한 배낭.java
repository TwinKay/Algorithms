import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,K;
    static int[][] dp;
    static int[] weights, values;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());

        weights = new int[N+1];
        values = new int[N+1];
        for (int i = 1; i <= N; i++) {
            token = new StringTokenizer(input.readLine());
            weights[i] = Integer.parseInt(token.nextToken());
            values[i] = Integer.parseInt(token.nextToken());
        }

        dp = new int[N+1][K+1];

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                if(j<weights[i]){
                    dp[i][j] = dp[i-1][j];
                }else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i]);
                }
            }
        }
        System.out.println(dp[N][K]);

    }
}