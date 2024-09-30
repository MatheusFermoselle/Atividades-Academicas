import java.text.DateFormat
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import javax.swing.text.DateFormatter

fun main() {
    val bancoDeDados = mutableListOf<Produto>()

    println("Bem-vindo ao gerenciamento de produtos!")

    while (true) {
        println(
            """
            ------- Produtos --------
            1- Adicionar produto.
            2- Buscar produto por índice (começa de 0)
            3- Remover produto por índice (começa de 0)
            4- Verificar validade por índice (começa de 0)
            5- Sair
        """.trimIndent()
        )
        print("Digite a opção desejada: ")
        val opcao = readln().toInt()

        when (opcao) {

            1 -> {
                val novoProduto = Produto()
                print("Digite o novo produto: ")
                novoProduto.nome = readln()

                print("Digite o preço:")
                novoProduto.preco = readln().toDouble()

                print("Digite a data de validade dd/MM/yyyy:")
                val dataTexto = readln()

                val formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy")

                val dataformatada = LocalDate.parse(dataTexto, formatador)
                novoProduto.validade = dataformatada
                bancoDeDados.add(novoProduto)


//                print("Digite o ano de vencimento:")
//                val ano = readln().toInt()
//
//                print("Digite o mês de vencimento:")
//                val mes = readln().toInt()
//
//                print("Digite o dia de vencimento:")
//                val dia = readln().toInt()
//
//                novoProduto.validade = LocalDate.of(ano, mes , dia)
            }

            2 -> {
                print("Digite o produto que deseja listar: ")
                val index = readln().toInt()

                if (index >= 0 && index <= bancoDeDados.size){
                    val formatador = DateTimeFormatter.ofPattern("dd/MM/yyyy")
                    val produtoEncontrado = bancoDeDados[index]
                    println("O produto ${produtoEncontrado.nome} custa R$${produtoEncontrado.preco} e tem validade ${produtoEncontrado.validade.format(formatador)}")
                } else{
                    println("Produto não encontrado")
                }

            }

            3-> {
                print("Digite o produto que deseja remover: ")
                val indexRemover = readln().toInt()
                val produtoRemovido = bancoDeDados.removeAt(indexRemover)
                println("O produto ${produtoRemovido.nome} foi removido com sucesso")

            }

            4-> {
                print("Digite o produto que deseja verificar a validade: ")
                val indexVerificar = readln().toInt()

                if (indexVerificar >= 0 && indexVerificar < bancoDeDados.size ){
                    val produtoEncontrado = bancoDeDados[indexVerificar]
                    println(produtoEncontrado.descrever())
                } else{
                    println("Produto não encontrado")
                }

            }

            5-> break
            else ->{
                println("Opção inválida")
            }


        }

    }

}