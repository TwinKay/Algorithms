import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        String s = "";
        while ((s = input.readLine()) != null) {
            char[] chars = s.toCharArray();
            for (int i = 0; i < chars.length; i++) {
                if (chars[i]=='i') chars[i]='e';
                else if (chars[i]=='e') chars[i]='i';
                else if (chars[i]=='I') chars[i]='E';
                else if (chars[i]=='E') chars[i]='I';
                sb.append(chars[i]);
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}


