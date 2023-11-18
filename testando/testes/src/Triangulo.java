class Triangulo extends Forma2D {
    float base;
    float altura;

    public Triangulo(float base, float altura) {
        this.base = base;
        this.altura = altura;
    }

    public float calcularArea() {
        return (base * altura)/2;
    }
}

