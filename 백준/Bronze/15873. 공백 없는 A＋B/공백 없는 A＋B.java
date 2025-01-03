import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        char[] chars = input.readLine().toCharArray();
        int sum = 0;
        for (int i = chars.length - 1; i >= 0; i--) {
            if (chars[i]=='0'){
                sum += 10;
                i --;
            }else{
                sum += Integer.parseInt(String.valueOf(chars[i]));
            }
        }
        System.out.println(sum);
    }
}