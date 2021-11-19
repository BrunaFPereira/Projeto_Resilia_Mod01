

def esc_personagem(sel):
    if sel == 'j':
        fases(sel)
    elif sel == 'n':
        fases(sel)
    elif sel == 'r':
        fases(sel)
    else:
        print('Personagem indefinido')


def personagem():
    print('__' *20)
    print()
    print(' - Seleção de Personagens - ')
    print('[j] Jonathan')
    print('..Direto da área da saúde, Jonathan com o apoio da Resilia, está mais do que preparado para a migração de carreira..')
    print('[n] Nathaly')
    print('..Em meio a rotina pesada, Nathaly não desanimará com a rotina da Resilia..')
    print('[r] Raian')
    print('..Com uma bagagem de conhecimento e o suporte da Resilia, Raian está mais do que preparado para os proximos desafios..') 
    print()
    selecao = input('Digite a inicial desejada [j, n ou r]: ')
    esc_personagem(selecao)

def fases(selecao):
    if selecao == 'j':
        jonathan()
    elif selecao == 'n':
        nathaly()
    elif selecao == 'r':
        raian()
    else:
        print('Personagem Indefinido')


  
def jonathan():
    print()
    print()
    print('Fase 1 - Hábitos')
    print()
    print('Em suas aulas de Soft, Jonathan entendeu que o resultado não aparece da noite para o dia.')
    print('E que seus hábitos precisavam ser reorganizados. Qual das alternativas é a correta? ')
    print()
    print('[a] Com metas estabelecidas e respeitadas, as chances de ter um resultado positivo, são maiores.')
    print('[b] O imediatismo dos objetivos é a chave do sucesso.')
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'a':
        print('Resposta errada, tente outra vez')
        personagem()
    elif resposta == 'a':
        print('Mandou bem, bora para a proxima fase!')
    print()
    print()
    print('Fase 2 - Inovação')
    print()
    print('De frente com mais uma fase, dessa vez sobre Inovação.')
    print('Inovação não surge do nada, qual das caracteristicas podemos relacionar com inovação?')
    print()
    print('[a] Curiosidade.')
    print('[b] Perfeccionismo.')
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'a':
        print('Resposta errada, tente outra vez')
        personagem()  
    elif resposta == 'a':
        print('Última fase, vamos nessa! \o/')          
    print()
    print('Fase 3 - Empregabilidade')
    print()
    print('Em seus últimos módulos da Resilia, a empregabilidade é um dos principais fatores para seu objetivo.')
    print('Escolha os fatores que mais influenciam na empregabilidade:')
    print()
    print('[a] Situação financeira: não influecia na repercução no exercicio da sua função.')
    print('[b] Habilidade e vocação: O diploma é essencial, mas não é o bastante.')
    print()
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'b':
        print('Resposta errada, tente outra vez')
        personagem()  
    elif resposta == 'b':
        print('PARABÉNS! As chances de um emprego está logo aí! ;) ')
        print('Jonatham finalmente conseguiu o emprego dos seus sonhos!')
        print('__' *20)
        personagem()

def nathaly():
    print()
    print()
    print('Fase 1 - Gestão de tempo e Rotina')
    print()
    print('Muito trabalho, estudo e outras "correrias", que dificultam a trilha do conhecimento.')
    print('Quais ferramentas ajudariam Nathaly, no seu dia-a-dia?')
    print()
    print('[a] Todoist e Trello.')
    print('[b] Excel e Vs code.')
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'a':
        print('Resposta errada, tente outra vez')
        personagem()
    elif resposta == 'a':
        print('Mandou bem, bora para a proxima fase!')
    print()
    print()
    print('Fase 2 - Postura Profissional')
    print()
    print('Em sua jornada, Nathaly deparou-se com mais uma dificuldade.')
    print('Sabendo que postura profissional positiva é um diferencial, marque a opção que correta:')
    print()
    print('[a] Seja sincero fale mal ou fale bem, mas fale.')
    print('[b] Respeite a politica da empresa e leve seu trabalho a sério.')
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'b':
        print('Resposta errada, tente outra vez')
        personagem()  
    elif resposta == 'b':
        print('Aí sim, bora para a última fase! \o/')          
    print()
    print('Fase 3 - Vieses Cognitivos')
    print()
    print('Em seu último desafio, em meio as armadilhas, Bruna terá cuidado para não tomar decisões irracionais?!')
    print('Escolha a alternativa correta, dos principais vieses cognitivos são:')
    print()
    print('[a] Viés da "Maria vai com as outras, Viés da Confirmação e Viés de Positividade.')
    print('[b] Viés da decoragem, Viés da formação e Viés da pré escolha.')
    print()
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'a':
        print('Resposta errada, tente outra vez')
        personagem()  
    elif resposta == 'a':
        print('PARABÉNS! Você manja mesmo de Softskills! ')
        print('No meio de tanta correria, Nathaly finalmente conseguiu equilibrar mais sua rotina de sucesso!')
        print('__' *20)
        personagem()    

def raian():
    print()
    print()
    print('Fase 1 - Relacionamento Interpessoal')
    print()
    print('No decorrer das aulas, Raian pecebeu a importacia da Comunidade Resilia.')
    print('Qual a melhor alternativa para o progresso de Raian:')
    print()
    print('[a] A prática da escuta com feedbacks, sem a necessidde de sua atenção.')
    print('[b] Estabelecendo limites, é possivel ter seu espaço, manter o foco e produtividade.')
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'b':
        print('Resposta errada, tente outra vez')
        personagem()
    elif resposta == 'b':    
        print('Mandou bem, bora para a proxima fase!')
    print()
    print()
    print('Fase 2 - Visão de negocios')
    print()
    print('Na sua busca pelo conhecimento, Raian se deu conta que nem tudo é programar.')
    print('Mas com essa competencia, ele não estava familiarizado. Ajude Raian a deicidr qual a melhor opção:')
    print()
    print('[a] Foco no individual, terminar o prazo é o mais importante.')
    print('[b] Coleta de experiencias e informações referente ao tipo de negocio trabalhado.')
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'b':
        print('Resposta errada, tente outra vez')
        personagem()  
    elif resposta == 'b':
        print('Aí sim, bora para a última fase! \o/')          
    print()
    print('Fase 3 - Pensamento crítico')
    print()
    print('Para se ter conhecimento real, é essencial que você identifique e retome as informações que receber.')
    print('Raian continua tendo problemas com soft, assinale a opção correta sobre pensamento crítico:')
    print()
    print('[a] Analisam e compreendem padrões.')
    print('[b] Aceitam lógicas simples')
    print()
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'a':
        print('Resposta errada, tente outra vez')
        personagem()  
    elif resposta == 'a':
        print('PARABÉNS! Você manja mesmo de Softskills! ')
        print('Sua jornada foi dura mas com ajuda das facilitadoras, foi possivel realizar seus objetivos! ')
        print('__' *20)
        personagem()        

print('__' *20)
print('***** EM BUSCA DO PITÃO *****')
print('__' *20)
entrar = input(">>>>> Aperte Enter <<<<<")
personagem()


        
