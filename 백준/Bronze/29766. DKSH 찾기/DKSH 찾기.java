import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static char[] chars;
    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        chars = s.toCharArray();
        int cnt = 0;
        for (int i=0; i<chars.length-3; i++) {
            if (chars[i]=='D'&&chars[i+1]=='K'&&chars[i+2]=='S'&&chars[i+3]=='H') {
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}