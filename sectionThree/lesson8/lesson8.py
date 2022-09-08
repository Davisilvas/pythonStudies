"""
Sistema de perguntas e respostas com python
"""
perguntas = {
    'p1': {
        'pergunta': 'Quanto é 2 + 2?',
        'resposta': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'respostaCerta': 'b',
    },
    'p2': {
        'pergunta': 'Quanto é 4 + 4?',
        'resposta': {
            'a': '8',
            'b': '10',
            'c': '9',
        },
        'respostaCerta': 'a',
    },
}

acertos = 0
for questionKey, questionValue in perguntas.items():
    print(f'{questionKey}: {questionValue["pergunta"]}')
    print('Escolha a resposta dentre as opções abaixo')

    for answerKey, answerValue in questionValue['resposta'].items():
        print(f'[{answerKey}]: {answerValue}')

    userAnswer = input('Informe sua resposta: ')
    if userAnswer == questionValue['respostaCerta']:
        print(f'Você acertou, a resposta é {questionValue["respostaCerta"]}')
        acertos += 1
    else:
        print('Você errou')
    print()

print(f'Você obteve {acertos} acertos')
