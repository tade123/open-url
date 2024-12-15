import time
import webbrowser
from datetime import datetime
import threading

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
    # 基準時刻を指定 (ターゲット時刻)
    target_time = datetime(2024, 1, 1, 0, 0, 0, 0)  # 年, 月, 日, 時, 分, 秒, ミリ秒

    # 開くURL
    url = "http://abehiroshi.la.coocan.jp/"

    # 別スレッドでタスクを実行
    threading.Thread(target=open_url_at, args=(target_time, url)).start()
