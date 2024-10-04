import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int N;
    static List<Character> lst;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            char[] chars = s.toCharArray();
            lst = new ArrayList<Character>();
            lst.add(chars[0]);
            for (int j = 1; j < chars.length; j++) {
                if (lst.get(lst.size() - 1) != chars[j]) {
                    lst.add(chars[j]);
                }
            }
            for (Character c : lst) {
                sb.append(c);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}