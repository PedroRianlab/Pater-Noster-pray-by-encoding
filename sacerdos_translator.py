import sys
import re
import unicodedata 


INDENT_CHAR = "    " 



ORAZOES_VALIDAS = {
    # 1. SACRAMENTO (Obrigatório em MAIÚSCULAS e com Citação Exata)
    "OREMOS { SACRAMENTO } = \"Sou Rei, sou o Bom Pastor! Vinde ao banquete que vos preparei E fome jamais tereis! A quem vamos, ó Senhor? Só tu tens palavras de vida E te dás em refeição\";": "SACRAMENTO",
    # 2. FÉ
    "OREMOS { FÉ } = \"Tu és minha vida, outro Deus não há Tu és minha estrada, a minha verdade Em Tua palavra eu caminharei Enquanto eu viver e até quando Tu quiseres Já não sentirei temor, pois estás aqui Tu estás no meio de nós\";": "FÉ",
    # 3. CONVERSÃO
    "OREMOS { CONVERSÃO } = \"Tarde te amei, ó beleza tão antiga e tão nova! Tarde demais eu te amei! Eis que habitavas dentro de mim e eu te procurava do lado de fora\";": "CONVERSAO"
}

# --- 2. FUNÇÕES DE VALIDAÇÃO E ERRO ---

def validar_obrigacoes_liturgicas(code_content):
    """Verifica se pelo menos uma oração válida foi invocada."""
    for oracao_completa in ORAZOES_VALIDAS:
        if oracao_completa in code_content:
            return True
    return False

def imprimir_erro_sacerdos(message):
    """Função para padronizar a saída de erros críticos."""
    print(f"\nERRO DO SACERDOS: {message}")
    sys.exit(1)

def validar_tipo_pao(line):
    """
    Regra ULTRA-ESTRITA: PÃO só aceita VERDADEIRO. 
    Verifica a atribuição direta do literal FALSO e gera erro específico.
    """
    # Remove comentários inline e trailing ';' para análise estável
    sanitized = line.split('#', 1)[0].rstrip(';').strip()
    if re.search(r'=\s*(FALSO|False|falso)\b', sanitized, re.IGNORECASE):
        imprimir_erro_sacerdos("A oração é aceita perante a VERDADE.")
    pass

# --- 3. TRADUTOR PRINCIPAL ---

def translate_pater_noster_to_python(pater_noster_code):
    
    if not validar_obrigacoes_liturgicas(pater_noster_code):
        imprimir_erro_sacerdos("O usuário não rezou da maneira correta. Verifique as Orações Iniciatórias.")
        
    python_code = [
        "# -*- coding: utf-8 -*-",
        "# Script traduzido pelo Sacerdos v3.16 (Versão Estável Corrigida)",
        "import sys"
    ]
    indent_level = 0
    main_defined = False
    
    lines = pater_noster_code.split('\n')

    for line in lines:
        stripped_line = line.strip()
        stripped_line = stripped_line.replace('//', '#')
        stripped_line_no_semicolon = stripped_line.rstrip(';').rstrip('}') 

        
        is_closing_brace = stripped_line == "}" or stripped_line.endswith("};")
        
        current_indent = INDENT_CHAR * indent_level
        
        if not stripped_line or stripped_line.startswith("#") or stripped_line.startswith("OREMOS"):
            if is_closing_brace:
                indent_level = max(0, indent_level - 1)
            continue

        
        var_command_match = re.match(r'([a-zA-Z_]\w*)\s*;\s*([A-Z_]+)\s*;', stripped_line)
        if var_command_match:
            var_name = var_command_match.group(1)
            command = var_command_match.group(2)
            
            if command == "NAO_TEMEREI_O_MAL":
                python_code.append(f"{current_indent}{var_name} -= 1")
            elif command == "AUMENTAI_MINHA_FÉ":
                python_code.append(f"{current_indent}{var_name} += 1")
            continue

        
        if is_closing_brace:
            indent_level = max(0, indent_level - 1)
            continue

        # Linhas que começam com identificadores minúsculos são código normal (ex.: pontuacao += 1)
        if stripped_line and stripped_line[0].islower():
            if "=" in stripped_line or any(op in stripped_line for op in ['+', '-', '*', '/', '%']):
                validar_tipo_pao(stripped_line)
                python_code.append(f"{current_indent}{stripped_line_no_semicolon}")
            continue

        command_match = re.match(r'([A-Z_]+)', stripped_line, re.IGNORECASE)
        
        if not command_match:
            if "=" in stripped_line or any(op in stripped_line for op in ['+', '-', '*', '/', '%']):
                validar_tipo_pao(stripped_line) 
                python_code.append(f"{current_indent}{stripped_line_no_semicolon}")
            continue

        command = command_match.group(1).upper()
        
        rest_of_line_after_command = stripped_line_no_semicolon[len(command):].strip()
        
        # --- A. DEFINIÇÕES E FLUXO PRINCIPAL ---
        if command == "PAI_NOSSO":
            python_code.append("\n# Definição do bloco principal PAI_NOSSO")
            python_code.append("def main():")
            indent_level += 1
            main_defined = True
            
        elif command == "VOSSO_REINO":
            func_def = rest_of_line_after_command.split('{')[0].strip()
            python_code.append(f"\n{current_indent}def {func_def}:")
            indent_level += 1
            
        elif command == "VOSSA_VONTADE":
            return_value = re.sub(r'[\(\)\{\}]', '', rest_of_line_after_command).strip()
            python_code.append(f"{current_indent}return {return_value}")

        elif command == "AMÉM" or command == "AMEM":
            continue

        # --- B. FUNÇÕES DE MANIPULAÇÃO (I/O) ---
        elif command == "TRANSFORMAI_EM_VINHO":
            # BUG B16 CORREÇÃO: Extração robusta do conteúdo entre parênteses
            content_match = re.search(r'\((.*)\)', stripped_line_no_semicolon)
            content = content_match.group(1).strip() if content_match else ""

            match_format = re.search(r'(\".*?\")\s*(,.*|$)', content)
            
            if match_format:
                format_string = match_format.group(1).strip()
                args = match_format.group(2).strip().lstrip(',')
            else:
                format_string = content
                args = ""

            if args:
                args_clean = args.strip('(').strip(')')
                python_code.append(f'{current_indent}print({format_string} % ({args_clean}))')
            else:
                python_code.append(f'{current_indent}print({format_string})')
            
        elif command == "OUVI_A_VOZ":
            
            var_name = rest_of_line_after_command.strip('(').strip(')')
            prompt = f'"Insira o valor para {var_name}: "'
            python_code.append(f"{current_indent}{var_name} = int(input({prompt})) # Converte input para ÁGUA/Inteiro")

        elif command == "PERDOAI":
            var_name = rest_of_line_after_command.strip('(').strip(')')
            python_code.append(f"{current_indent}{var_name} = 0 # PERDOAI: Variável resetada para 0")

        elif command == "VENHA_ATÉ_NÓS" or command == "VENHA_A_NÓS":
            func_call = rest_of_line_after_command
            python_code.append(f"{current_indent}{func_call}")
            
        # --- C. VARIÁVEIS E TIPOS (BATISMO) ---
        elif command == "BATISMO":
            
            cleaned_line = rest_of_line_after_command
            
            if '=' not in cleaned_line:
                 
                 if 'PÃO' in stripped_line.upper():
                     cleaned_line += " = True # Inicialização padrão para escopo (VERDADEIRO)"
                 else:
                     cleaned_line += " = None # Inicialização padrão para outros tipos" 
            
            cleaned_line = cleaned_line.replace("VERDADEIRO", "True").replace("FALSO", "False")
            cleaned_line = re.sub(r'(ÁGUA|VINHO|PÃO)', '', cleaned_line).strip() 
            cleaned_line = re.sub(r'\bVENHA_A_(?:T[ÉE]_)?N[ÓO]S\s+', '', cleaned_line)
            
            validar_tipo_pao(cleaned_line)
            python_code.append(f"{current_indent}{cleaned_line}")
        
        # --- D. Comandos de Incremento/Decremento ---
        # (Tratados acima no bloco VAR; COMANDO;)
            
        # --- E. CONTROLE DE FLUXO (IF/ELSE/WHILE) ---
        elif command == "SE_FOR_VOSSA_VONTADE" or command == "SE_POR_VOSSA_VONTADE":
            
            condition_match = re.search(r'\((.*?)\)\s*\{', stripped_line)
            condition = condition_match.group(1).strip() if condition_match else rest_of_line_after_command.strip().rstrip('{').strip()
            
            python_code.append(f"{current_indent}if {condition}:")
            indent_level += 1
            
        elif command == "SE_NÃO_FOR_VOSSA_VONTADE" or command == "SE_NAO_FOR_VOSSA_VONTADE":
            
            condition_match = re.search(r'\((.*?)\)', rest_of_line_after_command)
            
            if condition_match:
                condition = condition_match.group(1).strip()
                python_code.append(f"{current_indent}elif {condition}:")
            else:
                python_code.append(f"{current_indent}else:")

            indent_level += 1 

        elif command == "ENQUANTO_EU_VIVERES_E_ATÉ_QUANDO_TU_QUISERES" or command == "ENQUANTO_EU_VIVERES_E_ATE_QUANDO_TU_QUISERES":
            
            condition_match = re.search(r'\((.*?)\)\s*\{', stripped_line)
            condition = condition_match.group(1).strip() if condition_match else rest_of_line_after_command.strip().rstrip('{').strip()
            
            python_code.append(f"{current_indent}while {condition}:")
            indent_level += 1
            
    
    if main_defined and indent_level == 1:
        python_code.append(f"{INDENT_CHAR}pass")
        indent_level -= 1

    # Função de confissão antes da execução do programa (Tiago 5:16)
    python_code.append("\n\ndef confessa_teus_pecados():")
    python_code.append(f"{INDENT_CHAR}print('Tiago 5:16 — Confessai, pois, os vossos pecados uns aos outros e orai uns pelos outros, para que sareis.')")
    python_code.append(f"{INDENT_CHAR}resposta = input('Tens pecados a confessar? (s/n): ').strip().lower()")
    python_code.append(f"{INDENT_CHAR}if resposta not in ('s', 'n'):")
    python_code.append(f"{INDENT_CHAR*2}print('Resposta inválida. Use s/n.')")
    python_code.append(f"{INDENT_CHAR*2}sys.exit(1)")
    python_code.append(f"{INDENT_CHAR}if resposta == 'n':")
    python_code.append(f"{INDENT_CHAR*2}print('Segue em paz e permanece em graça.')")
    python_code.append(f"{INDENT_CHAR*2}return")
    python_code.append(f"{INDENT_CHAR}quer = input('Desejas te confessar agora? (s/n): ').strip().lower()")
    python_code.append(f"{INDENT_CHAR}if quer == 's':")
    python_code.append(f"{INDENT_CHAR*2}input('Confessa teus pecados: ')  # conteúdo não é usado, ato simbólico")
    python_code.append(f"{INDENT_CHAR*2}print('Absolvido. Vai em paz e ora pelos irmãos.')")
    python_code.append(f"{INDENT_CHAR*2}return")
    python_code.append(f"{INDENT_CHAR}print('Execução interrompida: a confissão foi recusada. Que o Senhor te conduza ao arrependimento.')")
    python_code.append(f"{INDENT_CHAR}sys.exit(1)")

    # Adiciona o bloco de execução principal do Python
    python_code.append("\n\n# Bloco de execução principal do Python")
    python_code.append("if __name__ == '__main__':")
    python_code.append(f"{INDENT_CHAR}confessa_teus_pecados()")
    python_code.append(f"{INDENT_CHAR}main()")
    
    return "\n".join(python_code)


# --- 4. BLOCO DE EXECUÇÃO ---

if __name__ == "__main__":
    if len(sys.argv) != 2:
        imprimir_erro_sacerdos("Uso correto: python sacerdos_translator.py <arquivo_de_entrada.pn>")

    input_file_path = sys.argv[1]
    
    if not input_file_path.endswith(".pn"):
        imprimir_erro_sacerdos("O arquivo de entrada deve ter a extensão .pn (Pater Noster)")
        
    output_file_path = input_file_path.replace(".pn", ".py")

    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            pater_noster_code_content = f.read()
            
        translated_code = translate_pater_noster_to_python(pater_noster_code_content)
        
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(translated_code)
        
        print(f"Sucesso! Código Pater Noster '{input_file_path}' traduzido para o script Python '{output_file_path}'.")

    except FileNotFoundError:
        imprimir_erro_sacerdos(f"Arquivo '{input_file_path}' não encontrado.")