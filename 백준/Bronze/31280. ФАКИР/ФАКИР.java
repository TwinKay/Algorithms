import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int[] arr = new int[4];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < 4; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        Arrays.sort(arr);
        int res = 0;
        for (int i = 0; i < 4; i++) {
            if (i != 0) {
                res += arr[i];
            }
        }
        System.out.println(res+1);
    }
}