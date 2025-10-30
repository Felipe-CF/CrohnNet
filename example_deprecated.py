"""
Arquivo de exemplo com código deprecado para testar o verificador.
ESTE ARQUIVO DEVE SER CORRIGIDO ANTES DO MERGE!
"""

# ❌ DEPRECADO: numpy.float foi removido no NumPy 1.20
import numpy as np
# x = np.float(3.14)  # Descomente para testar

# ❌ DEPRECADO: collections.Mapping movido para collections.abc
# from collections import Mapping  # Descomente para testar

# ✅ CORRETO: Use collections.abc
from collections.abc import Mapping

# ❌ DEPRECADO: DataFrame.append() foi deprecado no pandas 1.4.0
import pandas as pd

def example_deprecated_append():
    """Exemplo de uso deprecado do append."""
    df1 = pd.DataFrame({'A': [1, 2]})
    df2 = pd.DataFrame({'A': [3, 4]})
    
    # ❌ DEPRECADO
    # result = df1.append(df2)  # Descomente para testar
    
    # ✅ CORRETO
    result = pd.concat([df1, df2], ignore_index=True)
    return result

# ❌ DEPRECADO: sklearn.cross_validation foi movido
# from sklearn.cross_validation import train_test_split  # Descomente para testar

# ✅ CORRETO
from sklearn.model_selection import train_test_split

print("✅ Este arquivo está usando código atualizado (não deprecado)")
