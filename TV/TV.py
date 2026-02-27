from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
from rich.align import Align

console = Console()

c1 = '[on white]'
c2 = '[on cyan]'
vol_list = [f'{c1:<20}[/]', (f'{c2:<11}[/]{c1:<18}[/]'),
                (f'{c2:<13}[/]{c1:<16}[/]'), (f'{c2:<15}[/]{c1:<14}[/]'),
                (f'{c2:<17}[/]{c1:<12}[/]'), (f'{c2:<19}[/]{c1:<10}[/]')]

class Tv:
    """Para iniciar a classe escreva:
    X = Tv()
    A televisão precisa ser ligada antes que os comandos funcione, então antes de tudo
    passe o comando X.tvon()
    Os outros comandos estão bem claros.
    Caso queira desligar, pressione *
    Aproveite! :) """

    def __init__(self, status = False, channel = 1, vol = 1):
        self.channel = channel
        self.status = status
        self.vol = vol

    def tvon(self): #Função de ligar
        self.status = True
        return console.print(f'{'[bold red]Tv ligada com sucesso[/]':>46}')

    def tvoff(self): #Função de desligar
        self.status = False
        return print('Desligando Tv...')

    def volup(self): #Função de aumentar o volume
        if self.vol == 5:
            pass
        else:
            self.vol += 1

    def voldown(self): #Função de diminuir o volume
        if self.vol == 0:
            pass
        else:
            self.vol -= 1

    def channelup(self): #Função para passar o canal
        if self.channel == 3:
            print('Não há mais canais!')
        else:
            self.channel += 1

    def channeldown(self): #Função para voltar o canal
        if self.channel == 1:
            print('Não há mais canais!')
        else:
            self.channel -= 1

    def channelselect(self, numero_canal): #Função para pular para o canal especifico
        self.channel = numero_canal


    def comandos(self):
        comandosP = Panel(
            Align.center(
                f'{'Comandos'}',
                vertical='middle'
            ),
            width=46,
            border_style="bold red")

        canalP = Panel(
            Align.center(
                f'{'- Próximo\n- Anterior\n- (numero do canal)'}',
                vertical='middle'
            ),
            width=23,
            title='Canal',
            border_style="bold blue")

        volumeP = Panel(
            Align.center(
                f'{'- Aumentar \n- Diminuir\n'}',
                vertical='middle'
            ),
            width=23,
            title='Volume',
            border_style="bold yellow"
        )
        return console.print(comandosP, Columns([canalP, volumeP]))

    def comandoi(self):
        comando = input('Digite o comando(*):').strip().title()
        if comando == 'Aumentar':
            self.volup()
        elif comando == 'Diminuir':
            self.voldown()
        elif comando == 'Anterior':
            self.channeldown()
        elif comando in ['Próximo', 'Proximo']:
            self.channelup()
        elif comando in ['1', '2', '3']:
            self.channelselect(int(comando))
        elif comando == '*':
            self.tvoff()
        else: print('[red bold]Comando inválido, tente novamente![/]')

    def tvstatus(self): #Função apenas para mostrar o status da TV (Canal e Volume)
        global c1, c2
        if self.status == True:
            if self.channel == 1:
                console.print(Panel(
                    Align.center(
                        f'      Welcome to Television\n'
                        f'Select your Channel: [on white][1][/] [2] [3]\n'
                        f'      Volume {vol_list[self.vol]}\n '
                        f'  {'-  +':>14}',
                        vertical='middle'
                    ),
                    width=46,
                    title='[bold][TV Digital]')
                )

            if self.channel == 2:
                console.print(Panel(
                    Align.center(
                        f'      Welcome to Television\n'
                        f'Select your Channel: [1] [on white][2][/] [3]\n'
                        f'      Volume {self.vol}\n'
                        f'      {'-  +':>14}',
                        vertical='middle'
                    ),
                    width=46,
                    title='[bold][TV Digital]')
                )

            if self.channel == 3:
                console.print(Panel(
                    Align.center(
                        f'      Welcome to Television\n'
                        f'Select your Channel: [1] [2] [on white][3][/]\n'
                        f'      Volume {self.vol}\n '
                        f'      {'-  +':>14}',
                        vertical='middle'
                    ),
                    width=46,
                    title='[bold][TV Digital]')
                )
        self.comandos()
        self.comandoi()





