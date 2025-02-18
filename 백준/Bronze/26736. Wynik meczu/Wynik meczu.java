import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        char[] chars = input.readLine().toCharArray();
        int cntA = 0; int cntB = 0;
        for (char c : chars) {
            if (c=='A') cntA++;
            else cntB++;
        }
        sb.append(cntA).append(" : ").append(cntB);
        System.out.println(sb);
    }
}