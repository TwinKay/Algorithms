import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int N;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        if (N%2==0){
            System.out.println("SciComLove");
        }else{
            System.out.println("evoLmoCicS");
        }
    }
}