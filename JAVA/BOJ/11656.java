import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
        List<String> arr = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for (int i=0; i < a.length() ; ++i) {
            arr.add(a.substring(i));
        }
        Collections.sort(arr);
        for (String c : arr) {
            sb.append(c).append("\n");
        }
        System.out.print(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}