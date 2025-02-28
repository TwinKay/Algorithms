import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        int M = Integer.parseInt(input.readLine());

        if (N>=3 && M<=4){
            sb.append("TroyMartian\n");
        }
        if (N<=6 && M>=2){
            sb.append("VladSaturnian\n");
        }
        if (N<=2 && M<=3){
            sb.append("GraemeMercurian\n");
        }
        System.out.println(sb);

    }
}