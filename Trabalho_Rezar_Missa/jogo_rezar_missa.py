# -*- coding: utf-8 -*-
# Script traduzido pelo Sacerdos v3.16 (Versão Estável Corrigida)
import sys

# Definição do bloco principal PAI_NOSSO
def main():
    pontuacao = 0
    posicao_atual = 0
    escolha = 0
    acao_correta = 0
    jogando = 1
    entrada_invalida = 0
    print("\n\n")
    print("  ===================================================")
    print("              JOGO DA MISSA SAGRADA")
    print("  ===================================================")
    print("")
    print("                        +")
    print("                       +++")
    print("                        +")
    print("                     +++++++")
    print("                        +")
    print("                        +")
    print("                        +")
    print("\n")
    print("========== BEM-VINDO AO JOGO DA SANTA MISSA ==========")
    print("Você está na plateia acompanhando a celebração sagrada.")
    print("Siga os movimentos e as orações com reverência!")
    print("Faça as escolhas corretas em cada momento da missa!")
    print("======================================================\n")
    print("\n********** PARTE 1: RITOS INICIAIS **********\n")
    print("\n--- Entrada: Canto de entrada e procissão ---")
    print("O sacerdote e os ministros entram em procissão enquanto cantamos ou ouvimos o cântico de entrada.")
    print("Pontuação: %d\n" % ( pontuacao))
    print("1 - Levantar e acompanhar a procissão")
    print("2 - Sentar")
    print("3 - Ajoelhar")
    print("4 - Cantar o cântico")
    print("5 - Deixar a mente vagar em preocupações mundanas")
    print("Sua escolha: ")
    entrada_invalida = 1
    while entrada_invalida != 0:
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        if escolha >= 1:
            if escolha <= 5:
                entrada_invalida = 0 # PERDOAI: Variável resetada para 0
            elif escolha <= 5:
                print("⚠ Digite um número de 1 a 5!")
        elif escolha >= 1:
            print("⚠ Digite um número de 1 a 5!")
    acao_correta = 1
    if escolha == 5:
        print("\n✗ Sua mente se fechou ao momento sagrado. Enquanto a procissão avançava em reverência, você permaneceu interiormente ausente.")
        print("A desatenção voluntária criou uma barreira entre você e o Mistério que se iniciava.")
        print("Fim de jogo.")
        jogando = 0 # PERDOAI: Variável resetada para 0
    if escolha == acao_correta:
        if jogando != 0:
            print("\n✝ Correto! Você se levantou com reverência para a entrada!")
            pontuacao += 1
            posicao_atual = 1
    if escolha != acao_correta:
        if jogando != 0:
            print("\n✗ Errado! O correto era LEVANTAR.")
    if jogando != 0:
        print("\n--- Saudação e Sinal da Cruz ---")
        print("O sacerdote faz o sinal da cruz e saúda o povo. Responda: 'E com o vosso espírito'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Responder")
        if posicao_atual != 1:
            print("1 - Levantar e Responder")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Fechar-se interiormente ao diálogo com Deus")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Seu coração se fechou ao chamado de Deus. A soberba silenciosa impediu que você reconhecesse sua necessidade de perdão.")
            print("Sem abertura para a reconciliação, você não pôde receber as graças que a Missa oferecia.")
            print("Fim de jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé com disposição de conversão!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n--- Ato Penitencial (Confiteor) ---")
        print("Reconhecimento e pedido de perdão pelos pecados. Recite: 'Eu confesso a Deus todo-poderoso...'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Recitar")
        if posicao_atual != 1:
            print("1 - Levantar e Recitar")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Reter mágoa e recusa de perdoar a alguém presente")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ O ressentimento endureceu seu coração. Ao recusar perdoar, você impediu que a Graça tocasse a raiz da sua alma.")
            print("A Missa não pode sanctificar quem segue agarrado à recordação da injúria, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n--- Glória ---")
        print("Hino de louvor à Santíssima Trindade. Cante/Recite: 'Glória a Deus nas alturas...'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Cantar")
        if posicao_atual != 1:
            print("1 - Levantar e Cantar")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Deixar a vaidade controlar seus pensamentos durante o louvor")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Enquanto cantava o Glória, seu coração se voltou para si mesmo. A vaidade roubou a sinceridade da sua adoração.")
            print("Você louvou a Deus, mas pensava em si. A desconexão espiritual se aprofundou, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n--- Oração da Coleta ---")
        print("O sacerdote faz a oração que introduz a liturgia do dia. Responda ao final: 'Amém'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Responder Amém")
        if posicao_atual != 1:
            print("1 - Levantar e Responder Amém")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Julgar silenciosamente a oração dos outros à sua volta")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Enquanto deveria responder a Deus, você criticava seus irmãos. O julgamento crítico ocupou o lugar da caridade.")
            print("A comunidade se fragmentou em seu coração, e você ficou apartado do Corpo de Cristo, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n\n********** PARTE 2: LITURGIA DA PALAVRA **********\n")
    if jogando != 0:
        print("\n--- Primeira Leitura (Antigo Testamento) ---")
        print("O leitor proclama a Palavra de Deus. Ao final responda: 'Graças a Deus'")
        print("Pontuação: %d\n" % ( pontuacao))
        print("1 - Levantar e se distrair")
        if posicao_atual == 2:
            print("2 - Continuar Sentado e Responder Graças a Deus")
        if posicao_atual != 2:
            print("2 - Sentar e Responder Graças a Deus")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Você se recusa a ouvir pois já conhece a leitura")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 2
        if escolha == 5:
            print("\n✗ Por soberba, ao se recusar a ouvir, por julgar que já conhecia a leitura, você fechou o coração para o que Deus queria dizer hoje.")
            print("A Palavra não se repete, quem se fecha é quem a escuta. Você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se sentou para ouvir a Palavra!")
                pontuacao += 1
                posicao_atual = 2
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era SENTAR.")
    if jogando != 0:
        print("\n--- Salmo Responsorial ---")
        print("Resposta cantada ou rezada ao salmo. Responda o refrão junto com o cantor/leitor.")
        print("Pontuação: %d\n" % ( pontuacao))
        print("1 - Levantar")
        if posicao_atual == 2:
            print("2 - Continuar Sentado e Responder o Refrão")
        if posicao_atual != 2:
            print("2 - Sentar e Responder o Refrão")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Questionar silenciosamente a verdade que está sendo proclamada")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 2
        if escolha == 5:
            print("\n✗ Enquanto a Palavra de Deus ecoava, seu espírito permaneceu fechado em desconfiança. O orgulho da razão impediu que você ouvisse com fé.")
            print("Sem abertura ao Evangelho, a Semente não pôde germinar em seu coração, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu sentado!")
                pontuacao += 1
                posicao_atual = 2
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar SENTADO.")
    if jogando != 0:
        print("\n--- Segunda Leitura (Novo Testamento) ---")
        print("Leitura das cartas apostólicas. Ao final responda: 'Graças a Deus'")
        print("Pontuação: %d\n" % ( pontuacao))
        print("1 - Levantar")
        if posicao_atual == 2:
            print("2 - Continuar Sentado e Responder")
        if posicao_atual != 2:
            print("2 - Sentar e Responder")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Deixar a mente divagar em coisas materiais que deseja")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 2
        if escolha == 5:
            print("\n✗ Enquanto a Palavra era proclamada, seus pensamentos se prenderem ao que você ambiciona. A cobiça distraiu seu coração da verdade eterna.")
            print("Você ouviu com os ouvidos, mas não com o espírito, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu sentado!")
                pontuacao += 1
                posicao_atual = 2
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar SENTADO.")
    if jogando != 0:
        print("\n--- Aclamação ao Evangelho (Aleluia) ---")
        print("Canto que precede o Evangelho. Responda: 'Aleluia, Aleluia, Aleluia!'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Responder Aleluia")
        if posicao_atual != 1:
            print("1 - Levantar e Responder Aleluia")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Bolsa de dinheiro esquecida no chão")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Você saiu para ficar com o dinheiro encontrado e perdeu a missa. A cobiça te afastou do pão celeste, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se levantou para o Aleluia!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era LEVANTAR.")
    if jogando != 0:
        print("\n--- Evangelho ---")
        print("Proclamação do Santo Evangelho.Antes: Cruz Tripla e ao final: 'Glória a vós, Senhor'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé fazer a Cruz e Responder")
        if posicao_atual != 1:
            print("1 - Levantar e Responder")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Deixar a mente fluir entre fantasias e desejos")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Quando deveria estar em pé para saudar o Cristo que vem, seus pensamentos permaneciam dispersos. A falta de domínio interior o deixou desconectado.")
            print("Você não estava verdadeiramente presente para o Evangelho, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n--- Homilia ---")
        print("O sacerdote explica a Palavra de Deus. Escute com atenção e reflita.")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Escutar com atenção")
        if posicao_atual != 1:
            print("1 - Levantar e Escutar com atenção")
        print("2 - Sentar e Escutar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Ocupar-se em críticas interiores às palavras do sacerdote")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 2
        if escolha == 5:
            print("\n✗ Enquanto o sacerdote procurava transmitir a Mensagem, você permanecia julgando e questionando. O espírito crítico impediu que você recebesse a Graça.")
            print("A dureza do coração deixou você apartado da verdade sendo proclamada, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se sentou para escutar a homilia!")
                pontuacao += 1
                posicao_atual = 2
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era SENTAR e escutar com atenção.")
    if jogando != 0:
        print("\n--- Profissão de Fé (Creio) ---")
        print("Recitação do Credo. Responda: 'Creio em um só Deus, Pai todo-poderoso...'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Recitar")
        if posicao_atual != 1:
            print("1 - Levantar e Recitar")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Alguém fora da igreja zomba do credo e você sai para defender agressivamente a sua fé")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Sua defesa agressiva da fé afastou você da mansidão que Cristo pregava. O orgulho apostólico rompeu a comunhão,")
            print("você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se levantou para o Creio!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era LEVANTAR.")
    if jogando != 0:
        print("\n--- Oração dos Fiéis ---")
        print("Orações pela Igreja e pelo mundo. Responda: 'Atendei-nos, Senhor' após cada intenção")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Responder")
        if posicao_atual != 1:
            print("1 - Levantar e Responder")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Recusar se unir aos outros em oração por soberba espiritual")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Você se isolou da comunidade de fé. A soberba silenciosa impediu que você se solidarizasse com os irmãos em oração.")
            print("Sem comunhão com o Povo de Deus, você ficou sozinho e longe do Corpo Místico, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n\n********** PARTE 3: LITURGIA EUCARÍSTICA **********\n")
    if jogando != 0:
        print("\n--- Preparação dos Dons ---")
        print("Oferta do pão e vinho. Prepare-se interiormente e responda ao final: 'Bendito e louvado seja...'")
        print("Pontuação: %d\n" % ( pontuacao))
        print("1 - Levantar")
        if posicao_atual == 2:
            print("2 - Continuar Sentado e Responder")
        if posicao_atual != 2:
            print("2 - Sentar e Responder")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Entregar dons materiais mas com espírito de comparação")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 2
        if escolha == 5:
            print("\n✗ Enquanto oferecia os dons, seu coração media seu sacrifício contra o dos outros. A comparação envenenou o ato de doação.")
            print("Você ofereceu para ser visto, não para dar a Deus. A oferenda perdeu seu valor espiritual, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se sentou durante a preparação!")
                pontuacao += 1
                posicao_atual = 2
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era SENTAR.")
    if jogando != 0:
        print("\n--- Oração Eucarística (Consagração) ---")
        print("Momento solene da Consagração do Pão e Vinho. Responda reverentemente: 'Amém'")
        print("Pontuação: %d\n" % ( pontuacao))
        print("1 - Levantar")
        print("2 - Sentar")
        if posicao_atual == 3:
            print("3 - Continuar Ajoelhado e Responder Amém")
        if posicao_atual != 3:
            print("3 - Ajoelhar e Responder Amém")
        print("4 - Apenas Orar")
        print("5 - Cansaço extremo te chamando para desistir")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 3
        if escolha == 5:
            print("\n✗ A preguiça espiritual venceu sua determinação. No momento em que deveria estar em silêncio adorador, você se retirou.")
            print("Sua ausência neste ápice sagrado rompeu a ponte entre você e o Mistério da Redenção, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se ajoelhou para a Consagração!")
                pontuacao += 1
                posicao_atual = 3
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era AJOELHAR.")
    if jogando != 0:
        print("\n--- Cântico do Cordeiro (Agnus Dei) ---")
        print("Canto antes da comunhão. Responda: 'Cordeiro de Deus que tirais os pecados do mundo, tende piedade de nós'")
        print("Pontuação: %d\n" % ( pontuacao))
        print("1 - Levantar")
        print("2 - Sentar")
        if posicao_atual == 3:
            print("3 - Continuar Ajoelhado e Responder")
        if posicao_atual != 3:
            print("3 - Ajoelhar e Responder")
        print("4 - Apenas Orar")
        print("5 - Cheiro de pizza")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 3
        if escolha == 5:
            print("\n✗ Você saiu da igreja para satisfazer uma fome passageira e, ao voltar, a Missa já havia terminado.")
            print("Ao trocar o Banquete Eucarístico por algo momentâneo, perdeu o encontro que dá sentido a todos os outros.")
            print("Fim de jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se levantou com reverência para a entrada!")
                pontuacao += 1
                posicao_atual = 3
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar AJOELHADO.")
    if jogando != 0:
        print("\n--- Comunhão (Corpo e Sangue de Cristo) ---")
        print("Momento de receber a Eucaristia. Dirija-se ao sacerdote e responda: 'Amém'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e comungar (se estiver sem pecado mortal)")
        if posicao_atual != 1:
            print("1 - Levantar e comungar (se estiver sem pecado mortal)")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Bolsa de dinheiro esquecida no chão")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Você saiu para ficar com o dinheiro encontrado e perdeu a missa. A cobiça te afastou do pão celeste, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se levantou para comungar!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era LEVANTAR.")
    if jogando != 0:
        print("\n\n********** PARTE 4: RITOS FINAIS **********\n")
    if jogando != 0:
        print("\n--- Oração Pós-Comunhão ---")
        print("Agradecimento pelas graças recebidas. Responda ao final: 'Amém'")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé e Responder")
        if posicao_atual != 1:
            print("1 - Levantar e Responder")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Apenas Orar")
        print("5 - Permitir que o repouso depois da Comunhão seja preenchido por pensamentos triviais")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Após receber a Eucaristia, você não guardou o repouso contemplativo. O mundo invadiu sua alma logo após o encontro com Cristo.")
            print("A falta de silêncio interior anulou a ação da Graça, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n--- Avisos e Comunicações ---")
        print("Informações breves à comunidade.")
        print("Pontuação: %d\n" % ( pontuacao))
        print("1 - Levantar")
        if posicao_atual == 2:
            print("2 - Continuar Sentado")
        if posicao_atual != 2:
            print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Orar")
        print("5 - Pessoa zombando da sua fé")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 2
        if escolha == 5:
            print("\n✗ A ira te cegou e você partiu para o confronto. O lugar de paz se tornou palco de desordem por sua falta de paciência.")
            print("A comunidade perdeu um membro capaz de testemunho humilde, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se sentou para os avisos!")
                pontuacao += 1
                posicao_atual = 2
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era SENTAR.")
    if jogando != 0:
        print("\n--- Bênção Final ---")
        print("O sacerdote abençoa o povo.")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé")
        if posicao_atual != 1:
            print("1 - Levantar")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Orar")
        print("5 - Recusar interiormente a bênção por sentimento de indignidade")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Seu coração se fechou à generosidade de Deus. Ao recusar a bênção por sentimento falso de indignidade, você bloqueou a Graça que queria abraçá-lo.")
            print("A desconfiança na misericórdia divina afastou você da proteção que Deus oferecia para sua jornada, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você se levantou para a bênção!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era LEVANTAR.")
    if jogando != 0:
        print("\n--- Despedida ---")
        print("'Ide em paz, aleluia!' - O sacerdote se retira.")
        print("Pontuação: %d\n" % ( pontuacao))
        if posicao_atual == 1:
            print("1 - Continuar em Pé")
        if posicao_atual != 1:
            print("1 - Levantar")
        print("2 - Sentar")
        print("3 - Ajoelhar")
        print("4 - Orar")
        print("5 - Sair da Missa sem deixar levar a Graça para o mundo")
        print("Sua escolha: ")
        escolha = int(input("Insira o valor para escolha: ")) # Converte input para ÁGUA/Inteiro
        acao_correta = 1
        if escolha == 5:
            print("\n✗ Você se recusou interiormente a ser instrumento da Graça. A indiferença frente ao chamado de levar Cristo ao mundo apartou você do propósito sagrado da Missa.")
            print("Sem deixar o encontro com Cristo transformar sua missão, você perdeu a oportunidade de ser apóstolo no cotidiano, você perdeu o jogo.")
            jogando = 0 # PERDOAI: Variável resetada para 0
        if escolha == acao_correta:
            if jogando != 0:
                print("\n✝ Correto! Você permaneceu em pé até o final!")
                pontuacao += 1
                posicao_atual = 1
        if escolha != acao_correta:
            if jogando != 0:
                print("\n✗ Errado! O correto era ficar EM PÉ.")
    if jogando != 0:
        print("\n\n========== FIM DA SANTA MISSA ==========")
        print("Você completou toda a celebração!")
        print("Pontuação final: %d/21" % ( pontuacao))
        print("\nQue Deus vos abençoe e guarde sempre!")
        print("Ide em paz e o Senhor vos acompanhe!")
    print("\n\nAmém.")


def confessa_teus_pecados():
    print('Tiago 5:16 — Confessai, pois, os vossos pecados uns aos outros e orai uns pelos outros, para que sareis.')
    resposta = input('Tens pecados a confessar? (s/n): ').strip().lower()
    if resposta not in ('s', 'n'):
        print('Resposta inválida. Use s/n.')
        sys.exit(1)
    if resposta == 'n':
        print('Segue em paz e permanece em graça.')
        return
    quer = input('Desejas te confessar agora? (s/n): ').strip().lower()
    if quer == 's':
        input('Confessa teus pecados: ')  # conteúdo não é usado, ato simbólico
        print('Absolvido. Vai em paz e ora pelos irmãos.')
        return
    print('Execução interrompida: a confissão foi recusada. Que o Senhor te conduza ao arrependimento.')
    sys.exit(1)


# Bloco de execução principal do Python
if __name__ == '__main__':
    confessa_teus_pecados()
    main()