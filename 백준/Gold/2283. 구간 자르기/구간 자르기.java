import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int[] imos;
    static int[] sumArr;

    static int N, K;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());

        imos = new int[1000001];
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            imos[a]++;
            imos[b]--;
        }

        sumArr = new int[1000001];
        int now = 0;
        for (int i = 0; i < 1000001; i++) {
            now += imos[i];
            sumArr[i] = now;
        }

        int left = 0, right = 0;
        long currentSum = 0;
        boolean isFound = false;

        while (right < 1000001) {
            while (right < 1000001 && currentSum < K) {
                currentSum += sumArr[right];
                right++;
            }

            while (left < right && currentSum > K) {
                currentSum -= sumArr[left];
                left++;
            }

            if (currentSum == K) {
                isFound = true;
                sb.append(left).append(" ").append(right);
                System.out.println(sb);
                return;
            }
        }
        if (!isFound) {
            System.out.println("0 0");
        }
    }
}