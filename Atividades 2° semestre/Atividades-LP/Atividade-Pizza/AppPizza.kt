fun main() {

    val pizza = PedidoPizza()

    println("Qual será o sabor da sua pizza?")
    val saborUsuario = readln()
    println("Qual é o preço da sua pizza?")
    val precoUsuario = readln().toDouble()
    println("Qual é a quantidade de amigos que irá dividir?")
    val quantidadeAmigosUsuario = readln().toInt()

    val pizzaUsuario = PedidoPizza(saborUsuario, precoUsuario, quantidadeAmigosUsuario)

    while (true) {
        println("1: Adiconar cupom")
        println("2: Sair")
        print("Digite a opção: ")
        val opcaoUsuario = readln().toInt()

        when (opcaoUsuario) {
            1 -> {
                println("Qual será seu cupom?")
                val cupomUsuario = readln()
                pizzaUsuario.validarCupom(cupomUsuario)
            }

            2 -> break
            else -> println("Opção inválida")


        }



    }
    println(pizzaUsuario.descrever())
    println("Cada amigo vai pagar R$${"%.2f".format(pizzaUsuario.obterValorPorAmigo())}")
    println(pizzaUsuario.obterCuponsUsados())
}
