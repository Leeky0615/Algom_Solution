package 문자열.S4_듣보잡_1764.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.StringTokenizer;
// 🔑 hahsset 이용
public class 듣보잡 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        HashSet<String> hs = new HashSet<String>();
        ArrayList<String> al = new ArrayList<>();

        while (N --> 0){
            hs.add(br.readLine());
        }
        while (M --> 0){
            String name = br.readLine();
            if(hs.contains(name)){
                al.add(name);
            }
        }
        Collections.sort(al);
        System.out.println(al.size());
        for(String s: al){
            System.out.println(s);
        }

    }
}
