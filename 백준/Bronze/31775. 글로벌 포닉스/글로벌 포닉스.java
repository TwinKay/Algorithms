import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        boolean[] resArr = new boolean[3];
        for (int i=0; i<3; i++) {
            String s = input.readLine();
            char[] chars = s.toCharArray();
            if (chars[0]=='l'){
                resArr[0] = true;
            }else if (chars[0]=='k'){
                resArr[1] = true;
            }else if (chars[0]=='p'){
                resArr[2] = true;
            }
        }
        boolean isGlo = true;
        for (int i=0; i<3; i++) {
            if (!resArr[i]){
                isGlo = false;
                break;
            }
        }
        if (isGlo){
            System.out.println("GLOBAL");
        }else{
            System.out.println("PONIX");
        }
    }
}