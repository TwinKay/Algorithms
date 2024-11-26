import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int a=0,b=0,c=0;
        token = new StringTokenizer(input.readLine());
        for (int i=0; i<5; i++){
            if(i==0){
                a = Integer.parseInt(token.nextToken());
            }else if(i==2){
                b = Integer.parseInt(token.nextToken());
            }else if(i==4){
                c = Integer.parseInt(token.nextToken());
            }else{
                String trash = token.nextToken();
            }
        }
        if (a+b==c){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}