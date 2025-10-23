import subprocess


def test_modelo():

    resultado = subprocess.run(
        ["python", "screening.net"],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0, f"Erro na execução: {resultado.stderr}"

    # verifica se o print final está presente
    assert "Treinamento concluído" in resultado.stdout, \
        f"Saída inesperada:\n{resultado.stdout}"