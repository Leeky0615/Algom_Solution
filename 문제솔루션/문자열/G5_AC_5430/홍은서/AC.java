package 문자열.G5_AC_5430.홍은서;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class AC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        while(T --> 0){
            String[] orders= br.readLine().split("");
            int n = Integer.parseInt(br.readLine());
            String [] s = br.readLine().split("");
            Deque<Integer> deque = new LinkedList<>();
            boolean right = true; // 방향결정
             sb = new StringBuilder();

            for(String i: s){ // 덱에 숫자만 넣음
                if(!i.equals("[") && !i.equals("]") && !i.equals(",")){
                    deque.add(Integer.parseInt(i));
                }
            }

            for(String order: orders){ // 명령어 처리
                if(order.equals("R")){ // 뒤집기
                    // 여기서 방향만 바꿔줌ㅋ
                    if(right){
                        right = false;
                    }else{
                        right = true;
                    }

                }else{ // 맨 앞 제거
                    if(deque.isEmpty()){
                        System.out.println("error");
                        break;
                    }else{
                        if(right){
                            deque.pollFirst();
                        }else{
                            deque.pollLast();
                        }
                    }
                }
            }
            sb.append("[");
            if(deque.size()>0){
                if(right){
                    sb.append(deque.pollFirst());
                    while (!deque.isEmpty()){
                        sb.append(',').append(deque.pollFirst());
                    }
                }else{
                    sb.append(deque.pollLast());
                    while (!deque.isEmpty()){
                        sb.append(',').append(deque.pollLast());
                    }
                }
            }
            sb.append(']').append('\n');


        }

        System.out.println(sb);
    }
}
