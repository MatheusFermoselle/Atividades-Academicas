class PedidoPizza (
    var sabor: String = "",
    var preco: Double = 0.0,
    var quantidadeAmigos: Int = 0
){
    val listaCupom = mutableListOf<String>()
    fun descrever(): String{
       var pedido =  "Pedido de pizza de $sabor, que custa R$%.2f".format(preco)

        return pedido
    }

    fun validarCupom(cupom:String){
    if (cupom == "#amopizza"){
        preco = preco * 0.9
        listaCupom.add(cupom)
    } else {
        preco = preco
        listaCupom.add(cupom)
    }
    }

    fun obterValorPorAmigo(): Double{
        return if (quantidadeAmigos > 0){
            preco / quantidadeAmigos
        } else{
            0.0
        }
    }

    fun obterCuponsUsados(): String{
    var textoCupons = "Cupons usados: \n"

    for (cupomDaVez in listaCupom){
        textoCupons += "\n - $cupomDaVez"
    }
return textoCupons
    }


}