public class CPruebaLista {
    public static void main(String[] args) {
        CLista lista = new CLista();

        lista.agregarFinal(8);
        lista.agregarFinal(9);
        lista.agregarFinal(3);
        lista.agregarFinal(7);
        lista.agregarFinal(6);
        lista.agregarInicio(5);

        lista.imprimir();
    }
}