import java.io.*;
import java.util.*;

public class Main{

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

        int sum = 0;
        for(int i=0; i<4; i++) {
            st = new StringTokenizer(br.readLine());
            sum += Integer.parseInt(st.nextToken());
        }

        br.close();

        System.out.println((int)(sum/60));
        System.out.println(sum%60);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}