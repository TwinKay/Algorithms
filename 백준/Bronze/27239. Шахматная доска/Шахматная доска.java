import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        if (n%8!=0){
            sb.append((char)((n%8)+'a'-1));
            sb.append(n/8+1);
        }else{
            sb.append('h');
            sb.append(n/8);
        }
        System.out.println(sb);
    }
}

