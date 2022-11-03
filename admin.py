# gunakan modul json
import json
from datetime import datetime
import pytz


date = datetime.now(pytz.timezone('Etc/GMT-11')).strftime('%Y-%m-%d')
json_files = open('/workspaces/machinery/laundry/datas/member.json')

def new_member():
    name = input("masukan nama member baru")

    def write_json(new_data, filename = '/workspaces/machinery/laundry/datas/member.json'):
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data["member"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

        print("data succesfully added", new_data)
    
    new_data = {
        "id":id,
        "name":name,
        "date":date
        }
        
    write_json(new_data)

def read_member():
    x =  json_files
    data = json.load(x)
    for x in data['member']:
        print(x)


def look_member(name):
    try:
        datas = []
        x = json_files
        data = json.load(x)
        for x in data['member']:
            if x['name'] == name:
                datas.clear()
                for i in x:
                    datas.append(x[i])
                break

            else:
                datas.clear()
                datas.append(name)
                datas.append(date)
                continue
        
        name = datas[0]
        mdate = datas[1]

        # print(datas)
        return name, mdate
    
    except ValueError:
        return name
        
# # print(read_member())
# print(look_member('John'))
# # name = 'John'

