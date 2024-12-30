import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 0; t < T; t++) {
            token = new StringTokenizer(input.readLine());
            double A1 = Double.parseDouble(token.nextToken());
            double P1 = Double.parseDouble(token.nextToken());
            token = new StringTokenizer(input.readLine());
            double R1 = Double.parseDouble(token.nextToken());
            double P2 = Double.parseDouble(token.nextToken());

            double sliceValue = A1/P1;
            double wholeValue = (Math.PI*R1*R1)/P2;

            if (wholeValue>sliceValue) {
                sb.append("Whole pizza\n");
            } else {
                sb.append("Slice of pizza\n");
            }
        }
        System.out.println(sb);
    }
}