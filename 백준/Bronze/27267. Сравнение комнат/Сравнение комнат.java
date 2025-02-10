import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token =  new StringTokenizer(input.readLine());
        int a = Integer.parseInt(token.nextToken())*Integer.parseInt(token.nextToken());
        int b = Integer.parseInt(token.nextToken())*Integer.parseInt(token.nextToken());
        if (a>b){
            System.out.println("M");
        }else if (a<b){
            System.out.println("P");
        }else{
            System.out.println("E");
        }
    }
}