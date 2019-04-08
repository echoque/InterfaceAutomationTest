import json,pytest


#将dict或list转化成string
def test_dumps(sth):
    return json.dumps(sth)

#将string转换成dict或list
def test_loads(sth):
    return json.loads(sth)

#往json文件写入内容
def test_dump(sth,file):
    json.dump(sth,open(file,'w'))
    json_object = json.load(open(file,'r'))
    return json_object
    #无法追加内容，会把之前的json文件内容覆盖

#读取json文件
def test_load(file):
    with open(file,encoding='utf-8') as f:
        json_object = json.load(f,encoding='utf-8')
        return json_object


def test_add_json():
    pass


if __name__ == '__main__':
    dict={'k1':'v1'}
    dumps_sth=test_dumps(dict)
    print(dumps_sth)
    print(type(dumps_sth))
    print('\n')
    str='{"k1": "v1"}'
    print(test_loads(str))
    print(type(test_loads(str)))
    print('\n')
    file_path=r"E:\光荣之路\测试开发\corweixindemo\corweixindemo\testdata\member.json.py"
    print(test_load(file_path))
    print(type(test_load(file_path)))
    print('\n')
    d1 = {'age':18}
    print(test_dump(d1,file_path))
    print(type(test_dump(d1,file_path)))


