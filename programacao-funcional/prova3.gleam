import gleam/list
import sgleam/check
import gleam/string

///retorna os nomes na  lista *lst* de nomes que possuem mais de 5 caracter
pub fn nomes(lst: List(String)) -> List(String) {

  list.filter(lst, fn(nome) { string.length(nome) > 5 })
  
}

pub fn nomes_examples(){

    check.eq(nomes(["pedrao"]), ["pedrao"])
    check.eq(nomes([]), [])
    check.eq(nomes(["carla"]), [])
    check.eq(nomes(["pedrao", "carlao"]), ["pedrao", "carlao"])
}



///retorna o caracter de uma lista *lst* que esta no indice *id*
pub fn caractere(lst: List(String), id: Int) -> List(String){

  list.map(lst, fn(s) {
    case string.slice(s, id, 1) {
      "" -> ""
      char -> char
    }
  })
}

pub fn caractere_examples() {
  check.eq(caractere(["bola", "casa", "cama"], 0), ["b", "c", "c"])
  check.eq(caractere(["carlos", "pedro", "marcos"], 2), ["r", "d", "r"])
  check.eq(caractere(["", "", ""], 2), ["", "", ""])
}


/// retorna uma nova lista *lst* removendo as primeiras ocorrências dos elementos repetidos
pub fn ocorrencia(lst: List(a)) -> List(a) {
  list.fold(lst, [], fn(acc, elem) {
    list.append(
      acc,
      list.filter([elem], fn(x) { !list.contains(acc, x) })
    )
  })
}

pub fn ocorrencia_examples(){
    check.eq(ocorrencia([1,2,3,3,4]), [1,2,3,4])
    check.eq(ocorrencia([]), [])
    check.eq(ocorrencia([1,1,2,2,3,3]), [1,2,3])
}


/// retorna quantas vezes um elemento aparece em uma lista 
pub fn conta_vezes(lst: List(a), elem: a) -> Int {
  conta_aux(lst, elem, 0)
}

fn conta_aux(lst: List(a), elem: a, acc: Int) -> Int {
  case lst {
    [] -> acc
    [p, ..resto] ->
      case p == elem {
        True -> conta_aux(resto, elem, acc + 1)
        False -> conta_aux(resto, elem, acc)
      }
  }
}

pub fn conta_vezes_examples(){

    check.eq(conta_vezes([], 2), 0)
    check.eq(conta_vezes([], 0), 0)
    check.eq(conta_vezes([1,2,3,3], 3), 2)
    check.eq(conta_vezes([1,1,1,2,2,3,1], 1), 4)
}



