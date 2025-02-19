import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        int cnt = 0;
        for (int i = 0; i < 3; i++) {
            token = new StringTokenizer(input.readLine());
            int cnt7 = 0;
            for (int j = 0; j < N; j++) {
                if (Integer.parseInt(token.nextToken()) == 7) {
                    cnt7++;
                }
            }
            if (cnt7 >0) {
                cnt++;
            }
        }
        if (cnt==3){
            System.out.println("777");
        }else{
            System.out.println("0");
        }
    }
}
