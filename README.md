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

## 🔍 具体的な使用場面

### 1. 製造ライン — 設備の予兆保全

工作機械や搬送装置に取り付けた振動センサー・温度センサーのログをCSVで取り出し、アップロードします。通常稼働時とは異なるパターン（回転数の微妙なブレ、軸受け温度の緩やかな上昇など）を「異常」として検出することで、突発的な設備停止が起きる前にメンテナンスのタイミングを把握できます。

**想定データ例:** `timestamp, vibration_x, vibration_y, temperature`

---

### 2. 社内インフラ — サーバー・ネットワーク監視

CPU使用率、メモリ使用量、ネットワークトラフィックといったサーバーメトリクスを定期的にCSVへエクスポートし、取り込みます。通常のアクセスパターンから逸脱したスパイクや、深夜帯の不審なトラフィック増加を可視化・検出するのに活用できます。

**想定データ例:** `timestamp, cpu_usage_pct, mem_usage_pct, net_bytes_in`

---

### 3. 環境モニタリング — 農業・倉庫・研究施設

温室や冷蔵倉庫に設置した温湿度センサーのデータを読み込み、設定範囲を逸脱した異常値を検知します。人が常駐しない施設でも、記録データをあとから一括チェックして異常発生の時間帯を特定できます。

**想定データ例:** `timestamp, temperature_c, humidity_pct, co2_ppm`

---

### 4. IoT機器 — スマートホーム・ビル管理

電力メーターや照明・空調のセンサーデータを時系列で蓄積したログを取り込み、消費電力の急激な変動や、人がいない時間帯の不審なアクティビティを検出します。設備の使われ方のベースラインを自動学習するため、ルールベースでは設定しにくい「なんとなくおかしい」パターンにも対応できます。

**想定データ例:** `timestamp, power_w, room_temp_c, occupancy`

---

### 共通の操作手順

1. 上記のようなCSVファイルを用意する（または組み込みのデモデータで動作確認）。
2. ブラウザで `http://<Server-IP>:8501` を開く。
3. 画面左のサイドバーで **異常値の想定割合** を調整する（全データのうち何%が異常かの目安。0.05 = 5%が初期値）。
4. 「CSVアップロード」から対象ファイルを選択する。
5. グラフと表で検出結果を確認する。異常と判定された行が `is_anomaly: 異常` として表示される。

> **ヒント:** 異常割合のスライダーは、検出の厳しさを調整する主なパラメータです。誤検知が多い場合は値を下げ、見逃しが多い場合は値を上げてみてください。

---

## 🚀 使い方
1. `ansible/inventory.ini` を編集してターゲットサーバーを指定。
2. `ansible-playbook -i ansible/inventory.ini ansible/playbook.yml` を実行。

## 🛠️ 運用・管理コマンド (Operations)

デプロイ完了後、サーバー上でコンテナの状態を確認・操作するための主要コマンドです。

### 1. コンテナの稼働状態を確認
```bash
# 起動中のコンテナ一覧を表示
docker ps

# リソース使用状況（CPU/メモリ）をリアルタイム確認
docker stats sensor-app-container
```

### 2. アプリケーションログの確認

```bash
# 最新のログを表示
docker logs sensor-app-container

# ログをリアルタイムで監視 (Ctrl+Cで終了)
docker logs -f sensor-app-container
```

### 3. コンテナ内部でのデバッグ

```bash
# コンテナ内のシェルにログイン
docker exec -it sensor-app-container /bin/bash
```

### 4. コンテナの停止・削除

```bash
# アプリの停止
docker stop sensor-app-container

# コンテナの削除
docker rm sensor-app-container
```

## 💡 トラブルシューティング

ブラウザから http://<Server-IP>:8501 にアクセスできない場合は、サーバーのファイアウォール設定を確認してください。

```bash
sudo ufw allow 8501/tcp
```
