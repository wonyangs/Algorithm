import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        HashSet<String> set = new HashSet<>();

        for (int i = 1; i <= word.length(); ++i) {
            for (int j = 0; j < i; ++j) {
                set.add(word.substring(j, i));
            }
        }
        
        System.out.println(set.size());
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}