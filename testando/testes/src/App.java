import java.util.ArrayList;

public class App {
    public static void main(String[] args) {
        // Criando as formas
        Quadrado Quadrado = new Quadrado(3);
        Triangulo Triangulo = new Triangulo(2, 4);

        // Adicionando as formas em um ArrayList
        ArrayList<Forma2D> formas = new ArrayList<>();
        formas.add(Quadrado);
        formas.add(Triangulo);

        // Iterando sobre as formas e imprimindo as áreas
        for (Forma2D forma : formas) {
            System.out.println("Área: " + forma.calcularArea());
        }
    }
}

