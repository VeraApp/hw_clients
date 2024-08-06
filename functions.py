
def create_table(PSQL):
    PSQL.set_query("""
        CREATE TABLE IF NOT EXISTS clients(
            id serial PRIMARY KEY,
            name varchar(20) NOT NULL,
            surname varchar(60) NOT NULL,
            email varchar(30) UNIQUE NOT NULL
        ); 
    """)
    PSQL.set_query("""
        CREATE TABLE IF NOT EXISTS phone(
            client_id integer NOT NULL references clients(id),
            number varchar(11) UNIQUE, 
            constraint pk primary key (client_id, number)
        );
    """)

def add_phone(PSQL, client_id, number):
    try:
        if number:
            PSQL.set_query(""" INSERT INTO phone(client_id, number)
                                VALUES((%s), (%s))""", (client_id, number))
    except Exception as error:
        msg = ("ERROR: Не удалось добавить номер телефона - ", error)

def add_client(PSQL, name, surname, email, number):
    try:
        client_id = PSQL.get_query(""" INSERT INTO clients(name, surname, email)
                                       VALUES((%s), (%s), (%s))
                                       RETURNING id;""", (name, surname, email))[0]
        add_phone(PSQL, client_id, number)
    except Exception as error:
        msg = ("ERROR: Не удалось добавить клиента или номер телефона - ", error)
    return client_id

def update_client(PSQL, client_id, name=None, surname=None, email=None, old_number=None, new_number= None):
    if old_number and new_number:
        PSQL.set_query(""" UPDATE phone 
                               SET number = (%s)
                                WHERE number = (%s)""", (new_number, old_number))
    if name and surname and email:
        PSQL.set_query(f""" UPDATE clients 
                       SET name = (%s), 
                           surname = (%s),
                           email = (%s)
                        WHERE id = {client_id}""", (name, surname, email))

def delete_phone(PSQL, client_id, phone=None):
    if phone:
        PSQL.set_query(f""" 
            DELETE FROM phone
            WHERE client_id = (%s) and number = (%s)
        """, (client_id, phone))
    else:
        PSQL.set_query(f"""
            DELETE FROM phone
            WHERE client_id = {client_id}
    """)

def delete_client(PSQL, client_id):
    # Удаляем все номера данного клиента
    delete_phone(PSQL, client_id)

    PSQL.set_query(f"""
        DELETE FROM clients
        WHERE id = (%s)
    """, [client_id])
def selected_data(PSQL, name=None, surname=None, email=None, phone=None):
    name_str = ""
    surname_str = ""
    email_str = ""
    if phone is None:
        if name:
            name_str = f"name = '{name}' "
            if surname:
                surname_str = f" and surname = '{surname}'  "
                if email:
                    email_str = f" and email = '{email}' "
            else:
                if email:
                    email_str = f" and email = '{email}' "
        else:
            if surname:
                surname_str = f" surname = '{surname}' "
                if email:
                    email_str = f" and email = '{email}' "
            else:
                if email:
                    email_str = f" email = '{email}' "
        full_str = name_str + surname_str + email_str
        result = PSQL.get_query(f"""
            SELECT * FROM clients
            WHERE {full_str};
        """)
    else:
        client_id = PSQL.get_query(f"""
            SELECT client_id FROM phone
            WHERE number = '{phone}';
        """)[0]
        client_id = int(client_id[0])
        result = PSQL.get_query(f"""
            SELECT * FROM clients
            WHERE id ={client_id};
        """)
    for res in result:
        id = res[0]
        name = res[1]
        surname = res[2]
        email = res[3]
        print(f"Клиент с id = {id}. Имя: {name}, фамилия:  {surname}, email: {email}")