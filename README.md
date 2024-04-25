# chicsight
学部2年の授業にて作成した、FastAPIと機械学習モデルを使用して画像の推論と眼鏡の推奨を行うアプリケーションである。

## 概要
- 画像のアップロードと推論：ユーザーがアップロードした画像を用いて、事前に学習済みの分類モデルを使用して推論を行います。
- 眼鏡の推奨：ユーザーが回答したクイズに基づいて、適切な眼鏡の型を推奨します。

## 必要なライブラリ
- fastapi
- uvicorn
- torch
- torchvision

## 使用方法
1. プロジェクトをクローンする
   - `git clone https://github.com/HwaI12/chicsight.git`
2. 必要なライブラリをインストール
   - `pip install fastapi uvicorn`
   - `pip install python-multipart`
3. main.pyを実行
   - `uvicorn main:app --reload`
4. [http://127.0.0.1:8000/](http://127.0.0.1:8000/)にアクセスする