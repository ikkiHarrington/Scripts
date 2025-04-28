import TkEasyGUI as eg
import pandas as pd
import os

output_csv = 'output.csv'

# define layout
layout = [
    [
        eg.Input(key="filename"),
        eg.FileBrowse(),  # FileBrowse button
        eg.Button("Set", key="input_csv"),
    ],
    [eg.CloseButton()]
]

def ProcessCSV(input_csv):
    keywords = ['var1', 'var3']

    #csv読み込み
    df = pd.read_csv(input_csv, header=0)

    #headerをlistで取り出し、特定の文字列のheaderがあるか検索する
    headers = df.columns.tolist()
    exist = False

    for keyword in keywords:
        for header in headers:
            if header == keyword:
                exist = True
        if (exist == False):
            raise ValueError("no keyword in input csv")
            exit()
        exist = False
    print('keywords are in header!')

    #df which Raws are match keywords
    df_usecols = pd.read_csv(input_csv, usecols=keywords)
    print(df_usecols)

    #書き出し。index(最初の1列目)は消す
    df_usecols.to_csv(output_csv, index=False)



if __name__ == '__main__':
    # create a window
    with eg.Window("Select Raws from CSV", layout) as window:
        # event loop
        for event, values in window.event_iter():
            if event == "input_csv":
                file_path = values["filename"]
                ProcessCSV(file_path)