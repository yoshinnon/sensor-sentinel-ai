# 🛰️ Sensor-Sentinel-AI
### 汎用時系列データ異常検知・監視システム

## 📌 概要
本プロジェクトは、時系列センサーデータの異常を自動検知するシステムのプロトタイプです。
機械学習を用いた異常検知ロジック、Streamlitによる可視化、およびAnsibleによるDockerデプロイを網羅しています。

## ✨ 特徴
- **Unsupervised Learning:** Isolation Forestによるラベルなしデータの異常検知。
- **Containerized:** Dockerによる環境のポータビリティを確保。
- **IaC:** AnsibleによるUbuntuサーバーへの自動デプロイに対応。

## 🚀 使い方
1. `ansible/inventory.ini` を編集してターゲットサーバーを指定。
2. `ansible-playbook -i ansible/inventory.ini ansible/playbook.yml` を実行。
