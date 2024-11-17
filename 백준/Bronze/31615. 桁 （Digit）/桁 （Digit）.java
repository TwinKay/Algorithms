import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int a,b;

    public static void main(String[] args) throws IOException {
        a = Integer.parseInt(input.readLine());
        b = Integer.parseInt(input.readLine());
        a += b;
        String s = String.valueOf(a);
        System.out.println(s.length());
    }
}