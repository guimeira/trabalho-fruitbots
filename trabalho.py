from tkinter import *
from tkinter import ttk
from random import randint, randrange
import importlib
import traceback

#Armazena o estado atual de um robô.
class Robo:
    def __init__(self, tipo, linha, coluna, frutas):
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        self.frutas = frutas
        self.status = 'JOGANDO'

        #Carregar arquivo que controlará o robô:
        modulo = importlib.import_module(f'robo-{tipo}')
        self.jogada = modulo.jogar
        self.nome = modulo.nome
    
    #Realiza a jogada chamando a função importada do arquivo:
    def jogar(self, arena, frutas, robo, adversarios):
        return self.jogada(arena, frutas, robo, adversarios)

#Armazena o estado de uma fruta:
class Fruta:
    def __init__(self, tipo, linha, coluna):
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        self.capturada = False

#Representa uma posição na arena.
class ItemArena(ttk.Frame):
    def __init__(self, master, linha, coluna):
        super().__init__(master, style='Item.TFrame')
        self.lbl = ttk.Label(self, anchor="center")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.lbl.grid(column=0, row=0, padx=1, pady=1, sticky="nwes")
    
    def atualizar_imagem(self, imagem):
        self.lbl['image'] = imagem

#Representa a arena:
class Arena(ttk.Frame):
    def __init__(self, master, linhas, colunas, robos, frutas, imagens):
        super().__init__(master, style='Arena.TFrame')
        self.imagens = imagens
        self.robos = robos
        self.frutas = frutas
        self.linhas = linhas
        self.colunas = colunas
        self.frutas = frutas

        #Criar os widgets para cada posição:
        self.item_widgets = []
        for l in range(0, linhas):
            col_items = []
            self.rowconfigure(l, weight=1, minsize=70)
            for c in range(0, colunas):
                self.columnconfigure(c, weight=1, minsize=70)
                item = ItemArena(self, l, c)
                item.grid(row=l, column=c, sticky="nwes")
                col_items.append(item)
            self.item_widgets.append(col_items)
        
        self.atualizar_arena()
    
    #Atualiza os ícones em todas as posições da arena.
    def atualizar_arena(self):
        #Zerar todas as posições:
        for l in range(0, self.linhas):
            for c in range(0, self.colunas):
                self.item_widgets[l][c].atualizar_imagem('')
        
        #Exibir os robôs:
        for r in self.robos:
            if r.status == 'JOGANDO':
                self.item_widgets[r.linha][r.coluna].atualizar_imagem(self.imagens['ROBO'][r.tipo])
        
        #Exibir as frutas:
        for f in self.frutas:
            if not f.capturada:
                self.item_widgets[f.linha][f.coluna].atualizar_imagem(self.imagens['FRUTA'][f.tipo])

#Placar de um dos robôs.
class RoboPlacar(ttk.Frame):
    def __init__(self, master, robo, imagens):
        super().__init__(master)
        self.robo = robo
        self['borderwidth'] = 2
        self['relief'] = 'ridge'
        self['padding'] = (5,5)

        #Label que armazena o ícone do robô:
        self.icone = ttk.Label(self, anchor='center', image=imagens['ROBO'][robo.tipo])
        self.icone.grid(row=0, column=0, rowspan=3, sticky="nwes")

        #Label que armazena o nome do robô:
        self.nome = ttk.Label(self, text=robo.nome, style='PlacarNome.TLabel')
        self.nome.grid(row=0, column=1, columnspan=2*len(robo.frutas), sticky="ew")
        
        #Criar os labels para cada fruta:
        self.labels_frutas = []
        for tipo_fruta, quant in enumerate(robo.frutas):
            #Ícone da fruta:
            imagem = ttk.Label(self, image=imagens['FRUTA'][tipo_fruta])
            imagem.grid(row=1, column=2*tipo_fruta+1)

            #Quantidade da fruta:
            quant = ttk.Label(self, text=str(quant), style='PlacarNome.TLabel')
            quant.grid(row=1, column=2*tipo_fruta+2)
            self.labels_frutas.append(quant)
        
        #Label que armazena o status do robô:
        self.label_status = ttk.Label(self, text='Jogando', style='PlacarStatus.TLabel')
        self.label_status.grid(row=2, column=1, columnspan=2*len(robo.frutas), sticky="ew")
    
    #Atualiza este placar:
    def atualizar(self):
        #Atualizar frutas:
        for tipo, quant in enumerate(self.robo.frutas):
            self.labels_frutas[tipo]['text'] = str(quant)
        
        #Atualizar status:
        if self.robo.status == 'JOGANDO':
            self.label_status['text'] = 'Jogando'
        elif self.robo.status == 'EXCEÇÃO':
            self.label_status['text'] = 'Eliminado: lançou exceção'
        elif self.robo.status == 'JOGADA INVÁLIDA':
            self.label_status['text'] = 'Eliminado: retornou jogada inválida'
        elif self.robo.status == 'GANHOU':
            self.label_status['text'] = 'Ganhou! Parabéns!'
        elif self.robo.status == 'PERDEU':
            self.label_status['text'] = 'Perdeu! Que pena!'
        elif self.robo.status == 'EMPATOU':
            self.label_status['text'] = 'Empatou! Tente novamente!'

#Placar de todos os robôs:
class Placar(ttk.Frame):
    def __init__(self, master, robos, imagens):
        super().__init__(master)
        self.robos = robos
        self.placares = []

        #Alocar um placar para cada robô:
        for linha,r in enumerate(robos):
            placar = RoboPlacar(self, r, imagens)
            self.placares.append(placar)
            placar.grid(row=linha, column=0, sticky='nwes', padx=10, pady=10)
    
    #Atualiza todos os placares:
    def atualizar(self):
        for p in self.placares:
            p.atualizar()

#Controle central do jogo:
class Game(ttk.Frame):
    def __init__(self, master, num_robos=2, num_frutas=[5,3,1], tamanho_min=7, tamanho_max=10):
        super().__init__(master)

        #Carregar as imagens necessárias:
        self.imagens = {
            'VAZIO': None,
            'ROBO': [ PhotoImage(file=f'imagens/robo-{i}.png') for i in range(num_robos) ],
            'FRUTA': [ PhotoImage(file=f'imagens/fruta-{i}.png') for i in range(len(num_frutas)) ]
        }

        #Determinar, aleatoriamente, o tamanho da arena:
        self.linhas = randint(tamanho_min, tamanho_max)
        self.colunas = randint(tamanho_min, tamanho_max)
        self.celulas = self.linhas*self.colunas

        #Criar os robôs, cada um em uma posição aleatória:
        self.robos = []
        for r_num in range(num_robos):
            r_linha = randrange(self.linhas)
            r_coluna = randrange(self.colunas)

            #Vamos sortear novos números enquanto a posição sorteada estiver ocupada:
            while [r for r in self.robos if r.linha == r_linha and r.coluna == r_coluna]:
                r_linha = randrange(self.linhas)
                r_coluna = randrange(self.colunas)
            
            #Criar contador de frutas para o robô:
            r_frutas = [0.0 for _ in num_frutas]

            #Criar robô:
            self.robos.append(Robo(r_num, r_linha, r_coluna, r_frutas))
        
        #Criar as frutas, cada uma em uma posição aleatória:
        self.frutas = []
        for f_tipo, f_quant in enumerate(num_frutas):
            for f_num in range(f_quant):
                f_linha = randrange(self.linhas)
                f_coluna = randrange(self.colunas)

                #Sortear novamente caso a posição esteja ocupada por um robô ou outra fruta:
                while [r for r in self.robos if r.linha == f_linha and r.coluna == f_coluna] or [f for f in self.frutas if f.linha == f_linha and f.coluna == f_coluna]:
                    f_linha = randrange(self.linhas)
                    f_coluna = randrange(self.colunas)
                
                #Criar fruta:
                self.frutas.append(Fruta(f_tipo, f_linha, f_coluna))
        
        #Criar a arena:
        self.arena = Arena(self, self.linhas, self.colunas, self.robos, self.frutas, self.imagens)
        self.arena.grid(row=0, column=0, padx=10, pady=10, sticky="nwes")

        #Criar o placar:
        self.placar = Placar(self, self.robos, self.imagens)
        self.placar.grid(row=0, column=1, sticky="nwes")

        #Adicionar o jogo à janela:
        self.grid(row=0, column=0, sticky="nwes")

        #Iniciar o temporizador:
        self.after(2000, self.jogada)
    
    #Realiza uma jogada:
    def jogada(self):
        #Cada robô fará sua jogada:
        for robo in self.robos:
            #Alocar os objetos que serão passados para o robô:
            j_arena = { 'linhas': self.linhas, 'colunas': self.colunas }
            j_frutas = [ {'tipo': f.tipo, 'linha': f.linha, 'coluna': f.coluna} for f in self.frutas if not f.capturada ]
            j_robo = { 'linha': robo.linha, 'coluna': robo.coluna, 'frutas': robo.frutas.copy() }
            j_adversarios = [ { 'linha': r.linha, 'coluna': r.coluna, 'frutas': r.frutas.copy() } for r in self.robos if r != robo and r.status == 'JOGANDO' ]
            
            try:
                #Realiza a jogada do robô:
                jog = robo.jogar(j_arena, j_frutas, j_robo, j_adversarios)

                #Alterar posição do robô se for possível:
                if jog == 'CIMA':
                    if robo.linha > 0:
                        robo.linha -= 1
                elif jog == 'BAIXO':
                    if robo.linha < self.linhas-1:
                        robo.linha += 1
                elif jog == 'DIREITA':
                    if robo.coluna < self.colunas-1:
                        robo.coluna += 1
                elif jog == 'ESQUERDA':
                    if robo.coluna > 0:
                        robo.coluna -= 1
                else:
                    robo.status = 'JOGADA INVÁLIDA'
            except Exception as e:
                #Robô lançou uma exceção:
                traceback.print_exc()
                robo.status = 'EXCEÇÃO'
        
        #Atualizar as frutas:
        for fruta in self.frutas:
            #Todos os robôs que capturaram esta fruta:
            robos_cap = [r for r in self.robos if r.linha == fruta.linha and r.coluna == fruta.coluna and not fruta.capturada]

            #Distribuir os pontos igualmente para cada um:
            for r_cap in robos_cap:
                r_cap.frutas[fruta.tipo] += 1/len(robos_cap)
            
            if robos_cap:
                fruta.capturada = True
        
        #Robôs que estão competindo (não lançaram exceção):
        robos_competindo = [r for r in self.robos if r.status == 'JOGANDO']

        #Frutas que ainda não foram capturadas:
        frutas_nao_cap = [f for f in self.frutas if not f.capturada]

        #O jogo termina se todos os robôs pararem ou se acabarem as frutas:
        terminou = len(robos_competindo) <= 1 or len(frutas_nao_cap) == 0
        
        if not terminou:
            #Se não terminou, realiza a próxima jogada daqui 1 segundo:
            self.after(1000, self.jogada)
        else:
            #Calcular a pontuação de cada robô:
            pontuacoes = []

            for robo in self.robos:
                pontuacao = 0
                for tipo, quant in enumerate(robo.frutas):
                    #Robôs que capturaram mais frutas deste tipo:
                    robos_melhores = [r for r in self.robos if r != robo and r.frutas[tipo] >= quant and r.status == 'JOGANDO' ]

                    #Se ninguém foi melhor, este robô recebe um ponto:
                    if not robos_melhores:
                        pontuacao += 1
                
                #Adicionar a pontuação deste robô na lista:
                pontuacoes.append(pontuacao)
            
            #Obter maior pontuação:
            melhor = max(pontuacoes)

            #Verificar se um ou mais robôs obtiveram a maior pontuação:
            melhores = [p for p in pontuacoes if p == melhor]

            #Se mais de um obteve a maior pontuação, é um empate:
            tipo_vitoria = 'GANHOU' if len(melhores) == 1 else 'EMPATOU'

            #Atualizar o status de cada robô:
            for tipo, robo in enumerate(self.robos):
                if robo.status != 'JOGANDO':
                    continue

                if pontuacoes[tipo] == melhor:
                    robo.status = tipo_vitoria
                else:
                    robo.status = 'PERDEU'
        
        #Atualizar interface gráfica:
        self.arena.atualizar_arena()
        self.placar.atualizar()

#Criar e configurar janela:
root = Tk()
root.title('Batalha de Robôs')
root.resizable(False, False)

#Configurar estilos:
s = ttk.Style()
s.configure('Arena.TFrame', background='red')
s.configure('Item.TFrame', background='blue')
s.configure('PlacarNome.TLabel', font=('TkTextFont', 20, 'bold'))
s.configure('PlacarStatus.TLabel', font=('TkTextFont', 16))

#Criar jogo:
arena = Game(root)

#Iniciar loop principal:
root.mainloop()
