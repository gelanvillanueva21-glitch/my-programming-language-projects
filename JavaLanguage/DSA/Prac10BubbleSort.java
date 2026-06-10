package DSA;

public class Prac10BubbleSort {
    
    public static void main(String[] args) {
        int array[] = {9,2 ,6 ,3, 5, 1, 8, 4, 7};
        bubbleSort(array);
        for (int i : array) {
            System.out.print(i);
        }
    } private static void bubbleSort(int array[]) {

        for (int i = 0; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - 1; j++) {
                if (array[j] > array[j+1]) {
                    int temporary = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temporary;
                }
            }
        }
    }
}
