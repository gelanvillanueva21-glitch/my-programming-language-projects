package DSA;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class Prac16HashMap {

    public static void main(String[] args) {
        HashMap<Integer, String> array = new HashMap<>();
        ConcurrentHashMap<Integer, String> arrays = new ConcurrentHashMap<>();
        
        array.put(213, "Hello");
        array.put(123, null);
        array.put(null, "gwapoko");
        for (Integer key : array.keySet()) {
            System.out.println(key + "\t" + array.get(key));
        }

        arrays.put(2134, "hello");
        arrays.put(9312, null);
        arrays.put(null, "kunichiway");
        System.out.println(arrays.values());
    }
}