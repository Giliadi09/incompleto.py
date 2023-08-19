nome = input('qual é o seu nome')
receita = int(input('{} vc tem uma receita (1 sim ) (2 nao )?'.format(nome)))
if receita == 1:
    esf = int(input('A sua receita possue grau esferico? 1-sim // 2-não'))
    if esf == 1:
        esfdir = float(input('qual é o seu grau esferico do olho direito?'))  # aqui inicia a parte esferica da receita
        esfesq = float(input('qual é o seu grau esferico do lado esquerdo'))

    cil = int(input('sua receita possue grau cilindico? 1-sim ---- 2--nao'))
    if cil == 1:
        cildir = float(input('qual é o seu grau cilindrico direito?'))  # aqui inicia a parte cilindrica da receita
        cilesq = float(input('qual é o seu grau cilindrico do lado esquerdo?'))

    add = int(input('sua receita possue adição? 1-- sim / 2-- não '))  # aqui inicia a parte de perto da receita
    if add == 1:
        pert = float(input('qual é o valor da sua adição ?'))
        print('voce ira usar uma lente multifocal')

    else:  # aqui o paciente não tem add na receita
        print('vc vai usar uma lente monofocal')
        print('1-- EURO PRO')
        print('2-- ESSILOR')
        print('3--HOYA')

        marca = int(input('SELECIONE A MARCA DE SUA PREFERENCIA? '))

        if marca == 1:
            if esfdir <= 4 and esfesq <= 4:
                print('Voce ira usar uma lente LP BLUE CUT 1.56')
            elif esfdir <= 7 and esfesq <= 7:
                print('vc ira usar uma lente blue cut 1.60')
            elif esfdir >= 8 or esfesq >= 8:
                print('vc precisa de uma lente surfaçada')
        elif marca == 2:
            if esfdir <= 4 and esfesq <= 4:
                print('VC IRA USAR UMA LENTE PRONTA ORMA BLUE UV ')
            elif esfdir <= 7 and esfesq <= 7:
                print('vc ira usar uma LENTE PRONTA AIR WEAR BLUE UV')
            elif esfdir >= 8 or esfesq >= 8:
                print('vc ira usa uma STYLIS 1.67 BLUE VC')
            elif esfdir >= 10 or esfesq >= 10:
                print('vc precisa de uma lente surfaçada')

        elif marca == 3:
            if esfdir <= 4 and esfesq <= 4:
                print('vc precisa de uma LENTE PRONTA HILUX VS PREMIUM 1.50')
            elif esfdir <= 7 and esfesq <= 7:
                print('VC PRECISA DE UMA LENTE PRONTA HILUX ULTRAX E THINHARD 1.59 OU 1.60')
            elif esfdir <= 8 or esfesq <= 8:
                print('VC PRECISA DE UMA LENTE SURFAÇADA ENROUTE VS 1.67')
            elif esfdir >8 or esfesq >8:
                print('vc precisa de uma lente surfaçada NULUX IDENTILY V+ 1.74')


# iniciando a parte de consulta-p´
else:
    consulta = int(input('vc quer marcar uma consulta 1-- sim 2--não?'))
    if consulta == 1:
        contato = type(
            input('Digite o seu numero de telefone que nossa equipe entrara em contato com vc agendando um horario.'))
        print('a equipe mercadão agrace o seu contato')

    else:
        print('A equipe mercadão agradece o seu contato')