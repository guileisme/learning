class Quadrado extends Forma2D {
    float lado;

    public Quadrado(float lado) {
        this.lado = lado;
    }

    public float calcularArea() {
        return lado*lado;
    }
}