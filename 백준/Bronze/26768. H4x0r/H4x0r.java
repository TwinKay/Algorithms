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
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        char[] chars = input.readLine().toCharArray();
        for (char c : chars) {
            if (c=='a') sb.append("4");
            else if (c=='e') sb.append("3");
            else if (c=='i') sb.append("1");
            else if (c=='o') sb.append("0");
            else if (c=='s') sb.append("5");
            else sb.append(c);
        }
        System.out.println(sb);
    }
}