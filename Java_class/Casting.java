public class Casting {
    public static void main(String[] args) {
        // Implicit casting
        // byte > short > int > long > float > double
        // short x = 1;
        // double x = 1.1;
        // double y = x + 2;
        // String x = "1";
        String x = "1.1";
        double y = Double.parseDouble(x) + 2;
        // Integer.parseInt()
        // Short.parseShort()
        // Float.parseFloat()
        System.out.println(y);
    }
}
