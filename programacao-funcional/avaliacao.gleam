/// a funcao recebe uma data *data* e devolve 
/// se ela é considerada dia de ano ou nao *aaaa/12/31*
/// so é True caso o *dia* for *31* e o mes for *12*,caso contrario
/// False.
import gleam/string
import sgleam/check

pub fn eh_reveillon(data: String) -> Bool {
  let mes = string.slice(data, 5, 2)
  let dia = string.slice(data, 8, 2)
  case mes == "12" {
    True ->
      case dia == "31" {
        True -> True
        False -> False
      }
    False -> False
  }
}

/// função para teste da função *eh_reveillon*
pub fn eh_reveillon_examples() {
  check.eq(eh_reveillon("2024/12/31"), True)
  check.eq(eh_reveillon("2000/01/31"), False)
  check.eq(eh_reveillon("2001/12/30"), False)
}

///devolve True pois é dia de ano
/// devolve False pois não é dia de ano
/// devolve False pois não é dia de ano
/// Questao dois
/// 
/// eh_reveillon("2000/12/30")
/// let mes = string.slice("2000/12/30", 5, 2)
/// let dia = string.slice("2000/12/30", 8, 2)
/// let mes = "12"
/// let dia = "30"
/// case "12" == "12"{
///     True-> 
///         case "30" == "31"{
///             True -> True
///             False-> False
///          } 
///      False -> False
/// }
/// como 30 != 31 o codigo devolve False.
/// 
/// 
/// 
/// Questao 3:
/// recebe um texto qualquer, *texto*, porem uma limitação é que temos uma quantidade fixa de 5 caracteres.
/// caso o *texto* tiver mais de *5* caracteres, adiciona *...* na frente, caso *texto* tiver menos que *5* caracters
/// aadiciona *  * (espaco em branco) nos caracteres restantes, caso o *texto* tiver *5* caracteres, retorna o *texto* sem
/// mudar     
pub fn tamanho(texto: String) -> String {
  let tamanho = string.length(texto)
  let x = 5 - tamanho
  let espaco = string.repeat(" ", x)

  case string.length(texto) > 5 {
    True -> string.slice(texto, 0, 2) <> "..."
    False ->
      case string.length(texto) < 5 {
        True -> texto <> espaco
        False -> texto
      }
  }
}

///Função para textes da função *tamanho*
///Primeiro exemplo com *texto* contendo 
/// tamanho *5*, logo, retorna sem alteração
/// segundo exemplo com *Texto* contendo
/// mais de *5* caracteres, logo retorna
/// com *...*
/// Terceiro exemplo com *texto* contendo 
/// menos que *5* caracteres, logo 
/// adiciona * * (espaço em branco)
pub fn tamanho_examples() {
  check.eq(tamanho("texto"), "texto")
  check.eq(tamanho("textos"), "te...")
  check.eq(tamanho("abc"), "abc  ")
  check.eq(tamanho("text"), "text ")
}
