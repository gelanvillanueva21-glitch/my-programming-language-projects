package DSA;
import java.util.*;

public class Prac6ArrayLinkList {
    public static void main(String[] args) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        ArrayList<Integer> arrayList = new ArrayList<>();

        long startTime;
        long endTime;
        long elapsedTime;

        for (int i = 0; i < 1000000; i++) {
            linkedList.add(i);
            arrayList.add(i);
        }

        linkedList.get(999999);
        startTime = System.nanoTime();
        endTime = System.nanoTime();
        elapsedTime = endTime - startTime;

        System.out.println("LinkedList:\t" + elapsedTime + " ns");

        arrayList.get(999999);
        startTime = System.nanoTime();
        endTime = System.nanoTime();
        elapsedTime = endTime - startTime;

        System.out.println("ArrayList:\t" + elapsedTime + " ns");
    }
}
