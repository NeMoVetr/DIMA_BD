import mysql.connector
# ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ К БД
def price(conn):
    sql = """
    select sum(Оплата) from price;
    """
 cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchone()
    print(results)
def count_detail(conn):
    sql = """
    select sum(Количество_запчастей) from price;
    """
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchone()
    print('Запчасти')
    for row in results:
        print(row,'\n')
def post(conn, year):
    sql = """
    select avg(Зарплата) from post
    where Название=%s
    """
    cur = conn.cursor()
    cur.execute(sql, (year,))
    results = cur.fetchone()
    for row in results:
        print(row,'\n')

def detail(conn):
    sql = """
    select Деталь, Цена from import_
    group by Деталь, Цена
    order by Цена desc
    limit 5;
    """
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchmany(5)
    for row in results:
        print(row,'\n')
# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ book
def create_import(Товар, Деталь, Цена):
    sql = """
    # INSERT INTO import_(Товар, Деталь, Цена)
    VALUES (%s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
def get_import(conn, book_id):
    sql = """
    SELECT *
    FROM import_
    WHERE product_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (book_id,))
    return cur.fetchone()
def update_import(conn, book):
    sql = """
    UPDATE import_
    SET Товар = %s, Деталь= %s, Цена = %s
    WHERE product_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
def delete_import(conn, book_id):
    sql1 = "DELETE FROM import_type WHERE product_id=%s"
    sql2 = "DELETE FROM import_ WHERE product_id = %s"
    cur = conn.cursor()
    cur.execute(sql1, (book_id,))
    cur.execute(sql2, (book_id,))
    conn.commit()
# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ client
def create_client(conn, client):
    sql = """
    INSERT INTO client_(servic_id, ФИО, Дата_заказа)
    VALUES (%s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()
def get_client(conn, client_id):
    sql = """
    SELECT * 
    FROM client_
    WHERE servic_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (client_id,))
    return cur.fetchone()
def update_client(conn, client):
    sql = """
    UPDATE client_
    SET servic_id = %s, ФИО = %s, Дата_заказа = %s
    WHERE client_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()
def delete_client(conn, client_id):
    sql2 = "DELETE FROM client_ WHERE servic_id = %s"
    cur = conn.cursor()
    cur.execute(sql2, (client_id,))
    conn.commit()
# ФУНКЦИИ ДЛЯ ДОБАВЛЕНИЯ/ПРОСМОТРА/ОБНОВЛЕНИЯ/УДАЛЕНИЯ ДАННЫХ ИЗ ТАБЛИЦЫ order
def create_post(conn, order):
    sql = """
    INSERT INTO fix_PC.post(employee_id, Название, Зарплата)
    VALUES (%s, %s, %s)
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()
def get_post(conn, order):
    sql = """
    SELECT employee_id, Название, Зарплата
    FROM fix_pc.post
    WHERE employee_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, (order,))
    return cur.fetchone()
def update_post(conn, order):
    sql = """
    UPDATE post
    SET employee_id = %s, Название = %s, Зарплата = %s
    WHERE employee_id = %s
    """
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()
def delete_post(conn, order):
    sql3 = "DELETE FROM post WHERE employee_id = %s"
    cur = conn.cursor()
    cur.execute(sql3, (order,))
    conn.commit()
# ФУНКЦИИ ДЛЯ ПОДКЛЮЧЕНИЯ И ОТКЛЮЧЕНИЯ ОТ БД
def connect_to_db(host, user, password, database):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f"Успешное подключение к {database} с помощью MySQL Connector/Python\n")
    except Exception as e:
        print(f"Произошла ошибка при подключении к базе данных: {e}")
    return conn
def close_connection(conn):
    if conn:
        conn.close()
        print("\nСоединение с базой данных закрыто")
# ОСНОВНАЯ ФУНКЦИЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЕМ ПРОГРАММЫ
def main():
    host = "localhost"
    user = "root"
    password = "G1.G2.ad"
    database = "fix_PC"
    conn = connect_to_db(host, user, password, database)
    while True:
        print("\nВыберите таблицу с которой хотите взаимодействовать \n или одно из функциональных требований:")
        print("1) post")
        print("2) client_")
        print("3) import_")
        print(" ФУНКЦИОНАЛЬНЫЕ ТРЕБОВАНИЯ")
        print("4) Прибыль")
        print("5) Запчасти")
        print("6) Зарплата")
        print("7) Детали")
        print("8) Выход")
        table_choice = input("Введите номер пункта: ")
        if table_choice == '8':
            break
        if(table_choice == '1' or table_choice == '2' or table_choice == '3' ):
            print("\nВыберите действие:")
            print("1) Добавить запись")
            print("2) Просмотреть запись")
            print("3) Обновить запись")
            print("4) Удалить запись")
            print("5) Назад")
            action_choice = input("Введите номер пункта: ")
            if action_choice == '5':
                continue
        if table_choice == '1':  # order
            if action_choice == '1':
                new_order = tuple(input("Введите данные работника через запятую(employee_id, Название, Зарплата): ").split(','))
                create_post(conn, new_order)
            elif action_choice == '2':
                ID_order = input("Введите ID работника: ")
                order = get_post(conn, ID_order)
                print(order)
            elif action_choice == '3':
                updated_order_id = input("Введите ID работника для обновления: ")
                updated_order = list(input("Введите обновленные данные заказа через запятую(employee_id, Название, Зарплата): ").split(','))
                updated_order.append(updated_order_id)
                updated_order_tuple = tuple(updated_order)
                update_post(conn, updated_order_tuple)
            elif action_choice == '4':
                ID_order_del = input("Введите ID заказа для удаления: ")
                delete_post(conn, ID_order_del) 
        elif table_choice == '2':  # client   
            if action_choice == '1':
                new_client = tuple(input("Введите данные клиента через запятую(servic_id, ФИО, Дата_заказа): ").split(','))
                create_client(conn, new_client)            
            elif action_choice == '2':
                ID_client = input("Введите ID клиента: ")
                client = get_client(conn, ID_client)
                print(client)            
            elif action_choice == '3':
                updated_client_id = input("Введите ID клиента для обновления: ")
                updated_client = list(input("Введите обновленные данные клиента через запятую(servic_id, ФИО, Дата_заказа): ").split(','))
                updated_client.append(updated_client_id)
                updated_client_tuple = tuple(updated_client)
                update_client(conn, updated_client_tuple)            
            elif action_choice == '4':
                ID_client_del = input("Введите ID клиента для удаления: ")
                delete_client(conn, ID_client_del)
        elif table_choice == '3':  # book
            if action_choice == '1':
                new_book = tuple(input("Введите информацию о товаре через запятую\n(Товар, Деталь, Цена): ").split(','))
                create_import(conn, new_book)
            elif action_choice == '2':
                ID_book = input("Введите ID товара: ")
                book = get_import(conn, ID_book)
                print(book)
            elif action_choice == '3':
                updated_book_id = input("Введите ID товара для обновления: ")
                updated_book = list(input("Введите обновленную информацию о книге через запятую\n(Товар, Деталь, Цена): ").split(','))
                updated_book.append(updated_book_id)
                updated_book_tuple = tuple(updated_book)
                update_import(conn, updated_book_tuple)           
            elif action_choice == '4':
                ID_book_del = input("Введите ID товара: ")
                delete_import(conn, ID_book_del)
        elif table_choice == '4':
            price(conn)
            continue
        elif table_choice == '5':
            count_detail(conn)
            continue
        elif table_choice == '6':
            year = input("Введите название профессии: ")
            post(conn, year)
            continue
        elif table_choice == '7':
            detail(conn)
            continue
        else:
            print("Неверный пункт. Пожалуйста, попробуйте еще раз.")
    close_connection(conn)
if __name__ == "__main__":
    main()
