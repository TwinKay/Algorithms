import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        boolean[] arr = new boolean[26];
        String s = input.readLine();
        char[] chars = s.toCharArray();
        for (char c : chars) {
            arr[c - 'A'] = true;
        }
        for (int i = 0; i < 26; i++) {
            if (!arr[i]) {
                System.out.println((char) (i + 'A'));
                break;
            }
        }
    }
}