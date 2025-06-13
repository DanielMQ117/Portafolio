Proceso buscarProductoCatalogo

    Definir producto Como Cadena;
    Definir tiempoInicio, intentos Como Entero;
    Definir encontrado Como Logico;
	Definir catalogo Como Cadena;
	Definir Precio Como Entero;
	Dimensionar catalogo[9];
	Dimensionar Precio[9];
    encontrado <- Falso;
    intentos <- 0;
    catalogo[0] <- "Martillo";
    catalogo[1] <- "Clavos";
    catalogo[2] <- "Destornillador";
	catalogo[3] <- "Cinta metrica";
	catalogo[4] <- "Alicate";
	catalogo[5] <- "Laves";
	catalogo[6] <- "Tubo pvc";
	catalogo[7] <- "Cemento";
	catalogo[8] <- "Punzones";
	Precio[0] <- 250;
	Precio[1] <- 10;
	Precio[2] <- 200;
	Precio[3] <-450;
	Precio[4] <-340;
	Precio[5] <-200;
	Precio[6] <-40;
	Precio[7] <-700;
	Precio[8] <-200;
    Mientras intentos < 3 y no encontrado Hacer
        intentos <- intentos + 1;
        tiempoInicio <- HoraActual();
		
        Escribir "";
        Escribir "Intento ", intentos, " de 3";
        Escribir "Ingrese el nombre del producto a buscar ";
        Escribir "Tienes 20 segundos para ingresar el producto.";
        Leer producto;
		
        Si (HoraActual() - tiempoInicio) <= 20 Entonces
            Si estaEnCatalogo(producto, catalogo,Precio) Entonces
                Escribir " Producto encontrado en el cat�logo.";
                encontrado <- Verdadero;
            Sino
                Escribir " Producto no encontrado. Intenta nuevamente.";
            FinSi
        Sino
            Escribir " Tiempo agotado para ingresar el producto.";
        FinSi
    FinMientras
	
    Si no encontrado Entonces
        Escribir "";
        Escribir " Ha agotado los 3 intentos. No se encontr� el producto.";
    FinSi
FinProceso

Funcion resultado <- estaEnCatalogo(producto, catalogo,Precio)
    Definir resultado Como Logico;
    Definir i Como Entero;
    resultado <- Falso;
	
    Para i <- 0 Hasta 2 Hacer
        Si Mayusculas(producto) = Mayusculas(catalogo[i])  Entonces
			Escribir "El precio del producto es ",Precio[0];
            resultado <- Verdadero;
        FinSi
    FinPara
FinFuncion
