import csv


class LJ_Pipeline(object):
    def open_spider(self,spider):
        try:
            self.file = open('LJ_Data.csv', "w", encoding='utf-8')
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        dict_item = dict(item)   # 生成字典对象

        csv_str = item['name'][0]+','+item['discribe'][0]+','+item['price'][0]+','+item['uprice'][0]+'\n'
        print(csv_str)
        self.file.write(csv_str)

    def close_spider(self, spider):
        self.file.close()
