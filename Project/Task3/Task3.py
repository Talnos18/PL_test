import json
from sys import argv

def task3(name_json_test, name_json_values):

    def read_json(name_json):
        with open(name_json, "r") as f:
            data_json = json.load(f)
        return data_json

    def test_results(json_result_test, json_fill):
        for i in json_result_test:
            for v in json_fill['values']:
                if i.get('id') == v.get('id'):
                    i['value'] = v.get('value')
                    break
            if 'values' in i.keys():
                test_results(i['values'], json_fill)
        return {'tests' : json_result_test}

    def write_json(json_test, json_values):
        with open('report.json', "w") as f:
            json.dump(test_results(json_test['tests'], json_values), f, indent=1)

    return write_json( read_json(name_json_test), read_json(name_json_values)),\
           print("report.json создан")


if __name__ == '__main__':
    name_test, name_values = str(argv[1]), str(argv[2])
    task3(name_test,name_values)