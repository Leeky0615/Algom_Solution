package 문자열.S5_AC_5430.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.*;

public class AC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        boolean right = false;

        boolean error=false;
        StringBuilder sb= new StringBuilder();;
        while (T-->0){
            String [] orders = br.readLine().split("");
            int n = Integer.parseInt(br.readLine());
            String [] numbers = br.readLine().split("");
            Deque<String> deque = new LinkedList<>();

            for(int i=0; i<numbers.length; i++){
                if(!numbers[i].equals("[") && !numbers[i].equals("]") &&
                        !numbers[i].equals(",") ){
                    deque.addFirst(numbers[i]);
                }
            }

            for(String s: orders){
                if(s.equals("R")){
                    if(right){
                        right=false;
                    }else{
                        right=true;
                    }
                }else{
                    if(deque.isEmpty()){
                       error=true;
                        break;
                    }else{
                        if(right){
                            deque.pollFirst();
                        }else{
                            deque.pollFirst();
                        }
                    }
                }
            }
            if(error){
                sb.append("error").append("\n");
            }else{
                if(right){
                    while (!deque.isEmpty()){
                        sb.append(deque.pollLast()).append(",");
                    }
                }else{
                    while (!deque.isEmpty()){
                        sb.append(deque.pollFirst()).append(",");
                    }
                }
            }
            sb.append("]");

        }
        System.out.println(sb);

    }
}
