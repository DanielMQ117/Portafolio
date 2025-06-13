Proceso CineAtenas
	//este programa es para hacer compras de el menu de CINEMAS ATENAS;
	
	Definir promociones, bebidas, bocadillos, asientos Como Cadena;
	Definir preciosPromo, preciosBebidas, preciosBocadillos, preciosAsientos Como Real;
	Definir opcioon, subopcion, i, contador Como Entero;
	Definir total Como Real;
	Definir resumen Como Cadena;
	Dimension promociones(3);
	Dimension preciosPromo(3);
	Dimension bebidas(7);
	Dimension preciosBebidas(7);
	Dimension bocadillos(6);
	Dimension preciosBocadillos(6);
	Dimension asientos(4);
	Dimension preciosAsientos(4);
	Dimension resumen(101);
	
	escribir " +--------------------------------------+---------------------------------------+";
	escribir " |                              *CINEMAS-ATENAS*                                |";
	ESCRIBIR " |            !Promociones!             |        *Bebidas*                      |";
	escribir " |  palomitas yumbo y = 70c$            | bbid carbonatada yumbo= 80c$          |";
	escribir " |  palomitas medi y bbid grande=130c$  | bbid carbonatada mediana= 60c$        |";
	ESCRIBIR " |--------------------------------------| bebid carbonatada peque?a= 40c$       |";
	escribir " |             *Bocadillos*             | jugos medianos= 40c$                  |";
	escribir " | palomitas yumbo=90c$                 | jugos pequenos= 32c$                  |";
	escribir " | palomitas medianas=70c$              | agua = 30c$                           |";
	escribir " | palomitas pequenas=50c$              |---------------------------------------|";
	escribir " | nachos = 65c$                        |       *Tickets*                       |";
	escribir " | golocinas =25c$                      |   BOLETO VIP=700c$     boleto =200c$  |";
	escribir " |                                      |  lentes 3D=GRATIS!    lentes 3D =100  |";
	escribir " +--------------------------------------+---------------------------------------+";
	
	total <- 0;
	contador <- 0;
	
	promociones(1) <- "1. Palomitas yumbo y = 70c$";
	preciosPromo(1) <- 70;
	promociones(2) <- "2. Palomitas medi y bebida grande = 130c$";
	preciosPromo(2) <- 130;
	
	bebidas(1) <- "1. Bebida carbonatada yumbo = 80c$";
	preciosBebidas(1) <- 80;
	bebidas(2) <- "2. Bebida carbonatada mediana = 60c$";
	preciosBebidas(2) <- 60;
	bebidas(3) <- "3. Bebida carbonatada peque?a = 40c$";
	preciosBebidas(3) <- 40;
	bebidas(4) <- "4. Jugos medianos = 40c$";
	preciosBebidas(4) <- 40;
	bebidas(5) <- "5. Jugos peque?os = 32c$";
	preciosBebidas(5) <- 32;
	bebidas(6) <- "6. Agua = 30c$";
	preciosBebidas(6) <- 30;
	
	bocadillos(1) <- "1. Palomitas yumbo = 90c$";
	preciosBocadillos(1) <- 90;
	bocadillos(2) <- "2. Palomitas medianas = 70c$";
	preciosBocadillos(2) <- 70;
	bocadillos(3) <- "3. Palomitas peque?as = 50c$";
	preciosBocadillos(3) <- 50;
	bocadillos(4) <- "4. Nachos = 65c$";
	preciosBocadillos(4) <- 65;
	bocadillos(5) <- "5. Golosinas = 25c$";
	preciosBocadillos(5) <- 25;
	
	asientos(1) <- "1. Boleto VIP = 700c$";
	preciosAsientos(1) <- 700;
	asientos(2) <- "2. Boleto normal = 200c$";
	preciosAsientos(2) <- 200;
	asientos(3) <- "3. Lentes 3D = 100c$";
	preciosAsientos(3) <- 100;
	
	Repetir;
		Escribir "-----------------------------";
		Escribir "    MENu DE CINE ATENAS";
		Escribir "1. Promociones";
		Escribir "2. Bebidas";
		Escribir "3. Bocadillos";
		Escribir "4. Asientos";
		Escribir "5. Finalizar compra";
		Escribir "Seleccione una opci?n:";
		Leer opcioon;
		
		Segun opcioon Hacer
			1:
				Repetir;
					Escribir "";
					Escribir "PROMOCIONES DISPONIBLES:";
					Para i <- 1 Hasta 2
						Escribir promociones(i);
					FinPara
					Escribir "Ingrese numero de promocion (0 para regresar):";
					Leer subopcion;
					Si subopcion >= 1 Y subopcion <= 2 Entonces
						total <- total + preciosPromo(subopcion);
						contador <- contador + 1;
						resumen(contador) <- promociones(subopcion);
						Escribir "Agregado. Total: ", total, "c$";
					FinSi
				Hasta Que subopcion = 0;
				
			2:
				Repetir
					Escribir "";
					Escribir "BEBIDAS DISPONIBLES:";
					Para i <- 1 Hasta 6
						Escribir bebidas(i);
					FinPara
					Escribir "Ingrese numero de bebida (0 para regresar):";
					Leer subopcion;
					Si subopcion >= 1 Y subopcion <= 6 Entonces
						total <- total + preciosBebidas(subopcion);
						contador <- contador + 1;
						resumen(contador) <- bebidas(subopcion);
						Escribir "Agregado. Total: ", total, "c$";
					FinSi
				Hasta Que subopcion = 0;
				
			3:
				Repetir
					Escribir "";
					Escribir "BOCADILLOS DISPONIBLES:";
					Para i <- 1 Hasta 5
						Escribir bocadillos(i);
					FinPara
					Escribir "Ingrese numero de bocadillo (0 para regresar):";
					Leer subopcion;
					Si subopcion >= 1 Y subopcion <= 5 Entonces
						total <- total + preciosBocadillos(subopcion);
						contador <- contador + 1;
						resumen(contador) <- bocadillos(subopcion);
						Escribir "Agregado. Total: ", total, "c$";
					FinSi
				Hasta Que subopcion = 0;
				
			4:
				Repetir
					Escribir "";
					Escribir "ASIENTOS DISPONIBLES:";
					Para i <- 1 Hasta 3
						Escribir asientos(i);
					FinPara
					Escribir "Ingrese numero de asiento (0 para regresar):";
					Leer subopcion;
					Si subopcion >= 1 Y subopcion <= 3 Entonces
						total <- total + preciosAsientos(subopcion);
						contador <- contador + 1;
						resumen(contador) <- asientos(subopcion);
						Escribir "Agregado. Total: ", total, "c$";
					FinSi
				Hasta Que subopcion = 0;
				
			5:
				Escribir "";
				Escribir "Gracias por su compra!";
				Escribir "----- CINEMAS-ATENAS-----";
				Para i <- 1 Hasta contador
					Escribir resumen(i);
				FinPara
				Escribir "TOTAL A PAGAR: ", total, "c$";
		FinSegun
		Escribir "";
	Hasta Que opcioon = 5;
FinProceso
