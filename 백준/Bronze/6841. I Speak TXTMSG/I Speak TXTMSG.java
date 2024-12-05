import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static HashMap hmap;

    public static void main(String[] args) throws IOException {
        hmap = new HashMap();
        hmap.put("CU","see you");
        hmap.put(":-)","I’m happy");
        hmap.put(":-(","I’m unhappy");
        hmap.put(";-)","wink");
        hmap.put(":-P","stick out my tongue");
        hmap.put("(~.~)","sleepy");
        hmap.put("TA","totally awesome");
        hmap.put("CCC","Canadian Computing Competition");
        hmap.put("CUZ","because");
        hmap.put("TY","thank-you");
        hmap.put("YW","you’re welcome");
        hmap.put("TTYL","talk to you later");

        while (true){
            String s = input.readLine();
            if (s.equals("TTYL")){
                System.out.println(hmap.get(s));
                break;
            }else{
                if (hmap.containsKey(s)){
                    System.out.println(hmap.get(s));
                }else{
                    System.out.println(s);
                }
            }
        }




    }
}