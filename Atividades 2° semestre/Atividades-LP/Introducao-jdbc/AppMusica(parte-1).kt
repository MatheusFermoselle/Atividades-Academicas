import org.apache.commons.dbcp2.BasicDataSource
import org.h2.command.dml.Insert
import org.springframework.jdbc.core.BeanPropertyRowMapper
import org.springframework.jdbc.core.JdbcTemplate
import org.springframework.jdbc.core.queryForObject

fun main() {

    val datasource = BasicDataSource()
    datasource.driverClassName = "org.h2.Driver"
    datasource.url = "jdbc:h2:mem:Festival"
    datasource.username = "sa"
    datasource.password = ""

    val jdbcTemplate = JdbcTemplate(datasource)
    jdbcTemplate.execute("""
        CREATE TABLE Musica(
        id int Primary key auto_increment,
        nome varchar(255) not null,
        banda varchar(255) not null,
        produtor varchar(255)  
        )
    """.trimIndent())

    val qtdInseridos = jdbcTemplate.update(
        "Insert Into Musica(nome, banda, produtor) " +
            "values('Still loving you', 'Scorpions', 'Records')"
    )
    println("Linhas afetadas: $qtdInseridos")

    val listaMusica: List<Musica> = jdbcTemplate.query( //--> "query" = "consulta"
        "Select * from Musica",
        BeanPropertyRowMapper(Musica::class.java)
    )

    println(listaMusica[0].nome)
    listaMusica.forEach {  // -> mesma coisa que um for normal. "ForEach" = "para cada"
        println("""
            Id: ${it.id}
            Nome: ${it.nome}
            Banda: ${it.banda}
            Produtor: ${it.produtor}
        """.trimIndent())
    }

    val musicaId = 1

    val existeMusica : Boolean = jdbcTemplate.queryForObject(
        "Select count(*) FROM Musica where id =  ?",
        Int::class.java,
        musicaId
    ) > 0


    if (existeMusica != null){
        val musicaEncontrada = jdbcTemplate.queryForObject( //-> "query" = "consulta"
            "Select * from Musica where id = ?",
            BeanPropertyRowMapper(Musica::class.java),
            musicaId
        )

        println("""
            ID: ${musicaEncontrada.id}
            Nome : ${musicaEncontrada.nome}
        """.trimIndent())
    } else{
        println("Musica não existe")
    }


}