import json,pytest,requests


#将dict或list转化成string
def test_dumps():
    dict={'k1':'v1'}
    dumps_sth=json.dumps(dict)
    assert (type(dumps_sth)) == str


#将string转换成dict或list
def test_loads():
    str='{"k1": "v1"}'
    loads_sth=json.loads(str)
    assert type(loads_sth) == dict


#往json文件写入内容
def test_dump():
    file_path=r"E:\光荣之路\测试开发\corweixindemo\corweixindemo\testdata\member.json.py"
    sth={'age':18}
    json.dump(sth,open(file_path,'w'))
    json_object = json.load(open(file_path,'r'))
    return json_object
    assert type(file_path) == dict
    #无法追加内容，会把之前的json文件内容覆盖

#读取json文件
def test_load():
    file_path=r"E:\光荣之路\测试开发\corweixindemo\corweixindemo\testdata\member.json.py"
    with open(file_path,encoding='utf-8') as f:
        json_object = json.load(f,encoding='utf-8')
        return json_object
    assert type(file_path) == dict



'''
当url为get方法，且使用params传递参数，执行结果
相同点：使用get和post都可以请求和响应成功
'''
def test_getmethod_usepost():
    payload={'q':'电影'}
    url='https://www.douban.com/search'  #get请求
    res1=requests.get(url,params=payload)
    print("res1_url****"+res1.url)
    #输出结果  . res1_url****https://www.douban.com/search?q=%E7%94%B5%E5%BD%B1
    print(res1.text)
    res2=requests.post(url,params=payload)
    print("res2_url****"+res2.url)
    #输出结果 res2_url****https://www.douban.com/search
    print(res2.text)




'''
当url为post方法，且需要添加请求body，执行结果
1、使用get请求失败，请求时不会拼接请求体

. res_url****https://accounts.douban.com/j/mobile/login/basic
<bound method Response.json of <Response [403]>>

2、使用post，请求体使用params添加请求body，请求失败

. res_url****https://accounts.douban.com/j/mobile/login/basic?ck=&name=18500910544&password=Echoque0612&remember=False&ticket=
<bound method Response.json of <Response [200]>>
用户名或密码错误
'''

def test_post():
    mypayload = {'ck': '', 'name': '18500910544','password':'Echoque0612','remember':False,'ticket':''}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://accounts.douban.com/j/mobile/login/basic'
    #post方法传入请求体使用data或json
    res=requests.get(url,verify=False,headers=myheader,data=mypayload)
    # res=requests.post(url,verify=False,headers=myheader,data=mypayload)
    # res=requests.post(url,verify=False,headers=myheader,params=mypayload)

    print("res_url****"+res.url)
    print(res.json)
    print (res.json().get('description'))
    assert res.json().get('description')=='处理成功'


@pytest.mark.parametrize("size,order", [
            (10, 'desc'),(20,"asc")])
def test_get(size,order):
    mypayload = {'page': '1', 'size': size,'order':order,'orderby':'percent','order_by':'percent','market':'HK','type':'hk','_':'1553416305026'}
    myheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    url='https://xueqiu.com/service/v5/stock/screener/quote/list'
    # res=requests.get(url,verify=False,headers=myheader,params=mypayload)
    res=requests.post(url,verify=False,headers=myheader,params=mypayload)
    print (res.json())
    print("res_url****"+res.url)
    listlenth=len(res.json().get("data").get("list"))
    assert listlenth==size





