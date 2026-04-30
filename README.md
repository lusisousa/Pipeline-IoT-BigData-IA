# Pipeline de Dados com IoT, Big Data e IA

## 📌 Sobre o projeto
Este projeto foi desenvolvido como atividade da disciplina **Disruptive Architectures: IoT, Big Data e IA**.

O objetivo principal é construir um **pipeline de dados** utilizando um conjunto de dados de sensores IoT, aplicando conceitos de **Big Data, armazenamento em banco relacional e visualização interativa**.

Neste projeto, os dados de temperatura são extraídos de um arquivo CSV, tratados com Python, armazenados em um banco **PostgreSQL executado em Docker** e posteriormente visualizados em um **dashboard interativo com Streamlit**.

A proposta foi simular um cenário real de monitoramento de sensores IoT, no qual diferentes dispositivos registram temperaturas ao longo do tempo.

---

## 🚀 Tecnologias utilizadas
As principais tecnologias utilizadas no desenvolvimento foram:

- **Python 3**
- **Pandas**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker**
- **Streamlit**
- **Plotly**
- **Git e GitHub**

---

## 📂 Estrutura do projeto
```text
pipeline-iot-docker/
│
├── data/
│   └── temperature_readings.csv
│
├── sql/
│   └── views.sql
│
├── src/
│   └── main.py
│
├── dashboard.py
├── requirements.txt
└── README.md
```

---

## 📊 Base de dados
A base de dados utilizada foi obtida no Kaggle.

🔗 Link para download:  
https://www.kaggle.com/datasets

Após o download, o arquivo CSV deve ser colocado na pasta:

```text
/data
```

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/lusisousa/Pipeline-IoT-BigData-IA.git
cd pipeline-iot-bigdata-ia
```

---

### 2. Criar ambiente virtual
```bash
python -m venv venv
```

### Ativar no Windows
```bash
venv\Scripts\activate
```

---

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

---

### 4. Subir PostgreSQL com Docker
```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```

---

### 5. Criar banco de dados
```bash
docker exec -it postgres-iot psql -U postgres
```

Dentro do PostgreSQL:

```sql
CREATE DATABASE iot_db;
```

---

### 6. Executar pipeline de dados
```bash
py src/main.py
```

Esse comando realiza:
- leitura do CSV
- tratamento dos dados
- inserção no banco
- criação das views SQL

---

### 7. Executar dashboard
```bash
streamlit run dashboard.py
```

O dashboard será aberto no navegador em:

```text
http://localhost:8501
```

---

## 🧠 Views SQL implementadas
Foram criadas três views para análise dos dados:

- **avg_temp_por_dispositivo** → média de temperatura por dispositivo
- **leituras_por_hora** → quantidade de leituras por hora
- **temp_max_min_por_dia** → temperatura máxima e mínima por dia

Essas views facilitam a análise dos dados e a geração dos gráficos no dashboard.

---

## 🔧 Comandos Git utilizados
Durante o desenvolvimento do projeto, foram utilizados os seguintes comandos:

```bash
git init
git add .
git commit -m "Projeto inicial pipeline IoT"
git branch -M main
git remote add origin https://github.com/lusisousa/Pipeline-IoT-BigData-IA.git
git push -u origin main
```

Para atualizações:

```bash
git add .
git commit -m "Atualização do dashboard e views SQL"
git push
```

---

## 💡 Considerações finais
Durante o desenvolvimento deste projeto, pude aplicar na prática conceitos importantes da disciplina, como integração entre **IoT, banco de dados, Docker e visualização de dados**.

A atividade contribuiu bastante para o entendimento de como funciona um pipeline de dados em um cenário próximo ao mercado de tecnologia.

---

## 👨‍💻 Autor

Lucas S. Sousa
