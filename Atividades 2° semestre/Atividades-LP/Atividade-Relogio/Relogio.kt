class Relogio(
    var modelo: String = "",
    var preco: Double = 0.0,
    var horas: Int = 0,
    var minutos: Int = 0,
    var segundos: Int = 0

    ) {

    fun zerar() {
        minutos = 0
        segundos = 0
        horas = 0
    }

    fun validar(): String {  // O função, se alguem te chamar, você retorna a variável texto.

        var texto = "valor correto"

        if (horas > 23 || horas < 0) {
            horas = 0
            texto = "Valores inválidos identificados. Ajustado!"
        }
        if (minutos > 60 || minutos < 0) {
            minutos = 0
            texto = "Valores inválidos identificados. Ajustado!"
        }
        if (segundos > 60 || segundos < 0) {
            segundos = 0
            texto = "Valores inválidos identificados. Ajustado!"
        }

        return texto
    }


    fun verHora(): String {


        var HoraFormatada = "%02d".format(horas)
        var MinutoFormatado = "%02d".format(minutos)
        var SegundoFormatado = "%02d".format(segundos)

        return "$HoraFormatada:$MinutoFormatado:$SegundoFormatado"

    }

}