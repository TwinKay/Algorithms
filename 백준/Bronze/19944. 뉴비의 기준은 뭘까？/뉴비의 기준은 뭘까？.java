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
        int M = Integer.parseInt(token.nextToken());

        if (M==1 || M==2) System.out.println("NEWBIE!");
        else if (M<=N) System.out.println("OLDBIE!");
        else System.out.println("TLE!");
    }
}