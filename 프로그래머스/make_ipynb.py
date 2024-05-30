import os
import sys
import requests
import bs4
import json

PATH = "./Python"
URL = "https://school.programmers.co.kr/learn/courses/30/lessons/"

def main(index:str):
    response = requests.get(URL+index)
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    _, _class, title = list(soup.find("ol", class_="breadcrumb").children)    #breadcrumb로 문제 분류와 제목을 표현하고 있어서 따옴
    _class = _class.text.replace(":", "").replace("/", "_")   #여기는 일단 문제가 추가되며 예외상황이 더 붙을 수 있음
    title = title.text.replace("/", "_")

    folder_path = os.path.join(PATH, _class)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, f"{index}_{title}.ipynb")
    if os.path.exists(file_path):
        raise RuntimeError("파일이 있는데?")

    with open(file_path, 'w', encoding="UTF-8") as f:
        json.dump({
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [str(content) for content in soup.find("div", class_="markdown solarized-dark").contents]
                }
            ],
            "metadata": {
                "language_info": {
                    "name": "python"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 2
        }, f, ensure_ascii=False)

if __name__ == "__main__":

    try:
        number = sys.argv[1]
        int(number)
        main(number)
    except:
        raise RuntimeError(f"argument 입력 잘 한거 맞음? {number}")