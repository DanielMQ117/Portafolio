Proceso ValidarCedulaNicaragua
	Definir cedula, mensaje Como Cadena;
	Definir i, longitudd, tiempoInicial Como Entero;
	Definir valido Como Logico;
	Definir partes Como Cadena;
	Dimension partes[4];
	
	Escribir "=======================================================================";
	Escribir "";
	Escribir "            Validando cedula de identidad de Nicaragua";
	Escribir "";
	Escribir "=======================================================================";
	
	Para i <- 1 Hasta 3 Con Paso 1
		
		tiempoInicial <- HoraActual();
		
		Escribir "";
		Escribir " -> Intento ", i, " de 3";
		Escribir Sin Saltar " -> Ingrese cedula de identidad: ";
		Leer cedula;
		
		Si (HoraActual() - tiempoInicial)  < 12 Entonces
			
			
			longitudd <- Longitud(cedula);
			
			Si longitudd = 16 Entonces
				Si SubCadena(cedula, 3, 3) = "-" Y SubCadena(cedula, 10, 10) = "-" Y ContarGuiones(cedula) = 2 Entonces
					
					partes[0] <- SubCadena(cedula, 0, 2);
					partes[1] <- SubCadena(cedula, 4, 9);
					partes[2] <- SubCadena(cedula, 11, 14);
					partes[3] <- SubCadena(cedula, 15, 15);
					
					Si EsNumero(partes[0]) Y EsNumero(partes[1]) Y EsNumero(partes[2]) Y EsLetra(partes[3]) Entonces
						valido <- Verdadero;
						mensaje <- "	Cedula valida";
					SiNo
						valido <- Falso;
						mensaje <- "	Cedula invalida";
						Si No EsLetra(partes[3]) Entonces
							mensaje <- mensaje + ". El ultimo caracter debe ser una letra";
						FinSi
					FinSi
					
					Escribir mensaje;
					
				SiNo
					Escribir " Cedula debe tener 2 separadores - en las posiciones correctas";
				FinSi
			SiNo
				Escribir "	Cedula invalida, debe tener 16 caracteres";
			FinSi
		SiNo
			Escribir " Tiempo agotado, intente de nuevo!";
		FinSi
	FinPara
FinProceso


SubProceso resultado <- ContarGuiones(texxto)
	Definir i, resultado Como Entero;
	resultado <- 0;
	Para i <- 1 Hasta Longitud(texxto) Hacer
		Si SubCadena(texxto, i, i) = "-" Entonces
			resultado <- resultado + 1;
		FinSi
	FinPara
FinSubProceso

SubProceso resultado <- EsNumero(cadenaa)
	Definir i Como Entero;
	Definir resultado Como Logico;
	resultado <- Verdadero;
	Para i <- 0 Hasta Longitud(cadenaa) -1 Hacer
		Si no ((SubCadena(cadenaa, i, i) >= "0") Y (SubCadena(cadenaa, i, i) <= "9")) Entonces
			resultado <- Falso;
		FinSi
	FinPara
FinSubProceso

SubProceso resultado <- EsLetra(caracterr)
	Definir resultado Como Logico;
	Si (caracterr >= "A" Y caracterr <= "Z") O (caracterr >= "a" Y caracterr <= "z") Entonces
		resultado <- Verdadero;
	SiNo
		resultado <- Falso;
	FinSi
FinSubProceso
