package DSA;

public class Prac9InterpolationSearch {
    
    public static void main(String[] args) {
        
        int[] array = {1,2,3,4,5,6,7,8,9};
        int index = interpolationSearch(array, 8);

        if (index != -1) {
            System.out.println("Target Found At Index: " + index);
        } else {
            System.out.println("Target Not Found");
        }

    } private static int interpolationSearch(int[] array, int value) {

        int lower = 0;
        int higher = array.length - 1;

        while (value >= array[lower] && value <= array[higher] && lower <= higher) {
            
            int probe = lower + (higher - lower) * (value - array[lower]) /
                        (array[higher] - array[lower]);
            System.out.println("Probe: " + probe);

            if (array[probe] == value) {
                return probe;
            } else if (array[lower] < value){
                lower = probe + 1;
            } else {
                higher = probe - 1;
            }
        }
        return -1;

    }
}
