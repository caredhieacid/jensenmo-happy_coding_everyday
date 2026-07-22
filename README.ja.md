<div align="center">

# ⚡ HappyCoding Everyday

### リスクに合わせて厳密さを自動調整する Codex コーディングワークフロー。

目的を一度伝えるだけで、HappyCoding が小さな修正、限定的な協調、高リスクなデリバリーから最も軽く安全な経路を選びます。

**🌐 Language / 语言 / 言語 / 언어 / Idioma**

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

[![Status: Alpha](https://img.shields.io/badge/status-alpha-f59e0b)](#プロジェクトの状態)
[![CI](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml/badge.svg)](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml)
[![Codex Skill](https://img.shields.io/badge/Codex-agent%20skill-111827)](skills/jensenmo-happy-coding-everyday/SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e.svg)](LICENSE)

[クイックスタート](#クイックスタート) · [実行レーン](#3-つの実行レーン) · [設計原則](#設計原則) · [ドキュメント](docs/README.md)

</div>

> 英語版の [README.md](README.md) が正本です。この日本語版はドラフトで、ネイティブレビューを募集中です。内容が異なる場合は英語版を優先してください。

## HappyCoding とは

HappyCoding Everyday は Codex のための単一かつ自動的なコーディングワークフロー入口です。通常の依頼を小さな契約に変換し、必要十分な実行レーンを選び、作業を行い、最終変更後の新しい証拠で完了します。利用者がモード、テスト、エージェント構成を毎回指定する必要はありません。

## クイックスタート

```bash
codex plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday
```

Codex の **Plugins** を開き、**JensenMo HappyCoding** から **HappyCoding Everyday** をインストールします。新しいタスクで通常どおり依頼してください。

```text
ログイン回帰を修正し、無関係な未コミット変更を保持し、最後に新しい検証結果を示してください。
```

明示的に呼び出すこともできます。

```text
$jensenmo-happy-coding-everyday コードを変更する前に、この API 契約を監査してください。
```

## 3 つの実行レーン

| レーン | 使用条件 | 既定の動作 |
| --- | --- | --- |
| **Everyday** | 1 つの限定された成果、低い結合、1 つの受け入れ経路 | 調査、最小変更、焦点を絞った検証 |
| **Collaboration** | 独立して分割できる作業、または広い読み取り範囲 | 読み取りを並列化し、共有書き込みは 1 系統に保つ |
| **Delivery** | セキュリティ、移行、本番、長期調整、段階的な実環境検証 | 永続的な契約、段階ゲート、独立レビュー、ロールバック |

PR、複数ファイル、フロントエンドとバックエンドという単語だけでは Delivery に昇格しません。リスク、独立性、所有権、受け入れコストで判断します。

## 設計原則

- **意図は一度だけ**：ワークフロー選択を利用者に戻しません。
- **必要十分な厳密さ**：Everyday から始め、証拠がある場合だけ昇格します。
- **儀式より証拠**：コマンドの成功ではなく、要求された挙動を証明します。
- **読み取りは並列、書き込みは制御**：コンテキストを守り、競合を避けます。
- **新しい検証**：最終変更後に関連する検証を再実行します。
- **読み取り専用を尊重**：監査、説明、診断は変更権限ではありません。

詳細は [設計思想](docs/design-philosophy.md) と [アーキテクチャ](docs/architecture.md) を参照してください。

## Skill を直接インストールする

```bash
git clone https://github.com/caredhieacid/jensenmo-happy_coding_everyday.git
cd jensenmo-happy_coding_everyday
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/jensenmo-happy-coding-everyday" \
  "$HOME/.agents/skills/jensenmo-happy-coding-everyday"
```

既存の宛先は削除せず、先に内容を確認してください。`$HOME/.agents/skills` は現在の Codex ユーザースコープの場所です。

## 検証とリリース

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_repository.py
```

各 PR は決定的な plugin プレビューを作成します。plugin のバージョンと一致する `v*` タグは、ZIP と SHA-256 チェックサムを含む GitHub Release を自動作成します。行動シナリオの JSON が存在するだけでは合格ではなく、新しいエージェントコンテキストで観察可能な不変条件を確認する必要があります。

## プロジェクトの状態

現在は **Alpha** です。ルーティングモデル、plugin パッケージ、構造検証、初期の圧力シナリオは利用できますが、閾値は実際のコーディングタスクを通じて継続的に調整されます。

[ドキュメント](docs/README.md) · [コントリビューション](CONTRIBUTING.md) · [セキュリティ](SECURITY.md) · [サポート](SUPPORT.md) · [行動規範](CODE_OF_CONDUCT.md)

## ライセンス

[MIT](LICENSE) © 2026 Jensen Mo
