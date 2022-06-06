import java.awt.*;

// public class App {
//     public static void main(String[] args) {
//         Point point1 = new Point(x:1, y:1);
//         Point point2 = point1;
//         point1.x = 2;
//         System.out.println(point2);

//     }
// }

public class App {
    public static void main(String[] args) {
        String message = "    Hi \"Derek\""+ "!!    ";
        // System.out.println(message.endsWith("!!"));
        // System.out.println(message.startsWith("!!"));
        // System.out.println(message.length());
        // System.out.println(message.indexOf("h"));
        System.out.println(message);
        System.out.println(message.replace("Hi", "Hello"));
        System.out.println(message.replace("!", "*"));
        System.out.println(message.toLowerCase());
        System.out.println(message.toUpperCase());
        System.out.println(message.trim());
    }
}