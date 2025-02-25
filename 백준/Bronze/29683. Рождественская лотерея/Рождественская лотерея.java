import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int N = Integer.parseInt(token.nextToken());
        int A = Integer.parseInt(token.nextToken());
        int[] arr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        int cnt =0;
        for (int i : arr) {
            cnt += i/A;
        }
        System.out.println(cnt);
    }
}