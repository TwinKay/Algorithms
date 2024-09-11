import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(input.readLine());
        }
        Arrays.sort(arr);
        int cutNum = (int) Math.round(N*0.15);
        int sum = 0;
        for (int i = cutNum; i<N-cutNum; i++) {
            sum += arr[i];
        }
        double res = (double) sum /(N-cutNum*2);
        System.out.println(Math.round(res));

    }
}