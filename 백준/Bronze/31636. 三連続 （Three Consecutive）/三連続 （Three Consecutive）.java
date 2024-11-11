import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int N;
    static char[] chars;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        String s = input.readLine();
        chars = s.toCharArray();
        int cnt = 0;
        boolean isCon = false;
        for (int i = 0; i < N; i++) {
            if (chars[i] == 'o') {
                cnt++;
            }else{
                cnt = 0;
            }
            if (cnt == 3) {
                isCon = true;
                break;
            }
        }
        if(isCon){
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
    }
}