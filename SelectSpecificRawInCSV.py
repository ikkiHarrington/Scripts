import TkEasyGUI as eg
import pandas as pd
import os

keywords_list = []
output_csv = 'output.csv'

# define layout
layout = [
    [
        eg.Text("Select keywords list(.txt)"),
        eg.Input(key="text_filename"),
        eg.FileBrowse(),  # FileBrowse button
        eg.Button("Set", key="input_text"),
    ],
    [
        eg.Text("Select search target(.csv)"),
        eg.Input(key="filename"),
        eg.FileBrowse(),  # FileBrowse button
        eg.Button("Set", key="input_csv"),
    ],
    [eg.CloseButton()]
]

def ProcessCSV(input_csv):

    #csv読み込み
    df = pd.read_csv(input_csv, header=0)

    #headerをlistで取り出し、特定の文字列のheaderがあるか検索する
    headers = df.columns.tolist()
    exist = False

    for keyword in keywords_list:
        for header in headers:
            if header == keyword:
                exist = True
        if (exist == False):
            raise ValueError("no keyword in input csv: " + keyword)
            exit()
        exist = False
    print('keywords are in header!')

    #df which Raws are match keywords
    df_usecols = pd.read_csv(input_csv, usecols=keywords_list)
    print(df_usecols)

    #書き出し。index(最初の1列目)は消す
    df_usecols.to_csv(output_csv, index=False)

def processText(input_text):
    with open(input_text) as f:
        for line in f:
            line_woCRLF = line.replace('\n', '')
            keywords_list.append(line_woCRLF)
    print(keywords_list)

if __name__ == '__main__':
    # create a window
    with eg.Window("Select Raws from CSV", layout) as window:
        # event loop
        for event, values in window.event_iter():
            if event == "input_text":
                file_path = values["text_filename"]
                processText(file_path)
            if event == "input_csv":
                file_path = values["filename"]
                ProcessCSV(file_path)