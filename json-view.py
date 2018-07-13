import json
import xlwt
import time
class JsonTools():
    def __init__(self,path):
        self.jsonPath = path
        # 保存初始路径
        self.json = self.loadJson(path)
        # 保存json处理后的dict list

    def loadJson(self, path):
        """该方法用于初始化json文本，对json文本逐行转化为dict对象并存入一个新的list"""
        with open(path, 'rt', encoding='utf-8') as fout:
            # 在当前目录下打开json文本文件
            json_content = fout.readlines()
            # 逐行读取文件内容，每行作为一个元素放入一个list
        json_list = []
        for each in json_content:
            json_list.append(json.loads(each))
            # 对list中的每一段json文本转化为dict对象，将dict对象作为元素放入一个新的列表中
        return json_list
        # 返回最终包含dict元素的列表

    def filter(self, key, field, field_value1=None, field_2=None, field_value2=None, empty_filter=None):
        """
        该方法用于从初始化后的列表中，循环按字典的key提取对应的value值
        param：
        key: 返回的字典中的key对应的字段
        field：要过滤的字段名
        field_value1：field的补充筛选条件，类似于sql的where field == field_value1
        field_2：如果value是一个字典，需要按子key进行提取时可以使用该参数
        field_value2：子key的补充筛选条件
        empty_filter：过滤value为空或空列表[]的元素
        """
        cmp = {}
        for each in self.json:
            # try:
            #     if not empty_filter:
            #         cmp[each[key]] = each[field]
                    # 如果empty_filter为None，将每一行key字段的值作为键，field对应的值作为value保存到cmp字典中
                # else:
                #     if each[field] != [] and each[field] != None and each[field] != [""]:
                #         如果empty_filter字段为空，则对field对应的值进行判空，如果不为空列表、None、空列表中含有空字符串情况，则进行保存
                        # cmp[each[key]] = each[field]
            # except KeyError:
                #     cmp[each[key]] = "Nonexistent key"
            try:
                if not empty_filter:
                    if not isinstance(cmp[each[key]], list):
                        cmp[each[key]] = []
                    cmp[each[key]].append(each[field])
                    # 如果empty_filter为None，将每一行key字段的值作为键，field对应的值作为value保存到cmp字典中
                else:
                    if each[field] != [] and each[field] != None and each[field] != [""]:
                        # 如果empty_filter字段为空，则对field对应的值进行判空，如果不为空列表、None、空列表中含有空字符串情况，则进行保存
                        if not isinstance(cmp[each[key]], list):
                            cmp[each[key]] = []
                        cmp[each[key]].append(each[field])
            except KeyError:
                cmp[each[key]] = "Nonexistent key"
        return cmp

def time_trans(Unixtime):
    st = time.localtime(Unixtime)
    return time.strftime('%Y-%m-%d %H:%M:%S', st)

viewjson = JsonTools('View201807071114.json')
viewjsonContent = viewjson.json
print(viewjsonContent[-1].keys())
for each in viewjsonContent[::-1]:
    print(time_trans(each["CreateTime"]),"SiteId",each['SiteId'])

