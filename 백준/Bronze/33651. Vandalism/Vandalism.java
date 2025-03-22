import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        char[] chars = new char[]{'U','A','P','C'};
        boolean[] bools = new boolean[4];
        String s = input.readLine();
        for (char c : s.toCharArray()) {
            if (c=='U'){
                bools[0] = true;
            }else if (c=='A'){
                bools[1] = true;
            }else if (c=='P'){
                bools[2] = true;
            }else if (c=='C'){
                bools[3] = true;
            }
        }
        for (int i = 0; i < 4; i++) {
            if (!bools[i]) sb.append(chars[i]);
        }
        System.out.println(sb.toString());
    }
}
