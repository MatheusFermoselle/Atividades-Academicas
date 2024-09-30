import kotlin.math.min

fun main() {

    val relogioo = Relogio("Patek", 200000.00, 10, 25, 40)
    println(relogioo.verHora())
    println(relogioo.validar())

    println("Qual é o modelo do seu relógio")
    val modeloUsuaio = readln().toString()
    println("Qual é o preço do seu relógio")
    val precoUsuario = readln().toDouble()
    println("Qual são as horas do seu relógio")
    val horasUsuario = readln().toInt()
    println("Qual são os minutos do seu relógio")
    val minutosUsuario = readln().toInt()
    println("Qual são os segundos do seu relógio")
    val segundosUsuario = readln().toInt()

    val relogio2 = Relogio(modeloUsuaio, precoUsuario, horasUsuario, minutosUsuario, segundosUsuario)
    println(relogio2.validar())
    println("Hora no 2º relógio: ${relogio2.verHora()}")


    val texto = "ola"

    println(texto) // referente a olá (o texto retorna ola)

    val resultadoDoRetorno = relogio2.verHora() // HH:MM:SS
    println(resultadoDoRetorno)

}