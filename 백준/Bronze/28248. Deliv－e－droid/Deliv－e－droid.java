import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int a = Integer.parseInt(input.readLine());
        int b = Integer.parseInt(input.readLine());
        int res = a*50 - b*10;
        if (a>b) res += 500;
        System.out.println(res);
    }
}