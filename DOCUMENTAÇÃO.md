# pater-noster-pray-in-code — Guia completo de sintaxe

Linguagem esotérica onde cada construção é inspirada em símbolos litúrgicos. Este guia reflete o comportamento real do tradutor `sacerdos_translator.py`.

## 1) Oração iniciatória obrigatória (copie literalmente)

Escolha **uma** das três e mantenha o texto exato:

```
OREMOS { SACRAMENTO } = "Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição";

OREMOS { FÉ } = "Tu és minha vida, outro Deus não há Tu és minha estrada, a minha verdade Em Tua palavra eu caminharei Enquanto eu viver e até quando Tu quiseres Já não sentirei temor, pois estás aqui Tu estás no meio de nós";

OREMOS { CONVERSÃO } = "Tarde te amei, ó beleza tão antiga e tão nova! Tarde demais eu te amei! Eis que habitavas dentro de mim e eu te procurava do lado de fora";
```

## 2) Estrutura básica

```pn
OREMOS { SACRAMENTO } = "...";

PAI_NOSSO() {
    // código
}
AMÉM;
```

## 3) Tipos e declaração (BATISMO)

- Sempre declare com `BATISMO <TIPO> nome = valor;`
- Tipos disponíveis:
  - `ÁGUA` → inteiro
  - `VINHO` → texto/string
  - `PÃO` → booleano (apenas `VERDADEIRO` é aceito; `FALSO` aborta a tradução)

Exemplos:

```pn
BATISMO ÁGUA contador = 0;
BATISMO VINHO saudacao = "Pax et bonum";
BATISMO PÃO vela_acesa = VERDADEIRO;
```

## 4) Comandos principais

| Comando                                               | Equivalente  | Notas                                   |
| :---------------------------------------------------- | :----------- | :-------------------------------------- |
| `PAI_NOSSO(){ ... }`                                  | bloco `main` | raiz do programa                        |
| `AMÉM`                                                | fim          | encerra o script                        |
| `VOSSO_REINO nome(){`                                 | `def`        | define função                           |
| `VENHA_A_NÓS nome(args);`                             | chamada      | usa função definida                     |
| `VOSSA_VONTADE expr`                                  | `return`     | retorna valor                           |
| `SE_FOR_VOSSA_VONTADE (cond){`                        | `if`         | aceita também `SE_POR_VOSSA_VONTADE`    |
| `SE_NÃO_FOR_VOSSA_VONTADE (cond){`                    | `elif`       | se tiver condição vira `elif`           |
| `SE_NÃO_FOR_VOSSA_VONTADE {`                          | `else`       | sem condição vira `else`                |
| `ENQUANTO_EU_VIVERES_E_ATÉ_QUANDO_TU_QUISERES(cond){` | `while`      | aceita grafia sem acento: `..._ATE_...` |

## 5) Incremento e decremento

O tradutor entende o padrão **`variavel; COMANDO;`** (com ponto e vírgula):

```pn
contador; AUMENTAI_MINHA_FÉ;    // contador += 1
contador; NAO_TEMEREI_O_MAL;    // contador -= 1
```

## 6) Entrada e saída

- `TRANSFORMAI_EM_VINHO("texto", args...)` → `print`. Se houver `%d/%s`, usa formatação ao estilo `printf`.
- `OUVI_A_VOZ(nome)` → lê `input` e converte para `int`.
- `PERDOAI(nome)` → zera a variável (`nome = 0`).

## 7) Regras de blocos

- Cada `{` abre indentação; cada `}` fecha.
- `SE_NÃO_FOR_VOSSA_VONTADE` com condição deve vir após um `SE_FOR_VOSSA_VONTADE` ou outro `SE_NÃO_FOR_VOSSA_VONTADE` para formar `elif`.
- A mensagem final fora do loop deve ficar após o `}` do `ENQUANTO`.

## 8) Exemplo completo (contagem de hóstias)

````

## 9) Exemplos adicionais

### Milagre da multiplicação (função + chamada)
```pn
OREMOS { SACRAMENTO } = "Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição";

VOSSO_REINO milagre(pao_peixe) {
    BATISMO ÁGUA resultado = pao_peixe * 2;
    VOSSA_VONTADE resultado;
}

PAI_NOSSO() {
    BATISMO ÁGUA multiplica = VENHA_A_NÓS milagre(5);
    TRANSFORMAI_EM_VINHO("Resultado: %d", multiplica);
}
AMÉM;
````

### Loop de Glória (while + incremento suportado pelo tradutor)

```pn
OREMOS { SACRAMENTO } = "Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição";

PAI_NOSSO() {
    BATISMO ÁGUA i = 0;

    ENQUANTO_EU_VIVERES_E_ATÉ_QUANDO_TU_QUISERES(i < 3) {
        TRANSFORMAI_EM_VINHO("Glória!");
        i; AUMENTAI_MINHA_FÉ;   // incrementa i += 1 (forma aceita pelo tradutor)
    }
}
AMÉM;
```
