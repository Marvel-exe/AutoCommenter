# AutoCommenter for Instagram

## Easy to set-up and install

### Installation
First we need to download the files and install depencies

```bash
git clone https://github.com/MateeHash/AutoCommenter.git && cd AutoCommenter && pip3 install -r requirements.txt
```

### Setting up
Now we need to configurate some variables, let's edit ``config.py``

```python
USERNAME = "username"  # Your instagram account username

PASSWORD = "password"  # Your instagram account password

COMMENT = """Comment"""  # Comment to be posted

COMMENT_ON = "account_to_be_commented"  # Account to be commented
```

## Deployment

Just run:
```bash
python3 autocomment.py
```


## TODO

> * Multiple accounts to be commented