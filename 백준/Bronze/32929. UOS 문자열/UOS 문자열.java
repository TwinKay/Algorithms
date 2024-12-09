import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(input.readLine());
        N = N%3;
        if(N==0){
            System.out.println("S");
        }else if(N==1){
            System.out.println("U");
        }else{
            System.out.println("O");
        }
    }
}