# 概要
サポーターズvol10ハッカソンのとーむ「Pyてょn」のリポジトリ。

## 構築手順
#### ①こちらのリポジトリをクローンする。

<small>※クローンとは　ネット上のリポジトリの内容を自身のローカルPC内にコピーして持ってくること</small>

#### ②ローカルにもってこれたらrequirements.txt内のライブラリをインストールする

```
pip install -r requirements.txt
```

#### ③データベースのマイグレート
```
#マイグレーションファイルを作成。modelsに変更がなければNo changes detectedとなるかも

python manage.py makemigrations
```

```
#マイグレーションファイルをデータベースに適用

python manage.py migrate
```

#### ④以下のコマンドでサーバーを動かす
```
python manage.py runserver
```
以下の画面になればひとまず大丈夫
![img.png](img.png)