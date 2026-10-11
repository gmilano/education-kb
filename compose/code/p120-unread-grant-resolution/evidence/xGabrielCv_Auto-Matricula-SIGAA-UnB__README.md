# 🤖 SIGAA Sniper — Auto-Matrícula SIGAA (UnB)

<p align="center">

**Automação, monitoramento e gerenciamento de matrícula no SIGAA da UnB**

Interface Web • Interface gráfica • Terminal • Dashboard • Monitoramento • Notificações • DRY RUN • Diagnóstico

<br>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge\&logo=windows\&logoColor=white)](#-requisitos)
[![Web](https://img.shields.io/badge/Interface%20Web-recomendada-1D4ED8?style=for-the-badge)](#-interface-web)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-FFCA28?style=for-the-badge)](#-três-modos-de-uso)
[![Tests](https://img.shields.io/badge/Tests-260%20passing-2EA44F?style=for-the-badge)](#-testes)
[![License](https://img.shields.io/badge/License-Open%20Source-blue?style=for-the-badge)](#-licença)

</p>

> [!WARNING]
>
> ## ⚠️ Aviso importante — leia antes de utilizar
>
> Este projeto é uma **prova de conceito (PoC) e ferramenta educacional**, desenvolvida para estudo de engenharia de software, automação e integração com aplicações web.
>
> O projeto **não possui vínculo, afiliação, autorização ou endosso da Universidade de Brasília (UnB), do STI ou do SIGAA**.
>
> O uso de automação para acessar sistemas autenticados ou realizar operações acadêmicas pode estar sujeito aos Termos de Uso do SIGAA, às políticas institucionais de segurança e às normas acadêmicas da universidade.
>
> O usuário é **integralmente responsável** por todas as consequências decorrentes da utilização do software, incluindo eventuais bloqueios de conta, falhas de autenticação, solicitações de matrícula inválidas, perda de vagas, interrupções de serviço ou consequências administrativas e acadêmicas.
>
> O uso deve ser **ético e responsável**. Requisições excessivas, concorrência inadequada ou utilização abusiva podem sobrecarregar a infraestrutura do SIGAA e prejudicar outros estudantes.
>
> **Nunca utilize o software para tentar contornar filas, regras, mecanismos de segurança ou limitações impostas pelo sistema.**
>
> Para quem deseja apenas acompanhar a disponibilidade de vagas, o projeto possui um **modo de somente monitoramento**, destinado a separar essa finalidade da execução de matrícula.

---

## 📌 Sobre o projeto

O **SIGAA Sniper** acompanha as turmas que você escolher no SIGAA da UnB e avisa quando surge uma vaga — ou, se você quiser, tenta a matrícula sozinho. Tudo roda **no seu computador**: suas credenciais não vão para nenhum servidor além do próprio SIGAA.

* 🌐 Interface Web local (modo recomendado), 🖥️ interface gráfica e 💻 terminal;
* 🧭 configuração inicial guiada, passo a passo;
* 📊 dashboard ao vivo e 🗂️ histórico das execuções;
* 👀 somente monitoramento, 🧪 DRY RUN (teste sem matricular) e 📝 matrícula automática;
* 🔔 avisos por Telegram, ntfy, alarme sonoro, Windows, Webhook e e-mail;
* 🩺 diagnóstico e 📋 central de logs, com dados pessoais sempre mascarados.

---

# 🚀 Uso rápido

```text
1. Baixe o SIGAA-Sniper.zip
2. Extraia numa pasta
3. Dê duplo clique em SIGAA-Sniper.exe
4. Aceite o aviso legal e escolha [0] 🌐 Interface Web
5. Siga a configuração inicial — ela explica cada passo
```

Não é preciso instalar Python nem nenhum outro programa: tudo está dentro do `.exe`.

> [!TIP]
> O programa começa em **somente monitoramento**, com o **DRY RUN** ligado. Quando passar para a matrícula, teste primeiro com o DRY RUN: ele faz todo o caminho, mas **não confirma** a matrícula — assim você vê se as disciplinas e o login estão certos sem risco.

---

# 🧭 Três modos de uso

Ao abrir o programa, o aviso legal aparece e, depois de aceito, o menu:

```text
[0] 🌐 Interface Web  ★ RECOMENDADO — abre no navegador
[1] Interface gráfica
[2] Matrícula automática
[3] Somente monitoramento
[4] Configurações
[5] Diagnóstico
[6] Sair
```

| Modo | Como abrir | Para quem |
| --- | --- | --- |
| 🌐 **Interface Web — recomendado** | opção `[0]` | Uso do dia a dia: visual moderno, dashboard ao vivo, tudo num lugar só |
| 🖥️ **Interface gráfica** | opção `[1]` | Quem prefere uma janela tradicional do Windows |
| ⌨️ **Terminal** | opções `[2]` a `[5]` | Uso só com teclado |

Os três modos usam **as mesmas regras**: as mesmas validações, as mesmas configurações salvas e o mesmo motor. O que você configura em um vale nos outros.

---

# 🧩 Configuração inicial guiada

Na primeira vez, um assistente leva você por cada etapa — e **só avança quando a etapa está correta**:

1. **Credenciais** — matrícula, senha, CPF e data de nascimento;
2. **Disciplinas** — código, turma e departamento, com grupo e prioridade opcionais;
3. **Execução** — somente monitoramento, DRY RUN ou matrícula real, e o ritmo das buscas;
4. **Notificações** — como você quer ser avisado;
5. **Painéis** — se o dashboard abre ao iniciar e se a última execução deve ser carregada;
6. **Revisão** — tudo o que foi escolhido, antes de salvar.

Você pode **voltar** a qualquer etapa, **cancelar** ou escolher **“Configurar depois”**. O assistente não reaparece depois de concluído, mas pode ser aberto de novo em **Config. Avançadas → 🧭 Refazer a configuração inicial**.

### CPF e data de nascimento

* **CPF**: pode digitar com ou sem pontos (`123.456.789-09` ou `12345678909`). O programa confere a quantidade de dígitos e os dígitos verificadores, e diz exatamente o que está errado.
* **Nascimento**: sempre no formato **DD/MM/AAAA** (ex.: `01/02/2003`). Datas impossíveis (31/02, mês 13, datas no futuro) são recusadas **antes** do login — um dado errado faria o SIGAA recusar cada confirmação.

### Departamentos

Digite o **código** do departamento se já souber, ou clique em **📋 Ver departamentos** para ver a lista completa, pesquisar pelo nome e escolher. A lista só abre quando você pede. No terminal, digite **L** para ver a lista.

### Grupos e prioridade

* **Grupo de alternativas**: turmas no mesmo grupo são “uma ou outra”. Quando uma delas é garantida, as outras saem da busca. Ex.: coloque as turmas 01 e 02 de Cálculo 1 no grupo `calculo`.
* **Prioridade**: **alta** é consultada primeiro em cada rodada; **baixa**, só a cada três rodadas (sobra ritmo para as outras e alivia o SIGAA).

O botão **?** (ou `?` no terminal) ao lado de cada campo explica com exemplos.

---

# ✨ Principais funcionalidades

### 📊 Dashboard

* estado de cada disciplina (buscando, sem vagas, vaga vista, tentando, matriculada…);
* saúde da conexão, com a causa provável e o que fazer;
* gráficos de tempo de resposta, buscas por segundo e vagas ao longo do tempo;
* linha do tempo da execução e cada tentativa de matrícula, passo a passo;
* resumo ao fim de cada execução.

**Parado é parado.** Quando nenhuma execução está em andamento, o dashboard mostra **“⚪ Nenhuma execução em andamento”** e nada nele muda sozinho: nenhum tempo corre, nenhum alerta aparece.

**Última execução.** Por padrão, o programa abre com o dashboard e os logs **limpos** (o histórico continua guardado na tela Histórico). Se preferir ver os dados da última execução ao abrir, ligue **“Carregar dados da última execução ao abrir”** em **Config. Avançadas**. Esses dados aparecem marcados como **“📂 Última execução (recuperada)”** e nunca parecem uma execução ativa.

### 🗂️ Histórico

Cada execução fica gravada no seu computador (sem credenciais): vagas vistas por dia, **em que horários as vagas costumam abrir**, comparação entre duas execuções, relatório imprimível e exportação CSV/JSON. Se o arquivo do histórico for danificado, o programa o separa (`historico.db.corrompido-…`) e começa um novo, sem travar.

### ⏯️ Controle da execução

* **pausar e retomar** sem perder a sessão;
* **término automático** numa data e hora e **janela diária** (horários e dias em que o programa roda);
* **verificação prévia** do login e das disciplinas antes de começar;
* disciplinas alteradas durante a execução valem na hora;
* **perfis de carga** (Leve, Moderado, Intenso) com a carga estimada no SIGAA, e pausa automática se o SIGAA ficar instável.

### 👀 Somente monitoramento

Acompanha a disponibilidade de vagas **sem executar a matrícula**. Se o seu objetivo é só ser avisado, prefira sempre este modo.

### 🧪 DRY RUN

Executa o fluxo de teste **sem a etapa final de confirmação**. Tem uma segunda proteção independente, para que uma configuração errada não transforme um teste numa operação real. A Interface Web ainda pede uma confirmação extra antes de iniciar uma matrícula real.

### 🔔 Notificações

Telegram, ntfy, alarme sonoro, notificação do Windows, **Webhook** e **e-mail**. Webhook e e-mail têm um botão **“Como configurar?”**, e há um botão para **testar** o envio.

* **Webhook** (Discord, Slack ou JSON): cole a URL gerada pelo serviço. Ela precisa começar com `https://`.
* **E-mail**: servidor SMTP, porta, segurança (TLS/SSL), usuário, senha, remetente (opcional) e destinatário. No Gmail e no Outlook, use uma **senha de app**, não a senha da conta.

A configuração só é salva depois de conferida. Tokens, URLs de webhook e senhas ficam só na memória — ou, se você marcar para salvar, cifrados com a proteção de dados do Windows. **Nunca** aparecem em logs, no dashboard, em relatórios ou no pacote de suporte.

### 📋 Logs e 🩺 Diagnóstico

* logs com filtros, pesquisa e tradução das mensagens técnicas para linguagem simples;
* diagnóstico em camadas (dependências, configuração, pastas, conexão com o SIGAA);
* **assistente de solução de problemas**: escolha o sintoma e veja a causa provável e o que fazer;
* **pacote de suporte** (.zip) pronto para pedir ajuda — sem senha, CPF, nascimento ou tokens.

### ⚙️ Configuração

Perfis prontos (nunca ligam a matrícula real), **desfazer alterações**, importar/exportar, lista de departamentos atualizada, **modo demonstração** com um SIGAA simulado para aprender sem conta, tema escuro e tamanho do texto.

### 🧰 Recursos experimentais

Ficam numa área **Experimental** separada (sincronização de relógio por NTP, entre outros), para não afetar a execução normal. Podem exigir dependências extras.

---

# 🌐 Interface Web

**Como iniciar:** abra o programa, aceite o aviso legal e escolha **`[0]`**. O navegador abre sozinho, numa janela própria.

Se não abrir, o terminal mostra o link completo:

```text
  http://127.0.0.1:8765/?chave=Abc123...
```

Copie o link **inteiro** (com `?chave=`). Para encerrar, use o botão **⏻ Encerrar** na página ou **ENTER** no terminal — as credenciais são apagadas da memória. A janela do terminal precisa continuar aberta enquanto você usa a Web.

* **Funciona só no seu computador**: escuta apenas em `127.0.0.1` e não carrega nada da internet.
* **Porta**: 8765 por padrão; se estiver ocupada, o programa usa outra e avisa. Dá para mudar em **Config. Avançadas → 🌐 Interface Web**.
* **Atalhos**: `Ctrl + K` abre a paleta de ações e `?` mostra todos os atalhos.
* **Segurança**: chave de acesso nova a cada execução, bloqueio de chamadas vindas de outros sites, e a senha nunca é enviada de volta à página.

---

# 🔐 Segurança e privacidade

* 🔒 credenciais ficam **só na memória**, a menos que você escolha salvá-las (cifradas pelo Windows);
* 🧹 logs, diagnósticos e pacote de suporte passam por mascaramento de dados pessoais;
* 🚫 importações que tragam credenciais escondidas são recusadas;
* 📦 a distribuição é verificada antes de ser publicada, sem dados pessoais nem arquivos de uso local.

Detalhes em [`docs/SEGURANCA.md`](docs/SEGURANCA.md).

> [!IMPORTANT]
> Nunca publique senhas, CPF, tokens, cookies ou dados acadêmicos — nem em issues.

---

# ⚖️ Aviso legal

O aviso legal aparece **em toda inicialização**, em qualquer um dos três modos, e exige as **5 confirmações** antes de continuar. Na Interface Web, nenhuma função responde antes do aceite. O aviso trata de: finalidade educacional, ausência de vínculo com a UnB, Termos de Uso, responsabilidade do usuário, uso ético e a opção de menor risco (somente monitoramento).

---

# 🖥️ Executando num Windows novo

**Onde colocar:** extraia o ZIP em qualquer pasta (Área de Trabalho, Documentos, pendrive…). O programa cria `config/`, `data/` e `logs/` ao lado do `.exe`. Ao mudar de pasta, leve **a pasta inteira**, não só o `.exe`.

**Administrador?** Não precisa. Use o duplo clique normal.

**Avisos do Windows (esperados):**

* **“O Windows protegeu o computador” (SmartScreen)** — aparece com qualquer `.exe` novo sem assinatura paga. Clique em **Mais informações → Executar assim mesmo**, só se o arquivo veio do repositório oficial.
* **Firewall** — o programa precisa de internet para falar com o SIGAA. Permita em **Redes privadas**.

**Como saber se está funcionando:** a opção `[5] Diagnóstico` confere dependências, configuração, pastas e conexão.

### Problemas comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| O Windows Defender apagou o `.exe` | Falso positivo (comum em executáveis PyInstaller sem assinatura paga) | Veja a seção seguinte |
| A janela abre e fecha na hora | Um erro antes do menu | Abra um terminal na pasta e rode `SIGAA-Sniper.exe` para ver a mensagem |
| “Não é possível acessar o SIGAA” | Sem internet, ou o SIGAA está fora do ar | Confira a conexão e tente mais tarde |
| Emojis aparecem como `?` no terminal | Terminal com página de código antiga | Inofensivo |
| A Web pede “Link de acesso necessário” | Endereço aberto sem a chave | Copie o link completo do terminal, com `?chave=` |
| “Interface Web encerrada” | O terminal foi fechado ou recebeu ENTER | Abra o programa de novo e escolha `[0]` |
| As disciplinas “sumiram” | A pasta foi movida sem `config/` e `data/` | Copie a pasta inteira |

> [!NOTE]
> O executável é para **Windows 64-bit**. Em outros sistemas, use o código-fonte com Python.

---

## 🛡️ O Windows Defender apontou o executável como ameaça (falso positivo)

Para funcionar sem Python instalado, o `.exe` empacota o Python e as bibliotecas num único arquivo e os extrai numa pasta temporária a cada execução. Alguns programas maliciosos fazem o mesmo, então o antivírus pode confundir os dois — ainda mais com um arquivo novo e **sem assinatura digital paga**. O projeto **não usa ofuscação, compactação UPX nem nenhuma técnica de evasão**.

**O que fazer:**

1. **Confira a origem**: só continue se o arquivo veio do repositório oficial no GitHub.
2. **Confira a impressão digital**: o ZIP traz `SHA256SUMS.txt`; compare com `certutil -hashfile SIGAA-Sniper.exe SHA256` (a tela **Sobre** também mostra). Para garantia total, gere o `.exe` você mesmo com `tools/build_exe.bat`.
3. **Se confiar no arquivo, crie uma exclusão só para a pasta do programa**: `Segurança do Windows → Proteção contra vírus e ameaças → Gerenciar configurações → Exclusões → Adicionar uma exclusão → Pasta`. **Nunca** exclua pastas amplas (como `C:\` ou Downloads inteira) e nunca desative o Defender.
4. **Se o arquivo já foi removido**, restaure-o em `Histórico de proteção → Ações → Restaurar`.

Para remover a exclusão depois, volte à lista de `Exclusões` e clique em `Remover`. Você também pode reportar o falso positivo à Microsoft em **https://www.microsoft.com/pt-br/wdsi/filesubmission** — isso ajuda outras pessoas.

---

# 💻 Requisitos

**Executável:** Windows 64-bit. Nada mais precisa ser instalado.

**Código-fonte:** Python **3.9 ou superior** e as dependências de `requirements.txt`:

```bash
pip install -r requirements.txt
python main.py
```

Ou simplesmente `run.bat`, que confere o ambiente e instala as dependências quando possível. A interface gráfica usa o Tkinter, que já vem com o Python no Windows.

---

# 🧪 Testes

```bash
pip install -r requirements-dev.txt
python -m pytest
```

A suíte principal tem **250 testes**, e há mais **10 testes no navegador real** (`tests/test_web_e2e.py`, que exigem `playwright`) — todos aprovados. Os testes usam um **SIGAA simulado**, sem rede e sem credenciais reais. Os testes de longa duração ficam fora da suíte padrão (`SIGAA_SNIPER_LONGO=<minutos>` e `SIGAA_SNIPER_LONGO_PARADO=<minutos>`).

> [!CAUTION]
> Os testes automatizados **não substituem uma operação real no SIGAA**: login e matrícula com uma conta real e o uso numa janela real de matrícula não fazem parte deles.

---

# 📚 Documentação

| Documento | Conteúdo |
| --- | --- |
| [`docs/GUIA_DE_USO.md`](docs/GUIA_DE_USO.md) | Guia completo de uso |
| [`docs/SEGURANCA.md`](docs/SEGURANCA.md) | Credenciais, dados guardados e segurança da Interface Web |

Os dois também aparecem na tela **Ajuda** do programa.

---

# 🐛 Problemas, sugestões e contribuições

Sugestões, correções e relatos de problemas são bem-vindos no repositório oficial:

**[GitHub — Auto-Matrícula SIGAA UnB](https://github.com/xGabrielCv/Auto-Matricula-SIGAA-UnB)**

Ao relatar um problema, inclua a versão, o modo usado (Web, GUI ou terminal), a mensagem de erro e os passos para reproduzir. Se puder, anexe o **pacote de suporte** (tela Diagnóstico), que já sai sem dados pessoais.

> [!WARNING]
> Nunca envie senhas, CPF, tokens, cookies ou outros dados pessoais numa issue.

---

# 📜 Licença

Consulte o arquivo de licença distribuído com o projeto. Este software é disponibilizado para fins educacionais e de estudo. O uso continua sujeito às regras, termos e políticas dos sistemas acessados.

---

<p align="center">

**SIGAA Sniper 🤖**

*Automação com responsabilidade.*

</p>
