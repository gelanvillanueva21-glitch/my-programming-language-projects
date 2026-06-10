package DSA;
import java.util.*;

public class Prac15HashTables {

    public static void main(String[] args) {
        Hashtable<Integer, String> tables = new Hashtable<>();
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter How Many Student To Add");
        System.out.print("> ");
        int num = sc.nextInt();

        while (num >= 1) {
            System.out.print("Enter A Number: ");
            int id_number = sc.nextInt();
            System.out.print("Enter Name: ");
            String name = sc.next();
            num--;

            tables.put(id_number, name);
        }

        for (Integer keys : tables.keySet()) {
            System.out.println(keys + "\t" + tables.get(keys));
        }
        sc.close();
    }
}