/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */


function fizzbuzz(){
    for(let number = 1; number <= 100; number++){
        let salida = "";
        if(number%3 == 0){
            salida += 'fizz';
            //flag=true;
        }
        if(number%5 == 0){
            salida += 'buzz';
            //flag=true;
        }
        if(salida === ""){
            console.log(number);
        }else{
            console.log(salida);
        }
    }
}

fizzbuzz()
