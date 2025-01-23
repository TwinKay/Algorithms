import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static char[] chars;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        String s = input.readLine();
        chars = s.toCharArray();
        for (char c: chars) {
            if (c=='J') sb.append('O');
            else if (c=='O') sb.append('I');
            else sb.append('J');
        }
        System.out.println(sb);
    }
}