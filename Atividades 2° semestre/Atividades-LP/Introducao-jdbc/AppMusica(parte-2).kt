fun main() {
    val musicaRepositorio = MusicaRepositorio()
    musicaRepositorio.configurar()
    musicaRepositorio.criarTabela()

    val novaMusica = Musica()
    novaMusica.nome = "Diggy Diggy Hole"
    novaMusica.banda = "Rock de anão"
    novaMusica.produtor = "Produtora Top"

    // Retorna "true" ou "false"
    val sucesso = musicaRepositorio.inserir(novaMusica)

    if (sucesso) {
        println("Inserido com sucesso")
    } else {
        println("Deu ruim!")
    }


    val listaMusicas = musicaRepositorio.listar()
    listaMusicas.forEach {  // -> mesma coisa que um for normal. "ForEach" = "para cada"
        println(
            """
            Id: ${it.id}
            Nome: ${it.nome}
            Banda: ${it.banda}
            Produtor: ${it.produtor}
        """.trimIndent()
        )

        val idParaBusca = 1
        if (musicaRepositorio.existePorId(idParaBusca)){
            val musicaEncontrada = musicaRepositorio.buscaPorId(idParaBusca)
            println("Nome: ${musicaEncontrada.nome}")
        } else{
            println("Música não existe!")
        }

        musicaRepositorio.inserir(
        Musica(nome = "Hotel California", banda = "Eagles", produtor = "TOP"))

        if (musicaRepositorio.existePorId(idParaBusca)){
            val deletado = musicaRepositorio.deletePorId(idParaBusca)
        } else{
            println("Música não existe")
        }

        if (musicaRepositorio.existePorId(2)){
            val musicaAtualizada = Musica(
                nome = "Californication",
                banda = "RHCP",
                produtor = "Na california"
            )
            val atualizado = musicaRepositorio.atualizaPorId(2, musicaAtualizada)
            println(if (atualizado) "Atualizado!" else "Deu ruim")
        } else {
            println("Música não existe")
        }
    }
}