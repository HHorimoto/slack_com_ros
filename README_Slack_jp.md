## Set up Create an App Memo

`Slack api`で`Python`によるメッセージ送受信を行うセットアップの方法をまとめました。

以下の手順の**Token**と**チャンネルID**をメモしといてください。

### Download Slack

以下のリンクから，お使いの`OS`に合わせて`Slack`をダウンロードしてください。

- LINK : https://slack.com/intl/ja-jp/downloads/

### Create WorkSpace

以下のリンクから`Python`でメッセージの送受信を行う`WrokSpace`を作成してください。

- LINK : https://slack.com/get-started#/create
### Create New App

以下のリンクと手順から，新しいアプリケーションを作成してください．

- LINK : https://note.com/npaka/n/n4bcb38a1ea74

- 手順；`Create an (New) App`を選択 → `App Name`(アプリ名)と`Pick a workspace to develop your app in`(ワークスペース名)欄を入力 → `Create App`を選択

### Add Authority To Scopes

以下の手順で，権限を追加してください。

- 手順；`OAuth & Permissions`を選択 → `Scopes`に以下の権限を選択し`Add an OAuth Scope`で追加

+ chat:write
+ chat:write.customize
+ channels:history
+ channels:read
+ groups:history
+ groups:read

### Get Token

以下の手順で，`Token`を取得してください。

- 手順：`Install App`を選択 → `Install to Workspace`を選択 → `許可する`を選択 → `Token`をメモ

### Add App To Channel

以下の手順で，作成した`App`をワークスペース内のチャンネルに追加してください。

- 手順：追加したいチャンネルの投稿画面に`@{アプリ名}`で投稿 → `チャンネルに追加する`を選択

### Get Channel ID

以下の手順で，作成したワークスペース内のチャンネルの`ID`を取得してください。

- 手順：前項で追加したチャンネル名を右クリックして`チャンネル詳細を表示する`を選択 → 最下部の`チャンネルID`を取得

## References

[1] npaka, "slack API 入門 (1) - Pythonによるメッセージ送信", note, https://note.com/npaka/n/n4bcb38a1ea74 (参照 2022-08-15)
[2] 鈴木純, "Slackチャンネルにメッセージを投稿できるSlackAppを作成する", DelelopersIO, https://dev.classmethod.jp/articles/post-messages-to-slack-channel/ (参照 2022-08-15)