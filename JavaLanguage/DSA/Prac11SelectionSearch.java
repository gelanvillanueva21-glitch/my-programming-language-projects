package DSA;

public class Prac11SelectionSearch {
    
    public static void main(String[] args) {
        int[] array = {6, 2, 9, 8, 1, 3, 7, 4, 5};
        selection_sort(array);
        for (int i : array) {
            System.out.print(i);
        }
    } private static void selection_sort(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[min] > array[j]) {
                    min = j;
                }
            }
            int temporary = array[i];
            array[i] = array[min];
            array[min] = temporary;
        }
    }
}
