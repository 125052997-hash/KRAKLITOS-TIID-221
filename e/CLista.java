class CLista {
    Nodo primero;
    Nodo ultimo;
    int tamano;

    CLista() {
        primero = ultimo = null;
        tamano = 0;
    }

    void imprimir() {
        Nodo p = primero;

        while (p != null) {
            System.out.print(p.dato + "-->");
            p = p.sig;
        }

        System.out.println("null");
    }

    void agregarFinal(int e) {
        Nodo n = new Nodo(e);

        if (tamano == 0) {
            primero = ultimo = n;
        } else {
            ultimo.sig = n;
            ultimo = n;
        }

        tamano++;
    }

    // Método asignado: agregarInicio
    void agregarInicio(int e) {
        Nodo n = new Nodo(e);

        if (tamano == 0) {
            primero = ultimo = n;
        } else {
            n.sig = primero;
            primero = n;
        }

        tamano++;
    }
}