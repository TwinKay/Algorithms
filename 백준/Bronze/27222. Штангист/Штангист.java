import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        int[] arr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        int res = 0;
        for (int i = 0; i < N; i++) {
            token = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(token.nextToken());
            int b = Integer.parseInt(token.nextToken());
            if (arr[i]==1 && b>a){
                res += b-a;
            }
        }
        System.out.println(res);
    }
}