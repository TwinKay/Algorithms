import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        char[] chars = input.readLine().toCharArray();
        char mainC = chars[0];
        boolean isFind = false;
        for (int i = 1; i < N; i++) {
            if (mainC != chars[i]) {
                isFind = true;
            }
        }
        if (isFind) System.out.println("No");
        else System.out.println("Yes");
    }
}