import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int N,K;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        arr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }

        int left = 0; int right = 0;
        int cntOdd = 0;
        if (arr[right] % 2 == 1) cntOdd++;
        int max = 1-cntOdd;
        while (right < N-1) {
            if (cntOdd < K || arr[right+1] % 2 == 0) {
                right++;
                if (arr[right] % 2 == 1) {
                    cntOdd++;
                }
            } else {
                boolean isOdd;
                if (arr[left] % 2 == 1) isOdd = true;
                else isOdd = false;

                left++;
                if (isOdd) cntOdd--;
            }
            max = Math.max(max, right-left+1-cntOdd);
        }
        System.out.println(max);
    }
}