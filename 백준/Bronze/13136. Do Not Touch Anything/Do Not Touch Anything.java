import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(input.readLine());

        long R = Long.parseLong(token.nextToken());
        long C = Long.parseLong(token.nextToken());
        long N = Long.parseLong(token.nextToken());

        long rows = (R+N-1) / N;
        long cols = (C+N-1) / N;

        System.out.println(rows * cols);
    }
}