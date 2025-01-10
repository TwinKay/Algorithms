import java.io.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb= new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        for (int i = 1; i <= N; i++) {
            sb.append(i).append(" ");
            if (i%6==0){
                sb.append("Go! ");
            }
        }
        if (N%6!=0) sb.append("Go! ");
        System.out.println(sb);
    }
}
