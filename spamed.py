# internal imports
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# external imports
import requests


"""
Change 4 Fields (Compulspory) | 3 Fields are optional | Sample Video on where and how to find them is available in Readme.

URL: your form url # URL must be response URL, sample is provided
REFERER: Take by Filling a response
COOKIE: Take by filling a response
DATA: Fill a form and find it :)

PROXYS: You can provide proxies also.
MAX_WORKERS: Change this value to increase the speed of spam. Don't go beyond 500.
SPAM_COUNT: Change this to increase spam count
"""

MAX_WORKERS = 63 # Change this value to increase the speed of spam. Don't go beyond 500.
SPAM_COUNT = 100000 # Change this to increase spam count

URL = 'https://www.gstatic.com/_/freebird/_/ss/k=freebird.v.1U0mdraGdog.L.W.O/d=1/rs=AMjVe6jMHY779P5Du_fvzxuTKRbFzC-Nig

DATA = 'entry.1430483420=jungkook&dlut=1660944181553&entry.1430483420_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%224005593576072491623%22%5D&pageHistory=0&fbzx=1170865266493271732

REFERER = 'https://docs.google.com/forms/d/e/1FAIpQLSeaAsVg30Lda_-r85pu6mXNRRQCzERmogWrX0Ar7rwKXeto3A/viewform?fbzx=1170865266493271732

COOKIE = S=spreadsheet_forms=jlcZTa4zVLdq_R5929GaAYw2iLxtRyxwgEh4BMmOcio; COMPASS=spreadsheet_forms=CjIACWuJVwFcLekYPMbIbjc61n79pztBv9VAWxR5x-OizzIkU4Qt3osd9c_ddEGOeQdbnRDBmoCYBho0AAlriVeiDDdGUgDYgy5OHyN02TqQby0vzr1k1GM9LEF5hZe96skP6ot5Wy2MwwTk7GZ4Ew==; SID=NgjgQIiL7BZkfJuVw0xPr5-pyrDUUUsQu-QNyKvBN-k6_ajrMzk4q6WkQiYQQgX2xu_p0w.; __Secure-1PSID=NgjgQIiL7BZkfJuVw0xPr5-pyrDUUUsQu-QNyKvBN-k6_ajrkEckYR08HGOGWOfpLgT1wQ.; __Secure-3PSID=NgjgQIiL7BZkfJuVw0xPr5-pyrDUUUsQu-QNyKvBN-k6_ajroqdp1uf5kbxpFKlfW3KAVw.; HSID=A78VCQ2SGr1cSyzu1; SSID=ASBonfugEvWNIxhDf; APISID=IcHgB-Ibqn56Q0-e/AHZC9dDNnvzqzmu3z; SAPISID=uY9sI64SGYxKp2Rv/A8V45Qz3Rp6HFn5VX; __Secure-1PAPISID=uY9sI64SGYxKp2Rv/A8V45Qz3Rp6HFn5VX; __Secure-3PAPISID=uY9sI64SGYxKp2Rv/A8V45Qz3Rp6HFn5VX; SEARCH_SAMESITE=CgQIl5YB; AEC=AakniGOGyOzDeCZsAZipSUP_ZjBgloKToSMbp-4vsMWziogWvdU9-ZpieQ; 1P_JAR=2022-8-19-21; NID=511=cw0qTAyfNLk5GTe0LtrWI9mdpeflK1QR8u80oNuG34fzKFsad-dywyqJlWwCWK_GVBSpIgMQ_jIuBp-L5RmWZjC1MUfibZoWghyheouTtzSanBaMGrwHU3XDfb6RQvQ6OMd_FT3n1rwq729l8_fsjbe9zhu-ybFahMsBPsF4wH2bNwtAXoaI5zNNtx-GT7kCo3vmGwO8B3lu-n5-XNbHmzpOUpSZktSZdRy1bqUN3rSuHNB9MK6NSkl8Hg; GOOGLE_ABUSE_EXEMPTION=ID=f50f06b80dd79834:TM=1660944733:C=r:IP=189.219.62.58-:S=WoFk9KcnY6KgZGi1_-01R6Y; SIDCC=AEf-XMR-P-UWn07o5M2tHkeJLXB2BW5yN7b6B9Ad149Zv4BSvrV5ZAKlgh7c1KvgYkPYiZEyh9Y; __Secure-1PSIDCC=AEf-XMSXKyizr-d4tk_9Kcc1Vnc7QbjnSHw_YOHMqPgpAo65DZyDOvUXeWKj77zRG4pty-Xj2Q; __Secure-3PSIDCC=AEf-XMQGGOwLm6JvIGp-Ak2vXGcFVxy_jhbwVJhmhwElIKEF44Qe3nQIK-aZ0wPuSVdNTGX6nQ


HEADER = {
    'Host': 'docs.google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://docs.google.com',
    'Referer': REFERER,
    'Cookie': COOKIE,
    'Upgrade-Insecure-Requests':'1'
    }

# After 4.8K+ requests google will ask you to fill a captcha if you are not using proxy.
PROXYS = []
# PROXYS = ['144.217.101.242:3129', '192.41.71.204:3128', '192.41.13.71:3128', '104.154.143.77:3128']




def trouble():
    try:
        if len(PROXYS) > 0: # Proxies are passed
            proxy = PROXYS[random.choice([x for x in range(len(PROXYS))])]
            r = requests.post(URL, proxies={'http':proxy, 'https':proxy}, data=DATA, headers=HEADER)
        else:
            r = requests.post(URL, data=DATA, headers=HEADER)
        return r
    except Exception as e:
        raise Exception (e)


if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_calls = {executor.submit(trouble): count for count in range(SPAM_COUNT)}

        for future in as_completed(future_calls):
            try:
                result = future.result()
                print('[-] {}'.format(result.status_code))
            except Exception as e:
                print('[!] {}'.format(e))
