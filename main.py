import functions_psql as functions_psql
import functions as func

PSQL = functions_psql.PSQL("postgres", "1", 5434, "clients_db")

# Функция создающая таблицы
#func.create_table(PSQL)

# Создание клиентов
#func.add_client(PSQL, 'Юрий', 'Иванов', 'uivanov@mail.ru', '1112319')      --id = 6
#func.add_client(PSQL, 'Наталья', 'Иванова', 'nivanova@mail.ru', '111')     --id = 8
#func.add_client(PSQL, 'Татьяна', 'Иванова', 'tivanova@mail.ru', '222')     --id = 9
#func.add_client(PSQL, 'Иван', 'Дмитриенко', 'idmitr@google.com', '333')    --id = 10

# Добавление доп. номеров
# func.add_phone(PSQL, 7, '123456')
# func. add_phone(PSQL, 8, '147852369')
# func. add_phone(PSQL, 9, '21010')
# func. add_phone(PSQL, 9, '21011')

# Измененение в данных клиента
#func.update_client(PSQL, 7, 'Дмитрий', 'Агафьев', 'mail.ru', '1112319', '4445555')
#func.update_client(PSQL, 7, 'Алена', 'Агафьева', 'mail.ru', '1112319', '4445555')
#func.update_client(PSQL, 7, None, None, None, '4445555', '44455556')

# Удаление номера
#func.delete_phone(PSQL, 7, "123456")
#func.delete_phone(PSQL, 8)

# Удаление клиента
#func.delete_client(PSQL, 8)

# Нахождение клиента по его данным
#func.selected_data(PSQL, 'Иван', 'Дмитриенко', 'idmitr@google.com')
#func.selected_data(PSQL, None, None, None, '222')