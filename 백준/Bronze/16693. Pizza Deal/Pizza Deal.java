import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        int A1 = Integer.parseInt(token.nextToken());
        int P1 = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        int R1 = Integer.parseInt(token.nextToken());
        int P2 = Integer.parseInt(token.nextToken());

        double sliceValue = (double) A1 / P1;
        double wholeValue = (Math.PI * R1 * R1) / P2;
        if (wholeValue > sliceValue) {
            System.out.println("Whole pizza");
        } else {
            System.out.println("Slice of pizza");
        }
    }
}
