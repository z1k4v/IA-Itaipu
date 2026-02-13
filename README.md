# Passos iniciais em Programação e LLM

Novas habilidades serão testadas ao extremo

## Nomeclaturas e boas práticas

[Branches]
-Tipos

01. docs: apenas mudanças de documentação;
02. feat: uma nova funcionalidade;
03. fix: a correção de um bug;
04. perf: mudança de código focada em melhorar performance;
05. refactor: mudança de código que não adiciona uma funcionalidade e também não corrigi um bug;
06. style: mudanças no código que não afetam seu significado (espaço em branco, formatação, ponto e vírgula, etc);
07. test: adicionar ou corrigir testes.

-O que a branche faz

-Código de rastreio da tarefa em um organizador

*Exemplo: feat/CadastroVeiculos/PL123

[Commits]
-Estrutura:

<type>(<scope>): <subject> // <body> // <footer>

-Explicação

01. type ou categoria do commit: podem ser os mesmos utilizados para criar branches e que foram explicados acima;
02. scope: onde a alteração foi feita. Aqui, criamos nossos próprios scopes que, na maioria dos casos, refletem o nome de uma funcionalidade;
03. subject: um resumo do commit. Deve utilizar o imperativo, como: faz, adiciona, altera, muda e etc;
04. body: espaço utilizado para detalhar o que foi feito. É opcional;
05. footer: onde colocamos as PLs (códigos das tarefas) e também alguma breaking change.

- Regras Gerais

01. Evite linhas com mais de 100 caracteres;
02. Types aceitos: docs, feat, fix, perf, test, refactor e style;

## Passo a passo para utilizar corretamente o GitFlow

01. Criar branche nova no repositório remoto;
    - Criar a branch "develop" a partir da "main"
02. No VSCode habilitar ssh-agent com a chavede acesso utilizando o terminal
    - eval "$(ssh-agent -s)" // {inicia o ssh-agent, deve obter a resposta como: Agent pid xxxx}
    - ssh-add ~/.ssh/id_ed25519 // {adiciona a sua chave, após inserir chave deve responder com: Identity added}
    - ssh -T git@github.com // {Testa a conexão com o GitHub, deve obter a resposta como: Hi SEU_USUARIO! You've successfully authenticated...}
03. Verificar branches e adicionar a branche "develop";
    - git branch // {para verificar as branches}
    - git fetch // {traz as branches}
    - git checkout develop // {altera branch para "develop"}
    - git branch // {para verificar as branches}
04. Criar branch nova para trabalho;
    - git pull origin develop // {garantir que a "develop" local esteja atualizada como a "develop" da origem}
    - git checkout -b <nome padrão de branche> // {Criação de nova branch localmente}
05. Alterar o que for preciso;
06. Salvar novo arquivo;
07. Realizar git add das novas alterações;
    - Ir até source control
    - Stage Changes <+>
09. Realizar o git commit;
    - Nomear o commit de acordo com a padronização previamente definida
    - Selecionar commit
10. Realizar o Publish Branch;
11. No GitHub realizar Compare & pull request;
    - Alterar base para "develop"
    - Selecionar Create pull request
    - Selecionar Merge pull request
12. Deletar branch // {Pois já está mergeada na "develop"}
13. No VSCode deletar branch na local
    - git checkout develop // {Retorna para a branch "develop"}
    - git branch -D <Nome da branch a ser deletada>
14. Verificar branches
    - git branch // {para verificar branches}