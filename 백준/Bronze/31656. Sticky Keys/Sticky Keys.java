import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        char[] chars = s.toCharArray();
        List<Character> charList = new ArrayList<>();
        charList.add(chars[0]);
        for (int i = 1; i < chars.length; i++) {
            if (chars[i] != charList.get(charList.size()-1)) {
                charList.add(chars[i]);
            }
        }
        for (char c : charList) {
            sb.append(c);
        }
        System.out.println(sb);
    }
}