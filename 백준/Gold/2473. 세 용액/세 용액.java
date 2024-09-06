import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        long[] arr = new long[n];
        tokens = new StringTokenizer(input.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(tokens.nextToken());
        }
        Arrays.sort(arr);

        long resAbsSum = Long.MAX_VALUE;
        long resLeft = -1;
        long resRight = -1;
        long resBinary = -1;

        for (int left = 0; left < n-1; left++) {
            for (int right = left+1; right < n; right++) {
                long sumSide = arr[left] + arr[right];
                int binary = Arrays.binarySearch(arr, -(sumSide));

                if (binary < 0) {
                    binary = -(binary+1);
                }

                if (binary!=left && binary!=right && binary>=0 && binary<n) {
                    long sum = arr[left] + arr[right] + arr[binary];
                    sum = Math.abs(sum);
                    if (sum < resAbsSum) {
                        resAbsSum = sum;
                        resLeft = arr[left];
                        resRight = arr[right];
                        resBinary = arr[binary];
                    }
                }
                if (binary-1!=left && binary-1!=right && binary-1>=0 && binary-1<n) {
                    long sum = arr[left] + arr[right] + arr[binary-1];
                    sum = Math.abs(sum);
                    if (sum < resAbsSum) {
                        resAbsSum = sum;
                        resLeft = arr[left];
                        resRight = arr[right];
                        resBinary = arr[binary-1];
                    }
                }
                if (binary+1!=left && binary+1!=right && binary+1>=0 && binary+1<n) {
                    long sum = arr[left] + arr[right] + arr[binary+1];
                    sum = Math.abs(sum);
                    if (sum < resAbsSum) {
                        resAbsSum = sum;
                        resLeft = arr[left];
                        resRight = arr[right];
                        resBinary = arr[binary+1];
                    }
                }
            }
        }

        long[] res = {resLeft, resRight, resBinary};
        Arrays.sort(res);

        sb.append(res[0]).append(" ").append(res[1]).append(" ").append(res[2]);
        System.out.println(sb);
    }
}