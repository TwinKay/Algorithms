import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        String s = input.readLine();
        char[] chars = s.toCharArray();
        int oCnt = 0;
        for (char c : chars) {
            if (c == 'o') oCnt++;
        }
        System.out.println(2*N-oCnt);
    }
}