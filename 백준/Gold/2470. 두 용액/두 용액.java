import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        int[] arr = new int[n];
        tokens = new StringTokenizer(input.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(tokens.nextToken());
        }
        Arrays.sort(arr);

        int left = 0;
        int right = n-1;
        int resAbsSum = Integer.MAX_VALUE;
        int resLeft = -1;
        int resRight = -1;

        while (left < right) {
            int sum = arr[left] + arr[right];
            int absSum = Math.abs(sum);

            if (absSum < resAbsSum) {
                resAbsSum = absSum;
                resLeft = arr[left];
                resRight = arr[right];
            }

            if (sum < 0) {
                left ++;
            } else {
                right --;
            }
        }

        System.out.println(resLeft + " " + resRight);
    }
}