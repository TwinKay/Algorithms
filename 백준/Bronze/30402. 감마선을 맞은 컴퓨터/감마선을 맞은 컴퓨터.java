import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer token;

    public static void main(String[] args) throws IOException {
        flag:
        for (int i=0; i<15; i++){
            token = new StringTokenizer(input.readLine());
            for (int j=0; j<15; j++){
                char c = token.nextToken().charAt(0);
                if (c == 'w'){
                    System.out.println("chunbae");
                    break flag;
                }else if (c == 'b'){
                    System.out.println("nabi");
                    break flag;
                }else if (c == 'g'){
                    System.out.println("yeongcheol");
                    break flag;
                }
            }
        }
    }
}