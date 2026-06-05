package DSA;

public class Prac7LinearSearch {
    public static void main(String[] args) {
        int[] arrayList = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        
        int search = linearSearch(arrayList, 91);

        if (search != -1) {
            System.out.println("Target Found Index: " + search);
        } else {
            System.out.println("Target Not Found");
        }

    } private static int linearSearch(int[] array, int target) {

        for (int i = 0; i < array.length; i++) {
            if (target == array[i]) {
                return i;
            }
        }
        return -1;

    }
}
