import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        Long[] arr = new Long[3];
        for (int i = 0; i < 3; i++) {
            arr[i] = Long.parseLong(token.nextToken());
        }
        Arrays.sort(arr);
        System.out.println(arr[1]);
    }
}