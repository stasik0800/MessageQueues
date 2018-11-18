import json
from dicttoxml import dicttoxml
import pandas as pd


def return_xml(body,quest):
        xml_file_name = quest + ".xml"
        xml = dicttoxml(body)

        with open(xml_file_name, "w") as xml_output:
            xml_output.write(xml)
            print ('created ' + xml_file_name)


def return_json(body,quest):
        json_file_name = quest + ".json"

        with open(json_file_name, 'w') as json_output:
            json.dump(body,json_output)
            print ('created ' + json_file_name)


def return_csv(conn,quest,sql):
        csv_file_name = quest + ".csv"

        results = pd.read_sql_query(sql, conn)
        results.to_csv(csv_file_name, index=False , encoding='utf-8-sig')

        print ('created ' + csv_file_name)



def return_table(conn,quest_num,sql):
        cur = conn.cursor()

        drop_table = "drop table if exists {0};" .format(quest_num)
        cur.execute(drop_table)

        sql = """create table {0} as  {1}""".format(quest_num,sql)
        cur.execute(sql)

        print("created table {0}").format(quest_num)

