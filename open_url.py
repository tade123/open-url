import time
import webbrowser
from datetime import datetime
import threading
import argparse

def open_url_at(target_time, url):
    """
    指定した時刻にURLを開く。
    :param target_time: 実行する時刻 (datetimeオブジェクト)
    :param url: 開きたいURL
    """
    now = datetime.now()
    delay = (target_time - now).total_seconds()

    if delay > 0:
        print(f"URLを {target_time} に開きます。待機時間: {delay:.3f} 秒")
        time.sleep(delay)  # 指定時間まで待機
        print(f"Opening URL: {url} at {datetime.now()}")
        webbrowser.open(url)
    else:
        print("指定された時刻は過去です。")

if __name__ == "__main__":
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="指定した時刻にURLを開くプログラム")
    parser.add_argument("url", type=str, help="開きたいURL")
    parser.add_argument(
        "time", type=str, help="実行時刻（フォーマット: YYYY-MM-DD HH:MM:SS.mmm）"
    )
    args = parser.parse_args()

    # 入力された時刻を解析
    try:
        target_time = datetime.strptime(args.time, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        print("時刻の形式が正しくありません。フォーマット: YYYY-MM-DD HH:MM:SS.mmm")
        exit(1)

    # 別スレッドでタスクを実行
    threading.Thread(target=open_url_at, args=(target_time, args.url)).start()
