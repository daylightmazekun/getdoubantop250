#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import logging
import xlwt
from bs4 import BeautifulSoup
from pip._vendor import requests

logging.basicConfig(level=logging.INFO,
                    filename='./log/log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


# 获取可播放电影的link
def _get_movie_link(movie_link):
    content_link = requests.get(movie_link)
    soup_link = BeautifulSoup(content_link.content, "lxml")
    find_link = soup_link.find_all('a', attrs={'class': 'playBtn'})
    # workbook = xlwt.Workbook(encoding='utf-8')
    # worksheet = workbook.add_sheet('doubantop250', cell_overwrite_ok=True)
    for play_link_list in find_link:
        do_it = play_link_list.get('href').strip()
        see_it = play_link_list.text.strip()
        logging.info(see_it + do_it)
        # workbook, i = _save_excle(see_it, do_it, i, workbook, worksheet)
        # i = i + 1
    # workbook.save('DOUBANTOP250.xls')


# def _save_excle(movie_name, movie_link, i, workbook, worksheet):
#     worksheet.write(i, 0, movie_name)
#     for link in movie_link:
#         worksheet.write(i, 1, link)
#         i = i + 1
#     return workbook, i


def _get_douban_top(url):
    MOVIE_URL = 'http://movie.douban.com/top250/'
    content = requests.get(url)
    soup = BeautifulSoup(content.content, "lxml")
    movie_list = soup.find_all('div', attrs={'class': 'info'})
    for list in movie_list:
        movie_name = list.find('span', attrs={'class': 'title'}).text
        movie_link = list.find('span', attrs={'class': 'playable'})
        logging.info(movie_name)
        if movie_link:
            _get_movie_link(list.find('a').get('href'))
    next_page = soup.find('span', attrs={'class', 'next'})
    try:
        last_url = next_page.find('a').get('href')
    except Exception as e:
        return
    if last_url:
        _get_douban_top(MOVIE_URL + last_url)


if __name__ == '__main__':
    MOVIE_URL = 'http://movie.douban.com/top250/'
    _get_douban_top(MOVIE_URL)
