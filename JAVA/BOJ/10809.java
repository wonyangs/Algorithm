import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String word = br.readLine();
        int[] index = new int[26];
        Arrays.fill(index, -1);

        for (int i = 0; i < word.length(); ++i) {
            int idx = word.charAt(i) - 'a';
            if (index[idx] == -1) {
                index[idx] = i;
            }
        }

        for (int i = 0; i < 26; ++i) {
            sb.append(index[i]).append(" ");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}