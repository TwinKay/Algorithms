import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static long N,M;
    static long[] minutes;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Long.parseLong(token.nextToken());
        M = Long.parseLong(token.nextToken());
        minutes = new long[(int)N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            minutes[i] = Long.parseLong(token.nextToken());
        }
        Arrays.sort(minutes);

        long start = 1L; long end = 1000000000000L;
        long res = 0L;
        while (start <= end) {
            long mid = (start + end) / 2;
            long cnt = 0L;
            for (long minute : minutes) {
                cnt += mid/minute;
            }
            if (cnt >= M) {
                res = mid;
                end = mid - 1;
            }else{
                start = mid + 1;
            }
        }
        System.out.println(res);
    }
}
