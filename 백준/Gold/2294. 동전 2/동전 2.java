import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,K;
    static int[] arr,dp;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(input.readLine());
        }
        Arrays.sort(arr);
        dp = new int[K+1];
        Arrays.fill(dp,Integer.MAX_VALUE/2);
        dp[0] = 0;

        for(int i=0; i<N; i++){
            for (int j=arr[i]; j<=K; j++){
                dp[j] = Math.min(dp[j], dp[j-arr[i]]+1);
            }
        }
        int res = dp[K];
        if (res == Integer.MAX_VALUE/2) {
            System.out.println(-1);
        }else{
            System.out.println(res);
        }
    }
}