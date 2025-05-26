# 🚀 Organizador de Tarefas - Rei do Pitaco 👑

![Preview](https://img.shields.io/badge/Status-Pronto%20para%20Uso-brightgreen)  
Um organizador de tarefas intuitivo com flashcards, recorrência inteligente e salvamento automático.

---

## 📥 Primeiros Passos

### **1. Baixar os Arquivos**
1. Acesse o repositório do projeto:  
   [github.com/seu-usuario/repo](https://github.com/Ih4go/organizador-de-tarefas)
2. Baixe os dois arquivos necessários:
   - `ToDoList.py` (arquivo principal do programa)
   - `tasks.json` (exemplo de tarefas para teste)

   **Como baixar:**  
   - Opção 1: Clique em "Code" > "Download ZIP" (extraia os arquivos após o download)
   - Opção 2: Baixe individualmente clicando com botão direito em cada arquivo > "Salvar link como..."

### **2. Preparar a Pasta**
- Crie uma nova pasta em seu computador
- Mova ambos arquivos (`ToDoList.py` e `tasks.json`) para esta pasta

---

## 🖥️ Instalação e Execução

### **Passo 1: Instalar Python**
- **Windows/Mac:**
  1. Baixe a versão 3.6+ em [python.org](https://www.python.org/downloads/)
  2. Durante a instalação, MARQUE A OPÇÃO **"Add Python to PATH"**

- **Linux:**
  ```bash
  sudo apt-get update && sudo apt-get install python3 python3-tk

### **Passo 2: Executar o programa**
- **Windows:**
  1. Navegue até a pasta no Explorador de Arquivos.
  2. Clique na barra de endereços, digite cmd e pressione Enter.
  3. Execute:
  ```cmd
  python ToDoList.py

- **Linux/Mac:**
  1. Abra o terminal.
  2. Navegue até a pasta:
  ```bash
  cd /caminho/da/pasta
  3. Execute:
  python3 ToDoList.py

---


## 🧩 Funcionalidades

O arquivo exemplo `tasks.json` inclui tarefas de demonstração já adicionadas por mim:

✅ Tarefa diária

📅 Tarefa semanal (Todas as segundas-feiras)

🗓️ Tarefa mensal (Dia 15 de todo mês)

- **Dicas Importantes:**
1. Mantenha sempre os dois arquivos na mesma pasta
2. Não altere/exclua o `tasks.json` - ele armazena suas tarefas


---


## ✅ APP em funcionamento

- A tela principal do App mostrará todas as atividades em seus 3 estágios: Tarefas a fazer, em andamento e concluídas.

![Captura de tela 2025-05-26 093905](https://github.com/user-attachments/assets/a3ac19cb-f7fa-4225-b6ee-d199c52e179b)

- A segunda tela gerada é quando o botão de "+ Nova tarefa" é clicado. 
Nesse momento o usuário deverá colocar os detalhes da tarefa como: Título, descrição, prazo ou recorrência se for uma rotina.

![Captura de tela 2025-05-26 093439](https://github.com/user-attachments/assets/03ff3eb1-a2cf-4480-92f1-6460b0df07fe)


---


## 🛠️ Detalhes construtivos

- A Stack escolhida foi o Python por eu já possuir familiaridade com ela, devido estudá-la todo dia.
  
- As tarefas do dia-a-dia estão em constantes mudanças. Por isso escolhi para o App o formato de Flashcards.
  Assim o usuário terá maior liberdade para reclassificar os status de cada tarefa, deixando tudo mais dinâmico.
  
- Para maior agilidade e entrega do projeto em tempo hábil, o App foi gerado com auxílio da IA DeepSeek .
Segue o prompt utilizado:

**1. Solicitação Inicial**
```Prompt:
Crie um app de organização pessoal em python com interface gráfica no estilo flashcards.
Deverá ter 3 colunas de status de atividades: Tarefas a fazer, tarefas em andamento e tarefas concluídas.
Cada flashcard inserido nessas colunas deverá conter um título, descrição e data de término.
Torne possível para o usuário criar atividades novas, mover atividades criadas entre as colunas e também deletá-las quando desejar.

```

**2. Correção de Erro**
```Prompt:
O aplicativo está falhando na hora de mover as tarefas entre as colunas. Corrija para mim. Segue a mensagem de erro: [Exception details...]

```

**3. Adicionando Memória ao App**
```Prompt:
Torne possível adicionar tarefas rotineiras e também que o programa salve as últimas tarefas adicionadas
e as exiba quando for executado novamente.

```
**4. Correção de KeyError**
```Prompt:
Não foi possível executar o último código devido ao seguinte erro: [Traceback com KeyError...]

```
**5. Modificação na Lógica de Recorrência**
```Prompt:
Faça as seguintes alterações: Se o flashcard possuir recorrência diária,
então o flashcard não deverá perguntar qual o prazo da tarefa.
Se a tarefa for semanal também não deverá perguntar o prazo,
apenas pedir para o usuário registrar o dia da semana em que a tarefa será executada.
Se a tarefa for mensal também não deverá perguntar o prazo,
apenas pedir para o usuário registrar o dia do mês em que a tarefa será executada.

```
**6. Personalização de Interface**
```Prompt:
Personalize a interface do programa adicionando um texto no cabeçalho da janela escrito "Rei do Pitaco"
e no rodapé escreva "by Ihago Albuquerque".

```
**7. Correção de AttributeError**
```Prompt:
Ao executar o último script obtive o seguinte erro: [Traceback com AttributeError...]
```


---


## 🤝 Considerações Finais
Deixar o README arrumadinho e bem explicado deu bastante trabalho porém, foi um ótimo aprendizado.


Percebi o quanto faz diferença um bom README na hora de expor meus projetos. Com certeza dedicarei um tempo maior nisso daqui pra frente.
Agradeço ao Rei do Pitaco pela oportunidade de enriquecer meu repositório.


**Atenciosamente, Ihago Albuquerque**
