package DSA;

public class Prac8BinarySearch {

    public static void main(String[] args) {
        int[] array = new int[1000000];
        int target = 677777;

        for (int i = 0; i < array.length; i++) {
            array[i] = i;
        }

        int result = binarySearch(array, target);

        if (result != -1) {
            System.out.println("Target Found At Index: " + result);
        } else {
            System.out.println("Target Not Found");
        }
    } private static int binarySearch (int[] array, int target) {
        int lower = 0;
        int higher = array.length - 1;

        while (lower <= higher) {
            int middle = lower + (higher - lower) / 2;

            if (array[middle] == target) {
                return middle;
            } else if (array[middle] > target) {
                higher = middle - 1;
            } else {
                lower = middle + 1;
            }
        }
        return -1;
    }
}