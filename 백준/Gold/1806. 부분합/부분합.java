import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int n,m;
    static int[] arr;


    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        n = Integer.parseInt(token.nextToken());
        m = Integer.parseInt(token.nextToken());
        arr = new int[n];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        int minLen = Integer.MAX_VALUE;
        int left = 0, right = 0;
        int sum = 0;

        while (true) {
            if (sum >= m) {
                minLen = Math.min(minLen, right - left);
                sum -= arr[left++];
            } else if (right == n) {
                break;
            } else {
                sum += arr[right++];
            }
        }
        if (minLen == Integer.MAX_VALUE) {
            System.out.println(0);
        }else{
            System.out.println(minLen);
        }
    }
}