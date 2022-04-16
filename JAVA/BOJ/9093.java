import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < T; ++i) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                sb.append(new StringBuffer(st.nextToken()).reverse().toString()).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}