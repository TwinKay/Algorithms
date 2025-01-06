import java.io.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        char[] chars1 = input.readLine().toCharArray();
        char[] chars2 = input.readLine().toCharArray();
        int res = 0;
        for (int i = 0; i < N; i++) {
            if (chars1[i] != chars2[i]) res++;
        }
        System.out.println(res);
    }
}