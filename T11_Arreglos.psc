// Un restaurante desea saber cuales son las opiniones sobre un nuevo plato, se realizara
// una encuesta a los empleados (15 personas) del restaurante a los cuales se les pide que
// indiquen por medio de un numero del 1 al 10 su opinión. Elabore un algoritmo que pida a
// las 15 personas las opiniones y luego que presente el resultado.

Proceso opinionesEmpleados 
    Definir opiniones, opinion, contador Como Entero; 
    Dimension opiniones[10]; //Crea el arreglo
    
    Para contador <- 0 Hasta 9 Con Paso 1 Hacer
        opiniones[contador] <- 0; //Inicializa a cero cada elemento del arreglo 
    FinPara
    
    Para contador <- 1 Hasta 15 Con Paso 1 Hacer //Solicita las 15 opiniones 
        Repetir
            Escribir sin saltar "Ingrese opinion No", contador, " (valores del 1-10) ";
            Leer opinion;
        Hasta Que opinion <= 10 & opinion >=1
		
        opiniones[opinion-1] <- opiniones[opinion - 1] + 1;
		
    FinPara
	
    Para contador <- 0 Hasta 9 Con Paso 1 Hacer
        Escribir "Puntaje No ", contador + 1, " tiene ", opiniones[contador], " votos"; 
    FinPara;
	
FinProceso
