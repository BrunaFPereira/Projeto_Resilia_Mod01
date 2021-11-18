


print('__' *20)
print('***** EM BUSCA DO PITÃO *****')
print('__' *20)
entrar = input(">>>>> Aperte Enter <<<<<")

def personagem():
    print('__' *20)
    print()
    print(' - Seleção de Personagens - ')
    print('[b] Bruna')
    print('.. Passou por vários desafios na vida e junto com a Resilia, passsará por mais desafios ainda..')
    print('[j] Jonathan')
    print('..Direto da área da saúde, Jonathan com o apoio da Resilia, está mais do que preparado para a migração de carreira..')
    print('[n] Nathaly')
    print('..Em meio a rotina pesada, Nathaly não desanimará com a rotina da Resilia..')
    print('[r] Raian')
    print('..Com uma bagagem de conhecimento e o suporte da Resilia, Raian está mais do que preparado para os proximos desafios..') 
    print()
    selecao = input('Digite a inicial desejada [b, j, n ou r]: ')
    return selecao

def fases(selecao):
    if selecao == 'b':
        bruna()
    elif selecao == 'j':
        jonathan()
    elif selecao == 'n':
        nathaly()
    elif selecao == 'r':
        raian()
    else:
        print('Personagem Indefinido')

def bruna():
    print()
    print()
    print('Fase 1 - Mindset de Crescimento')
    print()
    print('Apesar de determinada, ela tinha problemas com foco e procrastinação.')
    print('Com a Resilia aprendeu que com mudanças de hábitos, é possivel evoluir. Ajude a Bruna na escolha:')
    print()
    print('[a] Trasforme as oportunidades em  dificuldades.')
    print('[b] Fortaleça seus pontos fortes através do autoconhecimento.')
    print()
    resposta = input('Digite uma das opções [a ou b]: ')
    if resposta != 'b':
        print('Resposta errada, tente outra vez')
        personagem()
    elif resposta == 'b':
        print('Mandou bem, bora para a proxima fase!')
    print()
    print()
    print('Fase 2 - Postura Profissional')
    print()
    print('Em sua jornada, Bruna deparou-se com mais uma dificuldade.')
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
        print('__' *20)

  
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
    if resposta == 'a':
        print('Mandou bem, bora para a proxima fase!')
        return resposta
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
        return selecaoPersonagem  
    elif resposta == 'b':
        print('PARABÉNS! As chances de um emprego está logo aí! ;) ')
        print('__' *20)

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
    if resposta == 'a':
        print('Mandou bem, bora para a proxima fase!')
        return resposta

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
    if resposta == 'b':
        print('Mandou bem, bora para a proxima fase!')
        return resposta


while True:
    selecaoPersonagem = personagem()
    if selecaoPersonagem == 'b':
        fases(selecaoPersonagem)
        break
    elif selecaoPersonagem == 'j':
        fases(selecaoPersonagem)
        break
    elif selecaoPersonagem == 'n':
        fases(selecaoPersonagem)
        break
    elif selecaoPersonagem == 'r':
        fases(selecaoPersonagem)
        break
    else:
        print('Personagem indefinido')
        