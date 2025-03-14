import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static long N;
    public static void main(String[] args) throws IOException {
        N = Long.parseLong(input.readLine());
        double d = Math.sqrt(N);
        System.out.println(d*4);

    }
}