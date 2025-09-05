# crawl4ai==0.7.4
import asyncio
import csv
import json

from bs4 import BeautifulSoup
from crawl4ai import *
from datetime import datetime


async def url_craw(url):

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
            # config=crawler_config
        )
        # print(result.markdown)

        return result

async def jdinfo_parse(url):
    # # 解析jd具体内容 job_jd
    job_jd_craw_result = await url_craw(url)
    soup = BeautifulSoup(job_jd_craw_result.cleaned_html, 'html.parser')
    sections = soup.find_all('section')
    jdinfo = [s.text.replace("\n"," ") for s in sections if s.find('strong')]
    # print(jdinfo)

    return jdinfo


async def jobinfo_parse(craw_result):


    # result = await url_craw(url)
    final_result = []
    soup = BeautifulSoup(craw_result.cleaned_html, 'html.parser')

    # print("--------------------------------")
    # print(type(soup))
    # print(soup)

    sections = soup.find_all('section')
    job_section = sections[-4]
    # print("---------------job_section-----------------")
    # print(type(job_section))

    job_section_li = job_section.find_all('li')
    print("---------------len(job_section)-----------------")
    print(len(job_section_li))

    for li in job_section_li:
    # for i in range(1,2):
        # print("---------------li-----------------")
        # print(type(li)) # <class 'bs4.element.Tag'>
        # print(li)
        # li = job_section_li[0]
        # li = job_section_li[i]
        # 解析网页
        job_title = li.find('h3')
        # print("job_tile: " + job_title.text.strip())

        job_link = li.find('a')['href']
        # print("job_link: " + job_link)

        # jd info
        # jd_craw_result = await url_craw(job_link)
        # jd_soup = BeautifulSoup(jd_craw_result.cleaned_html, 'html.parser')
        # jd_sections = jd_soup.find_all('section')
        # jd_info = [s for s in jd_sections if s.find('strong')]

        jd_info = await jdinfo_parse(job_link)
        print('---------jd_info-----------')
        print(type(jd_info))


        job_comany = li.find_all('a')[1]
        # print("job_comany: " + job_comany.text.strip())

        job_comany_link = li.find_all('a')[1]['href']
        # print("job_comany_link: " + job_comany_link)

        job_base = li.find_all('span')[1]
        # print("job_base: " + job_base.text.strip())

        job_time = li.find('time')
        # print("job_time: " + job_time.text.strip())

        final_result.append({"job_tile": job_title.text.strip(),
                             "job_link": job_link,
                             "job_comany": job_comany.text.strip(),
                             "job_comany_link": job_comany_link,
                             "jd_info": jd_info,
                             "job_base": job_base.text.strip(),
                             "job_time": job_time.text.strip()})

    # print(final_result)
    return final_result




async def main():

    for i in [1,60,120]:
        current_time = datetime.now().strftime("%y%m%d%H%M%S")
        url = f"https://www.linkedin.com/jobs/search/?currentJobId=4295947748&distance=25&f_TPR=r86400&f_WT=2&geoId=92000000&keywords=AI&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&start={i}"
        craw_result = await url_craw(url)
        jobinfo = await jobinfo_parse(craw_result)

        # 写入json文件
        # with open(f'jobs_{current_time}_start_{i}.json', 'w', encoding='utf-8') as f:
        #     json.dump(jobinfo, f, ensure_ascii=False, indent=4)  # ensure_ascii=False 支持中文
        # print(f'JSON文件已生成： jobs_{current_time}_start_{i}.json')












if __name__ == "__main__":
    asyncio.run(main())