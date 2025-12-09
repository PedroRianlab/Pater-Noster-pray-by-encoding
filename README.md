# 🕊️ pater-noster-pray-in-code (Fast Guide)

Guia rápido da linguagem esotérica e do tradutor Sacerdos.

## Como rodar

1. Salve o código com extensão `.pn`.
2. Inclua exatamente **uma** oração iniciatória (veja abaixo). "Não declarar a oração iniciatória faz o sacerdos não traduzir e gera uma mensagem personalizada no terminal"
3. Rode a tradução: `python sacerdos_translator.py <arquivo>.pn` → gera `<arquivo>.py`.
4. Execute o `.py`: `python <arquivo>.py`.
   > Requisito: Python 3 instalado e `sacerdos_translator.py` no mesmo diretório.

## Orações iniciatórias (copie o texto completo)

- **SACRAMENTO**
  - `OREMOS { SACRAMENTO } = "Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição";`
- **FÉ**
  - `OREMOS { FÉ } = "Tu és minha vida, outro Deus não há Tu és minha estrada, a minha verdade Em Tua palavra eu caminharei Enquanto eu viver e até quando Tu quiseres Já não sentirei temor, pois estás aqui Tu estás no meio de nós";`
- **CONVERSÃO**
  - `OREMOS { CONVERSÃO } = "Tarde te amei, ó beleza tão antiga e tão nova! Tarde demais eu te amei! Eis que habitavas dentro de mim e eu te procurava do lado de fora";`

## Estrutura mínima

```pn
OREMOS { SACRAMENTO } = "...texto completo...";

PAI_NOSSO() {
    // código
}
AMÉM;
```

## Tipos e declaração

| Token                            | Significado | Observações                                         |
| :------------------------------- | :---------- | :-------------------------------------------------- |
| `BATISMO ÁGUA nome = 0;`         | inteiro     | obrigatório usar `BATISMO` na declaração            |
| `BATISMO VINHO nome = "texto";`  | string      | aceita texto entre aspas                            |
| `BATISMO PÃO nome = VERDADEIRO;` | boolean     | **não** aceite `FALSO`: o tradutor encerra com erro |

### Regra especial do PÃO (verdade obrigatória)

- O tradutor encerrra o proceso se detectar atribuição literal de `FALSO/False/falso` a um `PÃO`.
- Entradas de usuário (ex.: `OUVI_A_VOZ`) não são barradas: se o usuário digitar 0, o valor 0 irá para a variável. Se precisar impedir isso, valide explicitamente e use `PERDOAI(var)` ou converta para `VERDADEIRO` conforme a sua regra.

## Comandos principais

| Comando                                                 | Equivalente | Observações                                             |
| :------------------------------------------------------ | :---------- | :------------------------------------------------------ |
| `PAI_NOSSO(){ ... }`                                    | `main`      | bloco raiz                                              |
| `AMÉM`                                                  | fim         | fecha o programa                                        |
| `VOSSO_REINO nome(){`                                   | `def`       | define função                                           |
| `VENHA_A_NÓS nome(args);`                               | chamada     | use após declarar a função                              |
| `VOSSA_VONTADE expr`                                    | `return`    | retorna de uma função                                   |
| `SE_FOR_VOSSA_VONTADE (condição) {`                     | `if`        | aceita também grafia `SE_POR_VOSSA_VONTADE`             |
| `SE_NÃO_FOR_VOSSA_VONTADE (condição) {`                 | `elif`      | se tiver condição vira `elif`; sem condição vira `else` |
| `ENQUANTO_EU_VIVERES_E_ATÉ_QUANDO_TU_QUISERES (cond) {` | `while`     | aceita também `..._ATE_...` sem acento                  |

## Incremento/Decremento

O tradutor entende o padrão `variavel; COMANDO;` (com ponto e vírgula):

- `contador; AUMENTAI_MINHA_FÉ;` → `contador += 1`
- `contador; NAO_TEMEREI_O_MAL;` → `contador -= 1`

## Entrada e saída

- `TRANSFORMAI_EM_VINHO("texto", args...)` imprime; se houver `%d/%s` usa formatação tipo `printf`.
- `OUVI_A_VOZ(var)` lê `input` e converte para `int`.

## Exemplo Obrigatório: Hello World da linguagem

```pn
OREMOS { SACRAMENTO } = "Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição";

PAI_NOSSO() {
  TRANSFORMAI_EM_VINHO("Hello, World!");
}
AMÉM;
```

## Exemplo Obrigatório: 02 (99 Hóstias (adaptação do 99 garrafas de cerveja))

```pn
// --- ORAÇÕES INICIATÓRIAS ---
OREMOS { SACRAMENTO } = "Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição";

PAI_NOSSO() {
    BATISMO ÁGUA hostias = 99;

    // Loop ENQUANTO (While loop)
    ENQUANTO_EU_VIVERES_E_ATE_QUANDO_TU_QUISERES(hostias > 0) {
        SE_FOR_VOSSA_VONTADE (hostias > 1) {
            TRANSFORMAI_EM_VINHO("%d hostias no altar, %d hostias de Cristo.", hostias, hostias);
            hostias; NAO_TEMEREI_O_MAL;
            TRANSFORMAI_EM_VINHO("Tirai uma e dai ao fiel, %d hostia(s) no altar agora.", hostias);
        }
        SE_NAO_FOR_VOSSA_VONTADE (hostias == 1) {
            TRANSFORMAI_EM_VINHO("A ultima hostia de Cristo esta no altar!");
            hostias; NAO_TEMEREI_O_MAL;
            TRANSFORMAI_EM_VINHO("Dai a ultima ao fiel. Nao ha mais hostias no altar.");
        }
    }

    TRANSFORMAI_EM_VINHO("\n\nO Banquete Sagrado terminou. Amem.");
}
AMÉM;
```

## Exemplo Aberto: Ritual da Eucaristia (entrada + reset)

```pn
// --- RITUAL DE INICIALIZAÇÃO (NECESSÁRIO PARA O TRADUTOR) ---
OREMOS { SACRAMENTO } = "Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição";

PAI_NOSSO() {
  // Declaração de variável (PÃO = Booleano/Flag)
  BATISMO PÃO estado_de_graca;

  TRANSFORMAI_EM_VINHO("\n--- SACRAMENTO DA EUCARISTIA ---");
  TRANSFORMAI_EM_VINHO("Você está em estado de graça? (Digite 1 para Sim, 0 para Nao):");

  // Entrada de dados (OUVI_A_VOZ) -> O tradutor converte para int(input(...))
  OUVI_A_VOZ(estado_de_graca);

  // --- BLOCO DE SUCESSO (IF) ---
  SE_FOR_VOSSA_VONTADE (estado_de_graca == 1) {
    TRANSFORMAI_EM_VINHO("\nO Corpo de Cristo foi recebido. Amém!");
  }

  // --- BLOCO DE FALHA (IF SEPARADO) ---
  // Isto substitui o ELSE, pois evita o bug de alinhamento.
  SE_FOR_VOSSA_VONTADE (estado_de_graca != 1) {
    TRANSFORMAI_EM_VINHO("\nVocê precisa se confessar antes de receber o Sacramento.");
    // Reset da variável (PERDOAI)
    PERDOAI(estado_de_graca);
  }

  TRANSFORMAI_EM_VINHO("\nProcesso finalizado.");
}
AMÉM;
```

# Inspirações

## 🎵 “Estás entre nós” — Criação da biblioteca **Fé**, laços de repetição, incremento, decremento

[Assista aqui](https://www.youtube.com/watch?v=5koIaw4nS2I)

## 🎵 “Tarde te Amei” — Criação da biblioteca **Conversão**

[Assista aqui](https://www.youtube.com/watch?v=YgawtDM1oug)

## 🎵 “O Bom Pastor” — Criação da biblioteca **Eucaristia**

[Assista aqui](https://www.youtube.com/watch?v=rzZeLsBmKG4)
