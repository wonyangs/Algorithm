import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
                
        h += 23;
        m += 15;
        h += m / 60;
        m %= 60;
        h %= 24;
        System.out.println(h + " " + m);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}