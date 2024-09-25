import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static int N,T;
    static String[] arr;
    static boolean find;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t=0; t<T; t++) {
            N = Integer.parseInt(input.readLine());
            arr = new String[N];
            for (int i = 0; i < N; i++) {
                arr[i] = input.readLine();
            }

            find = false;
            Trie trie = new Trie();
            for (int i = 0; i < N; i++) {
                if (find) break;
                trie.insert(String.valueOf(arr[i]));
            }
            if (find){
                sb.append("NO\n");
            }else{
                sb.append("YES\n");
            }
        }
        System.out.println(sb);
    }

    static class TrieNode{
        HashMap<Character, TrieNode> child;
        boolean isLast;

        TrieNode(){
            this.child = new HashMap<Character,TrieNode>();
            this.isLast = false;
        }
    }

    static class Trie{
        TrieNode root;

        Trie(){
            this.root = new TrieNode();
        }

        // insert
        public void insert(String str){
            TrieNode current = this.root;

            for (int i=0; i<str.length(); i++){
                if (current.isLast){
                    find = true;
                    return;
                }
                char alpha = str.charAt(i);

                if (!current.child.containsKey(alpha)){
                    current.child.put(alpha, new TrieNode());
                }

                current = current.child.get(alpha);
            }

            if (!current.child.isEmpty()) {
                find = true;
            }

            current.isLast = true;
        }
    }
}