import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        char[] chars = s.toCharArray();
        int cnt = 0;
        for (char c : chars) {
            if (c=='B'){
                cnt += 2;
            }
            else if (c=='A'||c=='a'||c=='b'||c=='D'||c=='e'||c=='d'||c=='g'||c=='o'||c=='O'||c=='P'||c=='p'||c=='Q'||c=='q'||c=='R'||c=='@') {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}