import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static long ang, res;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        res = 0L;
        ang = 0L;
        for (int i = 0; i < N; i++) {
            if (arr[i]==0){
                ang--;
            }else{
                ang++;
            }
            res += ang;
        }
        System.out.println(res);
    }
}