package DSA;
import java.util.*;


public class Prac4LinkedList {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();

        list.offer("A");
        list.add("B");
        list.add("C");
        list.add("D");
        list.add("E");
        list.add(4, "DA");
        System.out.println(list.getFirst());
        System.out.println(list.getLast());
        System.out.println(list.peekFirst());
        System.out.println(list.peekLast());
        list.addFirst("0");
        list.addLast("ZZ");
        System.out.println(list);
        list.removeFirst();
        list.removeLast();
        System.out.println(list);

        /*
        LinkedList<Integer> list = new LinkedList<>();
        list.add(10);       // 10 → null
        list.add(20);       // 10 → 20 → null
        list.add(30);       // 10 → 20 → 30 → null

        list.addFirst(5);   // 5 → 10 → 20 → 30 → null
        list.removeFirst(); // removes 5
        list.getLast();     // 30
        */
        
    }
}
