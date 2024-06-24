# Demo Prefect

## Descrição

Prefect é uma biblioteca de orquestração de fluxo de trabalho que permite definir, agendar e monitorar fluxos de trabalho complexos, facilitando a automação de tarefas.
No exemplo desse repositório há duas chamadas para uma API coletando dados da mesma


## Instalação

Para executar este demo localmente é necessário que maquina em questao ja tenha o Python instalado e o Prefect, caso nao tenha sugiro seguir a [documentação oficial](https://docs.prefect.io/latest/tutorial/)

Com isso feito, siga os passos:`

1.  **Clone o repositório**
        
    `git clone https://github.com/sergjuni/prefect-demo.git` 
    
2.  **Acesse o diretório do projeto**
    
    `cd prefect-demo` 
    
3.  **Crie um ambiente virtual**
    
    Crie um ambiente virtual para instalar as dependências. Se estiver usando `venv`, por exemplo:
  
    ``python -m venv venv`` 
	   
	   Ative o ambiente virtual usando o comando:
	   
	   ``source venv/bin/activate``
     
    
4.  **Execução do Demo**
    
    Execute o demo com o seguinte comando:
        
    `python main.py` 
    
    Isso iniciará um fluxo de trabalho de exemplo usando Prefect.

	O Prefect estará rodando localmente na porta ```http://127.0.0.1:4200```

_________


# Demo Prefect

## Description

Prefect is a workflow orchestration library that allows you to define, schedule, and monitor complex workflows, facilitating task automation. In the example of this repository, there are two API calls collecting data from the same source.

## Installation

To run this demo locally, ensure that your machine already has Python installed along with Prefect. If not, it's recommended to follow the [official documentation](https://docs.prefect.io/latest/tutorial/).

Once done, follow these steps:

1.  **Clone the repository**
    
    `git clone https://github.com/sergjuni/prefect-demo.git` 
    
2.  **Navigate to the project directory**
    
    `cd prefect-demo` 
    
3.  **Create a virtual environment**
    
    Create a virtual environment to install the dependencies. If using `venv`, for example:
        
    `python -m venv venv` 
    
    Activate the virtual environment with:
    
    `source venv/bin/activate` 
    
4.  **Run the Demo**
    
    Execute the demo with the following command:
    
    `python main.py` 
    
    This will start an example workflow using Prefect.
    
    Prefect will run locally on port `http://127.0.0.1:4200`.
   
    
