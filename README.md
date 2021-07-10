# lastpass-python

### lastpassのダッシュボード画面　-> account setting -> General -> show advanced settings -> Password Iterations -> 100100に変更

### lastpassのダッシュボード画面　-> account setting -> Multifactor Authentication -> Google Authenticatorをenabledに設定

```bash
$ git clone https://github.com/shige-ywyw/lastpass-python.git
$ cd lastpass-python
$ pip install -r requirements.txt
$ cp credentials.json.example credentials.json 
$ vi credentials.json
```

```json
{
    "username": "maildress",
    "password": "password"
}
```

```bash
$ python main.py
```