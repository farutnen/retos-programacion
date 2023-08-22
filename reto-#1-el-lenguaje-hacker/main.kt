fun main(){
    println(leetTranslator (text: "Este es un texto de prueba para ver si el reto funciona!"))

}
private fun leetTranslator(text: String): String {

    var leetText =""

    var leet = mapOf("A" to "4", "B" to "I3", "C" to "[", "D" to ")", "E" to "3", "F" to "|=", "G" to "&", "H" to "#", "I" to "1", "J" to ",.|", "K" to ">|", "L" to "1", "M" to "(v)" , "N" to "И", "O" to "0", "P" to "|*", "Q" to "(_,)", "R" to "I2", "S" to "5", "T" to "7", "U" to "(_)", "V" to "|/", "W" to "VV", "X" to "><", "Y" to "J", "Z" to "2", "1" to "L", "2" to "R", "3" to "E", "4" to "A", "5" to "S", "6" to "b", "7" to "T", "8" to "B", "9" to "g", "0" to "o")

    for (caracter in text) {
        var resultado = caracter.toString().uppercase()
        leetText += if(leet.containsKey(resultado)) {
            leet[resultado]
        }else {
            caracter.toString()
        }
    }

    return leetText
} 
