
# deprecado: numpy.float foi removido no NumPy 1.20
import numpy as np
x = np.float(3.14)  


# deprecado: DataFrame.append() foi deprecado no pandas 1.4.0
import pandas as pd

def example_deprecated_append():
    """Exemplo de uso deprecado do append."""
    df1 = pd.DataFrame({'A': [1, 2]})
    df2 = pd.DataFrame({'A': [3, 4]})
    
    # deprecado
    result = df1.append(df2) 
    
    # correto
    # result = pd.concat([df1, df2], ignore_index=True)
    return result

# deprecado: sklearn.cross_validation foi movido
from sklearn.cross_validation import train_test_split  # Descomente para testar

# correto
# from sklearn.model_selection import train_test_split

print("Este arquivo está usando código atualizado (não deprecado)")
