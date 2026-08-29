//atividade 3 
import gleam/string
pub fn add_numero_nove(num: String) -> String  {
  let inicio = string.slice(num, 0, 4)
  let com_nove = string.append(inicio, "9")
  let resto = string.slice(num, 4, string.byte_size(num))
  case string.byte_size(num) > 14 || string.byte_size(num) < 13{
  True -> "Numero invalido, colque o parenteses e o "
  False -> 
    case string.byte_size(num) == 13{
    True -> string.append(com_nove,resto)
    False -> num
    }
  }

}