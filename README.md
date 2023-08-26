<p align="center">
  <img width="150" height="150" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Escudo_de_la_universidad_Mariano_G%C3%A1lvez_Guatemala.svg/640px-Escudo_de_la_universidad_Mariano_G%C3%A1lvez_Guatemala.svg.png">
</p>

### Catedrático: Melvin Cali
### Alumno: Misael Armando Marroquín Godínez
### Carnet: 7690-23-23847


# Tarea No. 1 Algoritmos
En esta tarea realizamos un convertidor de unidades de medida de centímetros a metros, yardas, varas, pulgadas o pies.
&nbsp;

## Algoritmo escrito en Pseudocódigo
&nbsp;
Como primer punto, se escribió el algoritmo que convierte unidades de medida en pseudocódigo.
1.  A continuación, el algoritmo escrito en pesudocódigo.
----
----
```pseudocodigo
Algoritmo CONVERSOR_MEDIDAS
	//DECLARAR VARIABLES
	Definir cms como real
	//Solicita al usuario ingresar la longitud en centimetros
	Escribir "Ingrese longitud en centimetros:  "
	Leer cms
	Definir conversion Como Real
	definir metro Como Real
	metro <- 0.01
	definir yarda Como Real
	yarda <- 0.0109361
	definir vara Como Real
	vara <- 0.0083333
	Definir pulgada Como Real
	pulgada <- 0.393701
	Definir pie Como Real
	pie <- 0.0328084
	Definir medida como Cadena
	
	Escribir "Ingrese la unidad de medida, que desee convertir, 1. Metro, 2. Yarda, 3. Vara, 4. Pulgada, 5. Pie:    "
	leer medida 
	
	//Este procedimiento realiza la conversión de las longitudes ingresadas.
	
	Si (medida = "1")Entonces
		conversion = cms * metro
		Escribir "La longitud en metros es: ",conversion
	FinSi
	si (medida = "2") Entonces
		conversion = cms * yarda
		Escribir "La longitud en yardas es: ",conversion
	FinSi
	si (medida = "3") Entonces
		conversion = cms * vara
	Escribir " La longitud en varas es:  ", conversion
    FinSi	
    si (medida = "4") Entonces
		conversion = cms * pulgada
		Escribir "La longitud en pulgadas es:  ", conversion
	FinSi
	si (medida = "5") Entonces
		conversion = cms * pie
		Escribir "La longitud en pies es:  ", conversion
	SiNo
	Escribir 	"La unidad de medida no existe. Elija una opción de la 1 a la 5"
	FinSi

FinAlgoritmo
```
----

&nbsp;
&nbsp;
&nbsp;

## Algoritmo escrito en lenguaje C ++
&nbsp;
Como segundo punto, se escribió el algoritmo que convierte unidades de medida en lenguaje C++
&nbsp;
----
----
````C++
//Tarea de la clase de Algoritmos No. 1
//Conversor de Unidad de Medidas


#include <iostream>

int main(){
using namespace std;
//Declarar Variables
double cms;
double conversion;
const double metro = 0.01; 
const double yarda = 0.0109361;
const double vara = 0.0083333;
const double pulgada = 0.393701;
const double pie = 0.0328084;


// Solicita al usuario ingresar la longitud en cms.
std::cout << "Ingrese la longitud en cms.: ";
std::cin >> cms;

// Solicita al usuario ingresas la unidad de medida a convertir

std::cout << "Ingrese la unidad de medida, que desee convertir, 1. Metro, 2. Yarda, 3. Vara, 4. Pulgada, 5. Pie:    ";
std::string medida;
std::cin >> medida;

//Este procedimiento realiza la conversión de las longitudes ingresadas.
if (medida == "1"){
	conversion = cms * metro;
	std::cout << "La longitud en metros es: " << conversion << std::endl; 
} else if (medida == "2") {
	conversion = cms * yarda;
	std::cout << "La longitud en Yardas es: " << conversion << std::endl;
} else if (medida == "3"){
	conversion = cms * vara;
	std::cout << "La longitud en Varas es: " << conversion << std::endl;
} else if (medida == "4"){
	conversion = cms * pulgada;
	std::cout << "La longitud en Pulgadas es: " << conversion << std::endl;
} else if (medida == "5"){
	conversion = cms * pie;
	std::cout << "La longitud en Pies es: " << conversion << std::endl;
} else { 
	std::cout << "La Unidad de medida ingresada es invalida. Ingrese una opcion de 1  a  5" << std::endl;
}


return 0;

}
`````
&nbsp;
&nbsp;
## Algoritmo escrito en lenguaje Python
&nbsp;
Como tercer punto, se escribió el algoritmo que convierte unidades de medida en lenguaje Python
&nbsp;
----
````python
#Tarea de la clase de Algoritmos No. 1
#Conversor de Unidad de Medidas
#Declarar variales
conversion = float()
metro = 0.01
yarda = 0.0109361
vara = 0.0083333
pulgada = 0.393701
pie = 0.0328084

#Solicita al usuario ingresar la longitud en centimetros
print("Ingrese longitud en centimetros:  ")
cms = float(input())
#Solicita al usuario ingresas la unidad de medida a convertir
print("Ingrese la unidad de medida, que desee convertir, 1. Metro, 2. Yarda, 3. Vara, 4. Pulgada, 5. Pie:    ")
medida = input()

#Este procedimiento realiza la conversión de las longitudes ingresadas.
if medida == "1":
    conversion = cms * metro
    print("La longitud en metros es:  ",conversion)
elif medida == "2":
   conversion = cms * yarda
   print("La longitud en yardas es:  ",conversion)
elif medida == "3":
   conversion = cms * vara
   print("La longitud en Varas es:  ",conversion)
elif medida == "4":
   conversion = cms * pulgada
   print("La longitud en Pulgadas es:  ",conversion)
elif medida == "5":
   conversion = cms * pie
   print("La longitud en Pies es:  ",conversion)
else:
   print("La unidad de medida no existe. Elija una opcion de la 1 a la 5")

input("Presione Enter para salir...")
````



