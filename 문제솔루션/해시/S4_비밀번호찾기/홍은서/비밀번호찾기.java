package 해시.S4_비밀번호찾기.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 비밀번호찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String,String> map = new HashMap<>();

        while (N-->0){ // 주소와 비번 받기
            StringTokenizer st2 = new StringTokenizer(br.readLine()," ");
            String site = st2.nextToken();
            String pw = st2.nextToken();
            map.put(site,pw);
        }
        while (M-->0){
            String target = br.readLine();
            System.out.println(map.get(target));
        }
    }
}
