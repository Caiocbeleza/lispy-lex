import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str

def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    tokens = [
        ("LPAR", r"\("),
        ("RPAR", r"\)"),
        ("CHAR", r"#\\[a-zA-Z]*"),
        ("STRING", r"\".*\""),   
        ("NUMBER", r"(\+|\-|)?\d+(\.\d*)?"),
        ("NAME", r"([a-zA-Z_%\+\-]|\.\.\.)[a-zA-Z_0-9\-\>\?\!]*"),         
        ("BOOL", r"#[t|f]"),
        ("QUOTES", r"[\'\"]"),
        ("COMMA", r","),
        ("NEWLINE",  r"\\n"),

    ]
    
    regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)

    string = re.sub(r";;.*", "", code)

        
    for mo in re.finditer(regex, string):
        kind = mo.lastgroup
        value = mo.group()
        yield Token(kind, value)

    return [Token('INVALIDA', 'valor inválido')]