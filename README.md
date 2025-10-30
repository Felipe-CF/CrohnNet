# Python Dependency Scan - Verificação de Código Deprecado

Este projeto implementa verificação automática de código deprecado em projetos Python.

## Ferramentas Utilizadas

1. **Script Customizado** (`scripts/check_deprecated.py`)
   - Detecta padrões deprecados conhecidos
   - Verifica imports, funções e métodos deprecados
   - Falha o build se encontrar problemas

2. **Pylint**
   - Verificação adicional de deprecations
   - Integrado ao pipeline CI/CD

## Como Usar

### Localmente

\`\`\`bash
# Instalar dependências
pip install -r requirements.txt

# Executar verificação
python scripts/check_deprecated.py
\`\`\`

### No Pipeline

O workflow `.github/workflows/deprecated-code-check.yml` executa automaticamente em:
- Push para branches main, develop, feature/*
- Pull requests para main e develop

## Padrões Deprecados Detectados

- TensorFlow: `tf.contrib`, imports deprecados
- NumPy: `numpy.float`, `numpy.int`, `numpy.bool`
- Pandas: `DataFrame.append()`, `pandas.np`
- Scikit-learn: `sklearn.cross_validation`, `sklearn.grid_search`
- Python stdlib: `collections.Mapping`, `collections.Sequence`

## Adicionando Novos Padrões

Edite o dicionário `DEPRECATED_PATTERNS` em `scripts/check_deprecated.py`:

\`\`\`python
DEPRECATED_PATTERNS = {
    "modulo.funcao_antiga": "Use modulo.funcao_nova",
    # Adicione mais padrões aqui
}
\`\`\`

## Status do Pipeline

O pipeline falhará (❌) se código deprecado for detectado.
O pipeline passará (✅) apenas quando todo código estiver atualizado.
