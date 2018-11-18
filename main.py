import db
import format
import questions


def main(db_path,data_format):
    conn = db.set_connection(db_path)

    for quest,sql in sorted(questions.q.items()):
        data = db.get_data(conn, sql)

        if (data_format == 'json'):
            format.return_json(data,quest)

        elif (data_format == 'xml'):
            format.return_xml(data,quest)

        elif (data_format == 'csv'):
            format.return_csv(conn,quest,sql)

        elif (data_format == 'table'):
            format.return_table(conn,quest,sql)

    conn.close()


