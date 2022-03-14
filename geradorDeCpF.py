
from PySimpleGUI import PySimpleGUI as sg
import random




    #sg.Popup('{}{}{}.{}{}{}.{}{}{}-{}{}'.format(check1, check2, check3, check4, check5, check6, check7, check8, check9, somaTotal, somaTotal2))


font = ("Arial Black", 25)
def janelaLogin():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuário',font=font),sg.Input(key='user',size=(15,1),font=font)],
        [sg.Text('Senha   ',font=font),sg.Input(key='passwd',size=(15,1),password_char='*',font=font)],
        [sg.Button('Login',font=font)]
    ]
    return sg.Window('Tela de Login',layout, finalize=True)
def janelaGerador():
    sg.theme('Reddit')
    layout = [
        [sg.Text('        Gerador de CPF',size=(45,1),font=font)],
        [sg.Image('imagem/receita.png',size=(450,300))],
        [sg.Button('Gerar',font=font),sg.Button('Voltar',font=font)],
    ]
    return sg.Window('by Victor', layout,size=(450,420), finalize=True)
janela1, janela2 = janelaLogin(), None
while True:
    window, eventos, valores = sg.read_all_windows()
    if window == janela1 and eventos == sg.WIN_CLOSED:
        break
    if window == janela2 and eventos == sg.WIN_CLOSED:
        break
    if window == janela1 and eventos == 'Login':
        if valores['user'] == 'admin' and valores['passwd'] == 'admin':
            try:
                janela1.hide()
                janela2 = janelaGerador()
            except:
                sg.Popup('Erro 404, tente novamente mais tarde.')
        else:
            sg.Popup('Error 404, tente novamente mais tarde')
    if window == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and eventos == 'Gerar':
        try:
            def _generatorMS_():
                check1 = random.randrange(10)
                check2 = random.randrange(10)
                check3 = random.randrange(10)
                check4 = random.randrange(10)
                check5 = random.randrange(10)
                check6 = random.randrange(10)
                check7 = random.randrange(10)
                check8 = random.randrange(10)
                check9 = random.randrange(10)
                
                array1 = check9 * 2
                array2 = check8 * 3
                array3 = check7 * 4
                array4 = check6 * 5
                array5 = check5 * 6
                array6 = check4 * 7
                array7 = check3 * 8
                array8 = check2 * 9
                array9 = check1 * 10

                somaTotal = array1 + array2 + array3 + array4 + array5 + array6 + array7 + array8 + array9
                def _init_(a, b):
                    return round(a % b)
                somaTotal = 11 - _init_(somaTotal, 11)
                if somaTotal >= 10:
                    somaTotal = 0
                
                a1 = somaTotal * 2
                a2 = check9 * 3
                a3 = check8 * 4
                a4 = check7 * 5
                a5 = check6 * 6 
                a6 = check5 * 7
                a7 = check4 * 8
                a8 = check3 * 9
                a9 = check2 * 10
                a10 = check1 * 11


                

                somaTotal2 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
                somaTotal2 = 11 - _init_(somaTotal2, 11)

                if somaTotal2 >= 10:
                    somaTotal2 = 0
                try:
                    while True:
                        calculaTotal = check1 + check2 + check3 + check4 + check5 + check6 + check7 + check8 + check9 + somaTotal + somaTotal2
                        if calculaTotal == 33 or 44 or 55 or 66:
                            sg.Popup("O CPF {}{}{}.{}{}{}.{}{}{}-{}{} foi gerado! Ele é válido!".format(check1, check2, check3, check4, check5, check6, check7, check8, check9, somaTotal, somaTotal2))
                            break
                        else:
                            calculaTotal = check1 + check2 + check3 + check4 + check5 + check6 + check7 + check8 + check9 + somaTotal + somaTotal2
                            if calculaTotal == 33 or 44 or 55 or 66:
                                sg.Popup('O CPF {}{}{}.{}{}{}.{}{}{}-{}{} foi gerado! Ele é válido!'.format(check1, check2, check3, check4, check5, check6, check7, check8, check9, somaTotal, somaTotal2))
                                break
                except:
                    sg.Popup('Erro 404, Tente novamente')
                
            _generatorMS_()
        except:
            sg.Popup('deu erro aqui brother')
