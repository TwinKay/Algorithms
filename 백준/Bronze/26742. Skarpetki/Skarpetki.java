import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int cntB = 0;
        int cntC = 0;
        char[] chars = input.readLine().toCharArray();
        for (char c: chars) {
            if (c == 'B') cntB++;
            else if (c == 'C') cntC++;
        }
        System.out.println(cntB/2+cntC/2);
    }
}