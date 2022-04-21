import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(br.readLine());

        int sec = (b + c) % 60;
        int min = (a + (b + c) / 60) % 24;
        System.out.println(min + " " + sec);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}