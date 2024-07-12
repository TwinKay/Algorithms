import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;

	public static void main(String[] args) throws IOException {
		
		int T = Integer.parseInt(input.readLine());
		
		for (int t=0; t<T; t++) {
			tokens = new StringTokenizer(input.readLine());
			int a = (Integer.parseInt(tokens.nextToken()));
			int b = (Integer.parseInt(tokens.nextToken()));
			
			output.append("Case #").append(t+1).append(": ").append(a).append(" + ").append(b).append(" = ").append(a+b).append("\n");
		}
		System.out.println(output);
	}

}