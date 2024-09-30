import org.apache.commons.dbcp2.BasicDataSource
import org.springframework.jdbc.core.BeanPropertyRowMapper
import org.springframework.jdbc.core.JdbcTemplate

class MusicaRepositorio {

 lateinit var jdbcTemplate: JdbcTemplate


 fun configurar() {
     val datasource = BasicDataSource()
     datasource.driverClassName = "org.h2.Driver"
     datasource.url = "jdbc:h2:mem:Festival"
     datasource.username = "sa"
     datasource.password = ""

     val jdbcTemplate = JdbcTemplate(datasource)
 }

fun criarTabela(){
    jdbcTemplate.execute("""
        CREATE TABLE if not exists Musica(
        id int Primary key auto_increment,
        nome varchar(255) not null,
        banda varchar(255) not null,
        produtor varchar(255)  
        )
    """.trimIndent())
}

 fun inserir(novaMusica: Musica):Boolean {

     val qtdLinhasAfetadas = jdbcTemplate.update(
         """
            INSERT INTO Musica (nome, banda, produtor)
            values(?,?,?)
         """,
         novaMusica.nome,
         novaMusica.banda,
         novaMusica.produtor
     )
     return qtdLinhasAfetadas > 0
 }

   fun listar(): List<Musica> {
       return jdbcTemplate.query(
           "Select * from Musica",
           BeanPropertyRowMapper(Musica::class.java)
       )

   }

   fun existePorId(id: Int):Boolean{
       val qtdExistentes = jdbcTemplate.queryForObject(
           "Select count(*) from Musica where id = ?",
           Int::class.java,
           id
       )

       return qtdExistentes > 0

   }

    fun buscaPorId(id: Int): Musica{
        val musicaEncontrada = jdbcTemplate.queryForObject(
            "Select * from Musica Where id = ?",
            BeanPropertyRowMapper(Musica::class.java),
            id
        )

        return musicaEncontrada
    }

    fun deletePorId(id: Int):Boolean{
        val qtdLinhasAfetadas = jdbcTemplate.update(
            "Delete from Musica where id = ?",
            id
        )
        return qtdLinhasAfetadas > 0
    }

    fun atualizaPorId(id: Int, musicaAtualizada: Musica): Boolean{
        val qtdLinhasAfetadas = jdbcTemplate.update(
            """
                Update Musica set
                nome = ?,
                banda = ?,
                produtor = ?
                where id = ?
            """,
            musicaAtualizada.nome,
            musicaAtualizada.banda,
            musicaAtualizada.produtor,
            id
        )
        return qtdLinhasAfetadas > 0
    }
}

