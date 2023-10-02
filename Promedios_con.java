//Carlos Alejandro Moreno Camas 3ro JJ
//Carlos Adrioan Serrano Samayoa
import java.util.Scanner;
class PromedioCalificaciones {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Pedir al usuario la cantidad de calificaciones
        System.out.print("Ingrese la cantidad de calificaciones: ");
        int cantidadCalificaciones = scanner.nextInt();
        
        // Declarar variables para almacenar el total de calificaciones y el promedio
        double totalCalificaciones = 0;
        double promedio;
        
        // Pedir al usuario ingresar las calificaciones y calcular el total
        for (int i = 1; i <= cantidadCalificaciones; i++) {
            System.out.print("Ingrese la calificación #" + i + ": ");
            double calificacion = scanner.nextDouble();
            totalCalificaciones += calificacion;
        }
        
        // Calcular el promedio
        promedio = totalCalificaciones / cantidadCalificaciones;
        
        // Imprimir el promedio
        System.out.println("El promedio de calificaciones en el parcial es: " + promedio);
        
        // Imprimir mensaje de felicitación o consejo en función del promedio
        if (promedio == 10) {
            System.out.println("¡Felicidades! Tienes un promedio perfecto de 10.");
        } else if (promedio >= 8 && promedio <= 9) {
            System.out.println("Muy bien estas aprobado, buen trabajo.");
        } else if (promedio >= 5 && promedio <= 5) {
            System.out.println("Necesitas esforzarte un poco más, las bien.");
        } else {
            System.out.println("Estás REPROBADO y debes estudiar más.");
        }
        
        // Cerrar el scanner
        scanner.close();
    }
}
