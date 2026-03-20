#%%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros_compostos calcula o retorno financeiro a partir de um aporte. Deve-se considerar um valor, a taxa de juros atual e um tempo (em anos) para a taxa de juros calculada.
    
    Aporte: Número inteiro, que represente o valor em R$.
    
    Taxa: Número float entre 0 e 1 que represente o valor taxa de juros.
    
    Anos: Número inteiro >= 1 que representa o tempo que o investimento terá liquidez."""
    return aporte * (1 + taxa) ** anos

#%%

juros_compostos(aporte=1000, taxa=0.13, anos=4)