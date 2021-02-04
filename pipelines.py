# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http import request
import requests
import os
class TutorialPipeline:
    def process_item(self, item, spider):
        res = requests.get(url=item['img_url'])
        file_name =  item['img_url'].split('/')[-1]
        path = 'wallpaper'
        # creat the path directory if there is not directory
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path=path)
            pass
        # creat the file if the file is not exist
        if os.path.exists(path + '/' + file_name):
            pass
        else:
            with open(path +'/' + file_name, mode='wb') as f:
                f.write(res.content)
        return item
