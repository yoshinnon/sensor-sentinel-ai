# 🛰️ Sensor-Sentinel-AI
### 汎用時系列データ異常検知・監視システム

## 📌 概要
本プロジェクトは、時系列センサーデータの異常を自動検知するシステムのプロトタイプです。
機械学習を用いた異常検知ロジック、Streamlitによる可視化、およびAnsibleによるDockerデプロイを網羅しています。

## ディレクトリ構造

```
sensor-sentinel-ai/          # リポジトリルート
├── README.md                # プロジェクト説明（先ほどのテンプレート）
├── LICENSE                  # ライセンスファイル (MIT等)
├── .gitignore               # Pythonやvenvの不要ファイルを弾く
│
├── app/                     # アプリケーション本体
│   ├── app.py               # Streamlitメインプログラム
│   ├── model.py             # 異常検知ロジック (Isolation Forest等)
│   ├── preprocess.py        # 前処理ロジック
│   ├── requirements.txt     # Python依存ライブラリ
│   └── data/                # (任意) サンプルCSVデータ
│
├── ansible/                 # インフラ自動化 (IaC)
│   ├── inventory.ini        # 接続先サーバー設定
│   ├── playbook.yml         # 実行用メインプレイブック
│   └── roles/
│       └── docker_sensor_app/
│           ├── tasks/
│           │   └── main.yml # コンテナ作成・起動タスク
│           └── templates/
│               └── Dockerfile.j2 # Dockerイメージの設計図
│
└── tests/                   # (任意) テストコード
    └── test_preprocess.py
```

## ✨ 特徴
- **Unsupervised Learning:** Isolation Forestによるラベルなしデータの異常検知。
- **Containerized:** Dockerによる環境のポータビリティを確保。
- **IaC:** AnsibleによるUbuntuサーバーへの自動デプロイに対応。

## 🚀 使い方
1. `ansible/inventory.ini` を編集してターゲットサーバーを指定。
2. `ansible-playbook -i ansible/inventory.ini ansible/playbook.yml` を実行。
