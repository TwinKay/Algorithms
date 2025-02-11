import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(input.readLine());
        int a = Integer.parseInt(token.nextToken());
        int b = Integer.parseInt(token.nextToken());
        int c = Integer.parseInt(token.nextToken());

        int target = (a + c) / 2;

        int moveA = Math.abs(target - a);
        int moveC = Math.abs(target - c);

        System.out.println(moveA + moveC);
    }
}