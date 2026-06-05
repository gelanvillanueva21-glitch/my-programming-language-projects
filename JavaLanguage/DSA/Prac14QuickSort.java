package DSA;

public class Prac14QuickSort {
    
    public static void main(String[] args) {
        int[] array = {2, 9, 4, 6, 1, 3, 5, 7, 8};
        quickSort(array, 0, array.length - 1);
        
        System.out.println();
        for (int num : array) {
            System.out.print(num + " ");
        }
    } private static void quickSort(int[] array, int start, int end) {

        if (end <= start) {
            return;
        }
        System.out.println();
        for (int i : array) {
            System.out.print(i + " ");
        }


        int pivot = partition(array, start, end);
        quickSort(array, start, pivot - 1);
        quickSort(array, pivot + 1, end);

    } private static int partition(int[] array, int start, int end) {

        int pivot = array[end];
        int i = start - 1;

        for (int j = start; j <= end - 1; j++) {
            if (array[j] < pivot) {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        i++;
        int temp = array[i];
        array[i] = array[end];
        array[end] = temp;

        return i;

    }
}
