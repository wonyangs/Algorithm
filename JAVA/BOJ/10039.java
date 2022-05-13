import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int hap = 0;
        for (int i = 0; i < 5; ++i) {
            int point = Integer.parseInt(br.readLine());
            if (point < 40) {
                hap += 40;
                continue;
            }
            hap += point;
        }
        System.out.println(hap / 5);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}