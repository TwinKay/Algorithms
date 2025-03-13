import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static char[] chars;
    public static void main(String[] args) throws IOException {
        chars = input.readLine().toCharArray();
        int start = 0;
        int end = chars.length - 1;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] != '0') {
                start = i;
                break;
            }
        }
        for (int i = end; i >=0; i--){
            if (chars[i] != '0') {
                end = i;
                break;
            }
        }
        if (start <= end) {
            int cnt = 0;
            for (int i = start; i <= end; i++) {
                if (chars[i] == '0') cnt++;
            }
            System.out.println(cnt);
        }else{
            System.out.println(0);
        }

    }
}