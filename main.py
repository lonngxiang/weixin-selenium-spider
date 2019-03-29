from selenium import webdriver
import json
import time
from lxml import etree


contents=[]
driver = webdriver.Chrome()
# content_all = ["资生堂", "肌肤之钥", "NARS", "圣罗兰", "汤姆福特", "茵芙莎", "芭比波朗", "阿玛尼", "娇兰", "泊美", "海蓝之谜", "姬芮", "悦诗风吟", "希思黎",
#                "迪奥", "莱珀妮", "自然堂", "佰草集", "百雀羚", "相宜本草", "美宝莲", "伊蒂之屋", "兰蔻", "SK-II", "香奈儿"]
content_all = ["资生堂", "肌肤之钥", "NARS", "圣罗兰", "汤姆福特", "茵芙莎",]
for k in range(len(content_all)):


    driver.get('https://weixin.sogou.com/')
    time.sleep(2)
    input_text=driver.find_element_by_xpath('//input[@type="text"]')
    input_text.send_keys("{}".format(content_all[k]))
    time.sleep(1)
    button=driver.find_element_by_xpath('//input[@value="搜文章"]')
    button.click()
    time.sleep(3)
    tool=driver.find_element_by_xpath('//div[@id="tool_show"]')
    tool.click()
    times=driver.find_element_by_xpath('//span[@class="all-wy-box"][1]')
    times.click()
    timess=driver.find_element_by_xpath('//div[contains(@class,"time-box")]/a[@data-type="1"]')
    timess.click()
    time.sleep(3)


    print(driver.current_url)
    html1=etree.HTML(driver.page_source)
    try:
        if html1.xpath('//ul[@class="news-list"]/li'):
            for j in range(len(html1.xpath('//ul[@class="news-list"]/li'))):
                name1=html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/h3/a'.format(j+1))[0]
                name=name1.xpath('string(.)')
                print(name)
                link=html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/h3/a/@href'.format(j+1))[0]
                info1=html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/p'.format(j+1))[0]
                info=info1.xpath('string(.)')
                author=html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/div[@class="s-p"]/a/text()'.format(j+1))[0]
                time1=html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/div[@class="s-p"]/span/text()'.format(j+1))[0]
                contents.append([name,link,info,author,time1])
                print(name,link,info,author,time1)
            time.sleep(2)
        else:
            pass
    except:
        pass




    try:
        for i in range(2):
            if driver.find_element_by_xpath('//div[@id="pagebar_container"]/a[@id="sogou_next"]'):
                next=driver.find_element_by_xpath('//div[@id="pagebar_container"]/a[@id="sogou_next"]')
                next.click()
                time.sleep(3)
                print(i)
                print("###################")
                print(driver.current_url)
                # print(driver.page_source)
                html1 = etree.HTML(driver.page_source)
                for j in range(len(html1.xpath('//ul[@class="news-list"]/li'))):
                    name1 = html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/h3/a'.format(j + 1))[0]
                    name = name1.xpath('string(.)')
                    print(name)
                    link = html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/h3/a/@href'.format(j + 1))[0]
                    info1 = html1.xpath('//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/p'.format(j + 1))[0]
                    info = info1.xpath('string(.)')
                    author = html1.xpath(
                        '//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/div[@class="s-p"]/a/text()'.format(j + 1))[0]
                    time1 = html1.xpath(
                        '//ul[@class="news-list"]/li[{}]/div[@class="txt-box"]/div[@class="s-p"]/span/text()'.format(
                            j + 1))[0]
                    contents.append([name, link, info, author, time1])
                    print(name, link, info, author, time1)
                time.sleep(2)
            else:
                pass
    except:
        pass


print(contents)
driver.close()
