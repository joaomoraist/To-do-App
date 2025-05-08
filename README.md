# To-do App

Este é um projeto simples criado por mim e outros colaboradores, cujos dados de mídia social compartilharei nas próximas seções. Foi um trabalho semestral exigido pela universidade **UniFECAF** e o objetivo principal é ajudar outras pessoas a organizar suas tarefas com um aplicativo bacana.

![Pasted image 20250420005731](https://github.com/user-attachments/assets/0410e1e7-c780-41bf-9df0-7e6c271cff00)

<hr>

## Objetivos do Projeto

- **Adicionar uma nova tarefa**: Criar uma nova tarefa
- **Excluir a tarefa desejada**: Excluir uma tarefa
- **Editar uma tarefa**: Poder alterar seu arquivo
- **Filtrar/Organizar suas tarefas**: Exibir suas tarefas filtradas por pasta, busca ou outros
- **Interface amigável**: Uma interface de usuário agradável e intuitiva

## Objetivos da Universidade

- [x] **Gerenciamento de dados**

- [x] **Fluxograma**

- [x] **Interface para o usuário**

- [x] **Validação de Dados**

- [x] **Linguagem de Programação**

- [x] **Integração Front-end e Back-end**

- [x] **Autenticação de usuário**

- [x] Conexão com o banco de dados

- [x] Perfis de Usuário

#### Fulling all of theses requirements give us a total of 3 points in ours Semester grade

<hr>

## Technologies Used

### Backend

- Python
- MySQL
- Sys Library
- Os Library
- Pathlib Library
- Json Library and Files
### Frontend

- Tkinter

<hr>

## Project Structure

```mathematica
src\
└── Back End\
│	└── database_function.py
│	└── SQL Script\
│		└── sqlfile.sql
│
└── Front End\
	└── assets\
	│	└── ... (Image Files)
	└── gui.py ... gui12.py
	└── changewindows.py
	└── functions.py
	└── data_file.json
	└── dados_login.json
	└── Janelas e objetivo.xlsx
```

![Pasted image 20250420021004](https://github.com/user-attachments/assets/65b3c54e-f2e2-4d9c-8b01-29975f161867)


<hr>

## Installation

#### Prerequisites
 - Python
#### Steps

1. Clone this repository:
    ```shell
    git clone https://github.com/will-csc/To-do-App.git
    cd your-repo
    ```

*Obs:* In the **"Back End"** folder, change the **"database_functions.py"** file and put your password and name in row 31 at **"connection()"** function.

Example:
```Sql
def connection():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sny-301mv",
        database="todo_app"
    )

    return conexao, conexao.cursor()

```

2. Install these librarys:

```cmd
pip install requests
pip install Pillow
pip install Jinja2
pip install mysql-connector-python
pip install --upgrade mysql-connector-python
pip install twilio
```

3. Execute the SQL Statement
```sql
DROP DATABASE IF EXISTS todo_app;
CREATE DATABASE IF NOT EXISTS todo_app;
USE todo_app;

/*------------------ TABELA DE USUARIOS ----------------*/
CREATE TABLE IF NOT EXISTS users(
	id_user INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL UNIQUE,
    e_mail VARCHAR(50) NOT NULL UNIQUE,
    phone BIGINT NOT NULL,
    userpassword VARCHAR(50) NOT NULL,
    retrieve_code BIGINT NOT NULL,
    user_rank INT DEFAULT 1 NOT NULL
);
ALTER TABLE users ADD CONSTRAINT chk_retrieve_code CHECK (retrieve_code > 999999999);
ALTER TABLE users ADD CONSTRAINT chk_user_rank CHECK (user_rank IN (1,2));

/*------------------ TABELA DE DOCUMENTOS RELACIONADOS AO USUÁRIO ----------------*/
CREATE TABLE IF NOT EXISTS documents(
	id_docs INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT NOT NULL,
    doc_name VARCHAR(100) NOT NULL,
    doc_path VARCHAR(700) NOT NULL UNIQUE,
    deadline DATE NOT NULL,
    week_day VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE
    CASCADE ON UPDATE CASCADE
);

/*---------------- FUNÇÃO PARA PREENCHER NOME DO DIA --------------------------*/
DELIMITER $$

CREATE FUNCTION nome_dia_semana(data DATE) RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    DECLARE dia_semana INT;
    SET dia_semana = WEEKDAY(data); -- Segunda = 0, Domingo = 6

    RETURN CASE dia_semana
        WHEN 0 THEN 'Segunda'
        WHEN 1 THEN 'Terça'
        WHEN 2 THEN 'Quarta'
        WHEN 3 THEN 'Quinta'
        WHEN 4 THEN 'Sexta'
        WHEN 5 THEN 'Sábado'
        WHEN 6 THEN 'Domingo'
    END;
END$$

DELIMITER ;

/*------------ TRIGGER PARA INSERÇÃO AUTOMÁTICA -----------------*/
DELIMITER $$

CREATE TRIGGER before_insert_documents
BEFORE INSERT ON documents
FOR EACH ROW
BEGIN
    SET NEW.week_day = nome_dia_semana(NEW.deadline);
END$$

DELIMITER ;
```

4. Execute the following command inside the **"Front End"** folder
```cmd
python gui.py
```

<hr>

## Contributors

Let's connect! 📫 by Mail, Linkedin or WhatsApp<br>

#### William
<div> 
  <a href="mailto:william.cesarbds2016@gmail.com" target="_blank">
  <img src="https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico" 
       width="40" height="40" alt="Gmail">
</a>
  <a href="https://www.linkedin.com/in/william-cesar-7b7b89202/" target="_blank">
    <img src="https://t.ctcdn.com.br/ClbNm_AxWl6gDsKOKmnZXzmsIXI=/1080x1080/smart/i490027.jpeg" 
         width="40" height="40" alt="LinkedIn">
  </a> 
    <a href="https://wa.me/5511969541207" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" 
         width="40" height="40" alt="WhatsApp">
    </a>
<a href="https://github.com/will-csc" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40" height="40" alt="GitHub">
  </a>
</div>

#### Eduardo
<div> 
  <a href="mailto:eduardo170620063103@gmail.com" target="_blank">
    <img src="https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico" 
       width="40" height="40" alt="Gmail">
</a>
  <a href="https://www.linkedin.com/in/eduardooliveira1706" target="_blank">
    <img src="https://t.ctcdn.com.br/ClbNm_AxWl6gDsKOKmnZXzmsIXI=/1080x1080/smart/i490027.jpeg" 
         width="40" height="40" alt="LinkedIn">
  </a> 
    <a href="https://wa.me/5511984325997" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" 
         width="40" height="40" alt="WhatsApp">
    </a>
</div>

#### João
<div> 
  <a href="mailto:jv.timotio@gmail.com" target="_blank">
    <img src="https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico" 
       width="40" height="40" alt="Gmail">
</a>
  <a href="https://www.linkedin.com/in/joão-morais-t/" target="_blank">
    <img src="https://t.ctcdn.com.br/ClbNm_AxWl6gDsKOKmnZXzmsIXI=/1080x1080/smart/i490027.jpeg" 
         width="40" height="40" alt="LinkedIn">
  </a> 
    <a href="https://wa.me/5511993134134" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" 
         width="40" height="40" alt="WhatsApp">
    </a>
</div>

#### Matheus
<div> 
  <a href="mailto:matheusrochacontato892@gmail.com" target="_blank">
    <img src="https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico" 
       width="40" height="40" alt="Gmail">
</a>
  <a href="https://www.linkedin.com/in/matheus-rocha-b6622b262?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank">
    <img src="https://t.ctcdn.com.br/ClbNm_AxWl6gDsKOKmnZXzmsIXI=/1080x1080/smart/i490027.jpeg" 
         width="40" height="40" alt="LinkedIn">
  </a> 
    <a href="https://wa.me/5511980542175" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" 
         width="40" height="40" alt="WhatsApp">
    </a>
</div>
