import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        char[] chars = input.readLine().toCharArray();
        int cnt = 0;
        for (int i = 6; i<chars.length; i++){
            if (chars[i] == '_') cnt++;
        }
        System.out.println(cnt*5+2+chars.length);
    }
}