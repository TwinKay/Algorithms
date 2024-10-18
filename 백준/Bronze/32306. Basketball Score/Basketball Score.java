import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int a,b,c,d,e,f,sco1,sco2;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        a = Integer.parseInt(token.nextToken());
        b = Integer.parseInt(token.nextToken());
        c = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        d = Integer.parseInt(token.nextToken());
        e = Integer.parseInt(token.nextToken());
        f = Integer.parseInt(token.nextToken());
        sco1 = a+2*b+3*c;
        sco2 = d+2*e+3*f;
        if (sco1>sco2){
            System.out.println(1);
        }else if (sco1<sco2){
            System.out.println(2);
        }else{
            System.out.println(0);
        }
    }
}