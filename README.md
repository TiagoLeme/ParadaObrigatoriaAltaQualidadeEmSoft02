# 🧮 Parada Obrigatória 2 — Disciplina: Alta Qualidade em Software

Este repositório faz parte da **disciplina de Alta Qualidade em Software** e tem como objetivo aplicar práticas de **análise de defeitos**, **correção de código** e **testes automatizados**, seguindo metodologias de **TDD (Test-Driven Development)**.

---

## 📁 Estrutura do Repositório

O projeto contém **quatro arquivos principais**, descritos a seguir:

### 1️⃣ `Calculadora.py`

Arquivo original fornecido, contendo o **código-fonte inicial** da calculadora.
Este código apresenta **bugs identificados durante a análise**, servindo como base para o processo de detecção e correção.

---

### 2️⃣ `RelatorioDeBugs.pdf`

Documento contendo a **análise detalhada dos defeitos encontrados** no código original.
O relatório descreve cada bug, seus impactos, passos para reprodução, severidade e as **modificações aplicadas para correção**.

---

### 3️⃣ `CalculadoraCorrigida.py`

Versão **corrigida** do código da calculadora.
Inclui as **correções dos bugs identificados**, melhorias de validação de entrada, tratamento de exceções e aprimoramentos na estrutura do programa.

---

### 4️⃣ `testes.py`

Arquivo que contém os **testes automatizados** implementados para verificar o funcionamento correto das funcionalidades corrigidas.
Esses testes garantem que as alterações realizadas mantêm o comportamento esperado do sistema e evitam a reintrodução de erros.

---

## 🧠 Objetivos do Projeto

* Praticar **identificação e documentação de defeitos** (bug reports).
* Aplicar a metodologia **TDD (Test-Driven Development)**.
* Demonstrar **boas práticas de escrita e correção de código**.
* Validar o código corrigido por meio de **testes automatizados**.

---

## 🚀 Como Executar

1. **Python 3.x** instalado.
2. No terminal, navegue até a pasta do projeto.
3. Para executar a calculadora:

   ```bash
   python CalculadoraCorrigida.py
   ```
4. Para rodar os testes automatizados (se usar `pytest`):

   ```bash
   pytest testes.py
   ```

---

## 👨‍💻 Autor

**Tiago Leme**
Disciplina: *Alta Qualidade em Software*
