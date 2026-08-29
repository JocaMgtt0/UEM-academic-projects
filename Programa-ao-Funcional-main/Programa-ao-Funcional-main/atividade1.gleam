import gleam/string
import sgleam/check

// Exercício 1

/// Devolve True *s* começa e termina com o mesmo caratere, False caso
/// contrário.
pub fn comeco_fim_igual(s: String) -> Bool {
  s != "" && string.slice(s, 0, 1) == string.slice(s, -1, 1)
}

pub fn comeco_fim_igual_examples() {
  check.eq(comeco_fim_igual("ana"), True)
  check.eq(comeco_fim_igual("abacate"), False)
  check.eq(comeco_fim_igual("b"), True)
  check.eq(comeco_fim_igual(""), False)
}

// Exercício 2

// comeco_fim_igual("agua" <> "boa")

// comeco_fim_igual("aguaboa")

// "aguaboa" != "" && string.slice("aguaboa", 0, 1) == string.slice("aguaboa", -1, 1)

// True && string.slice("aguaboa", 0, 1) == string.slice("aguaboa", -1, 1)

// string.slice("aguaboa", 0, 1) == string.slice("aguaboa", -1, 1)

// "a" == string.slice("aguaboa", -1, 1)

// "a" == "a"

// True


// Exercício 3

// Análise
// Adicionar o nono dígito a um número de telefone se ele ainda não tem nove dígitos.

// No formato (XX) XXXXX-XXXX ou (XX) XXXX-XXXX onde X é um dígito
pub type NumeroTelefone =
  String

/// Adiciona "9" como o nono dígito em *numero* se ele ainda não tiver o nono dígito.
pub fn adiciona_nono_digito(numero: NumeroTelefone) -> NumeroTelefone {
  case string.length(numero) == 14 {
    True -> string.slice(numero, 0, 5) <> "9" <> string.slice(numero, 5, 9)
    False -> numero
  }
}

pub fn adiciona_nono_digitos_examples() {
  check.eq(adiciona_nono_digito("(44) 9787-1241"), "(44) 99787-1241")
  check.eq(adiciona_nono_digito("(51) 95872-9989"), "(51) 95872-9989")
}
