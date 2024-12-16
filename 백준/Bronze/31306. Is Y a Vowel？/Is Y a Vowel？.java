import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        char[] chars = s.toCharArray();
        int voCnt = 0;
        int yCnt = 0;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == 'a' || chars[i] == 'e' || chars[i] == 'i' || chars[i] == 'o' || chars[i] == 'u') {
                voCnt++;
            }
            else if (chars[i] == 'y') {
                yCnt++;
            }
        }
        sb.append(voCnt).append(" ").append(voCnt+yCnt);
        System.out.println(sb);
    }
}