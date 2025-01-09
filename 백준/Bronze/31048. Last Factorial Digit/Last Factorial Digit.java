import java.io.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb= new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        for (int i = 0; i < N; i++) {
            int a = Integer.parseInt(input.readLine());
            int res = 1;
            for (int j = 1; j <= a; j++) {
                res *= j;
            }
            sb.append(res%10).append("\n");
        }
        System.out.println(sb);
    }
}