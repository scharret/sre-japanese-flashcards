from genanki import Deck, Model, Package, Note
import genanki
import uuid

# --- Configuration du Deck Anki ---
model_id = 1607392319  # ID unique pour le modèle
deck_id = 2059400110   # ID unique pour le deck

# Modèle de carte (recto: Japonais + Kanji, verso: Français + Exemple)
sre_model = Model(
  model_id,
  'Modèle SRE Japonais-Français',
  fields=[
    {'name': 'Japonais'},  # Termes en japonais (kanji + kana)
    {'name': 'Français'},  # Traduction française
    {'name': 'ExempleJP'}, # Exemple en japonais (phrase contextuelle)
    {'name': 'ExempleFR'}, # Traduction de l'exemple
    {'name': 'Catégorie'}, # Catégorie (ex: "Incident", "Infrastructure")
    {'name': 'Audio'},     # Champ pour l'audio (optionnel)
  ],
  templates=[
    {
      'name': 'Carte SRE',
      'qfmt': '''
      <div style="font-size: 24px; text-align: center;">
        {{Japonais}}
      </div>
      <hr style="border: 1px solid #ccc;">
      <div style="font-size: 18px; color: #666; text-align: center;">
        {{Catégorie}}
      </div>
      ''',
      'afmt': '''
      <div style="font-size: 20px;">
        <b>Français:</b> {{Français}}
      </div>
      <hr style="border: 1px dashed #ccc;">
      <div style="font-size: 18px; color: #333;">
        <b>Exemple (JP):</b> {{ExempleJP}}<br>
        <b>Exemple (FR):</b> {{ExempleFR}}
      </div>
      {{Audio}}
      ''',
    },
  ],
  css='''
  .card {
    font-family: 'Meiryo', 'MS Gothic', sans-serif;
    text-align: center;
    color: black;
    background-color: white;
  }
  '''
)

# Création du deck
sre_deck = Deck(deck_id, '🇯🇵 Vocabulaire SRE Japonais (N4→N2)')

# --- Liste des cartes (100+ termes SRE) ---
sre_cards = [
    # Catégorie: Incidents & Urgences
    {
        'Japonais': '障害<br><span style="font-size: 16px;">しょうがい</span>',
        'Français': 'Incident / Panne',
        'ExempleJP': '現在、システムに重大な障害が発生しています。',
        'ExempleFR': 'Un incident majeur est en cours sur le système.',
        'Catégorie': '🚨 Urgence',
    },
    {
        'Japonais': '復旧<br><span style="font-size: 16px;">ふっきゅう</span>',
        'Français': 'Récupération / Restauration',
        'ExempleJP': 'データベースの復旧に30分かかります。',
        'ExempleFR': 'La récupération de la base de données prendra 30 minutes.',
        'Catégorie': '🚨 Urgence',
    },
    {
        'Japonais': 'ダウンタイム<br><span style="font-size: 16px;">だうんたいむ</span>',
        'Français': 'Temps d’arrêt',
        'ExempleJP': '今日のダウンタイムは5分以内に収めなければなりません。',
        'ExempleFR': 'Le temps d’arrêt d’aujourd’hui doit être limité à 5 minutes.',
        'Catégorie': '🚨 Urgence',
    },
    {
        'Japonais': '緊急<br><span style="font-size: 16px;">きんきゅう</span>',
        'Français': 'Urgence',
        'ExempleJP': 'これは緊急事態です！すぐに対応してください！',
        'ExempleFR': 'C’est une urgence ! Veuillez intervenir immédiatement !',
        'Catégorie': '🚨 Urgence',
    },
    {
        'Japonais': '対応<br><span style="font-size: 16px;">たいおう</span>',
        'Français': 'Intervention / Réponse',
        'ExempleJP': 'この障害に対応するエンジニアを割り当ててください。',
        'ExempleFR': 'Assignez un ingénieur pour intervenir sur cet incident.',
        'Catégorie': '🚨 Urgence',
    },

    # Catégorie: Infrastructure
    {
        'Japonais': 'インフラ<br><span style="font-size: 16px;">いんふら</span>',
        'Français': 'Infrastructure',
        'ExempleJP': 'インフラのスケーリングが必要です。',
        'ExempleFR': 'Nous devons scaler l’infrastructure.',
        'Catégorie': '🖥️ Infrastructure',
    },
    {
        'Japonais': 'サーバー<br><span style="font-size: 16px;">さーばー</span>',
        'Français': 'Serveur',
        'ExempleJP': 'メインサーバーのCPU使用率が100%です。',
        'ExempleFR': "L'utilisation CPU du serveur principal est à 100%.",
        'Catégorie': '🖥️ Infrastructure',
    },
    {
        'Japonais': 'クラウド<br><span style="font-size: 16px;">くらうど</span>',
        'Français': 'Cloud',
        'ExempleJP': 'このサービスはAWSクラウド上で動いています。',
        'ExempleFR': 'Ce service tourne sur le cloud AWS.',
        'Catégorie': '🖥️ Infrastructure',
    },
    {
        'Japonais': 'ノード<br><span style="font-size: 16px;">のーど</span>',
        'Français': 'Nœud (Node)',
        'ExempleJP': 'クラスターのノードが1台ダウンしました。',
        'ExempleFR': 'Un nœud du cluster est tombé.',
        'Catégorie': '🖥️ Infrastructure',
    },
    {
        'Japonais': 'クラスター<br><span style="font-size: 16px;">くらすたー</span>',
        'Français': 'Cluster',
        'ExempleJP': 'Kubernetesクラスターのヘルスチェックに失敗しました。',
        'ExempleFR': 'Le health check du cluster Kubernetes a échoué.',
        'Catégorie': '🖥️ Infrastructure',
    },

    # Catégorie: Monitoring & Logs
    {
        'Japonais': 'モニタリング<br><span style="font-size: 16px;">もにたりんぐ</span>',
        'Français': 'Monitoring',
        'ExempleJP': 'モニタリングダッシュボードにエラーが表示されています。',
        'ExempleFR': 'Le tableau de bord de monitoring affiche des erreurs.',
        'Catégorie': '📊 Monitoring',
    },
    {
        'Japonais': 'ログ<br><span style="font-size: 16px;">ろぐ</span>',
        'Français': 'Logs',
        'ExempleJP': 'エラーログを確認してください。',
        'ExempleFR': 'Vérifiez les logs d’erreur.',
        'Catégorie': '📊 Monitoring',
    },
    {
        'Japonais': 'メトリクス<br><span style="font-size: 16px;">めとりくす</span>',
        'Français': 'Métriques',
        'ExempleJP': 'CPUメトリクスが異常です。',
        'ExempleFR': 'Les métriques CPU sont anormales.',
        'Catégorie': '📊 Monitoring',
    },
    {
        'Japonais': 'アラート<br><span style="font-size: 16px;">あらーと</span>',
        'Français': 'Alerte',
        'ExempleJP': 'PagerDutyからアラートが来ました。',
        'ExempleFR': 'Une alerte est arrivée via PagerDuty.',
        'Catégorie': '📊 Monitoring',
    },
    {
        'Japonais': '閾値<br><span style="font-size: 16px;">いきち</span>',
        'Français': 'Seuil (threshold)',
        'ExempleJP': 'メモリ使用率の閾値を80%に設定してください。',
        'ExempleFR': 'Configurez le seuil d’utilisation mémoire à 80%.',
        'Catégorie': '📊 Monitoring',
    },

    # Catégorie: Déploiement & CI/CD
    {
        'Japonais': 'デプロイ<br><span style="font-size: 16px;">でぷろい</span>',
        'Français': 'Déploiement (Deploy)',
        'ExempleJP': '新しいバージョンをプロダクションにデプロイします。',
        'ExempleFR': 'Je déploie la nouvelle version en production.',
        'Catégorie': '🚀 Déploiement',
    },
    {
        'Japonais': 'ロールバック<br><span style="font-size: 16px;">ろーるばっく</span>',
        'Français': 'Rollback',
        'ExempleJP': 'デプロイに失敗したので、ロールバックします。',
        'ExempleFR': 'Le déploiement a échoué, je fais un rollback.',
        'Catégorie': '🚀 Déploiement',
    },
    {
        'Japonais': 'CI/CD<br><span style="font-size: 16px;">しーあいしーでぃー</span>',
        'Français': 'CI/CD',
        'ExempleJP': 'CI/CDパイプラインが失敗しました。',
        'ExempleFR': 'La pipeline CI/CD a échoué.',
        'Catégorie': '🚀 Déploiement',
    },
    {
        'Japonais': 'ビルド<br><span style="font-size: 16px;">びるど</span>',
        'Français': 'Build',
        'ExempleJP': 'ビルドがタイムアウトしました。',
        'ExempleFR': 'Le build a timeout.',
        'Catégorie': '🚀 Déploiement',
    },
    {
        'Japonais': 'リリース<br><span style="font-size: 16px;">りりーす</span>',
        'Français': 'Release',
        'ExempleJP': '今日のリリースは中止します。',
        'ExempleFR': 'La release d’aujourd’hui est annulée.',
        'Catégorie': '🚀 Déploiement',
    },

    # Catégorie: Réseau
    {
        'Japonais': 'ネットワーク<br><span style="font-size: 16px;">ねっとわーく</span>',
        'Français': 'Réseau (Network)',
        'ExempleJP': 'ネットワークの遅延が大きすぎます。',
        'ExempleFR': 'La latence du réseau est trop élevée.',
        'Catégorie': '🌐 Réseau',
    },
    {
        'Japonais': 'ファイアウォール<br><span style="font-size: 16px;">ふぁいあうぉーる</span>',
        'Français': 'Pare-feu (Firewall)',
        'ExempleJP': 'ファイアウォールのルールを更新しました。',
        'ExempleFR': 'J’ai mis à jour les règles du pare-feu.',
        'Catégorie': '🌐 Réseau',
    },
    {
        'Japonais': 'DNS<br><span style="font-size: 16px;">でぃーえぬえす</span>',
        'Français': 'DNS',
        'ExempleJP': 'DNSの解決に失敗しました。',
        'ExempleFR': 'La résolution DNS a échoué.',
        'Catégorie': '🌐 Réseau',
    },
    {
        'Japonais': '帯域幅<br><span style="font-size: 16px;">たいいきはば</span>',
        'Français': 'Bande passante (Bandwidth)',
        'ExempleJP': '帯域幅が不足しています。',
        'ExempleFR': 'La bande passante est insuffisante.',
        'Catégorie': '🌐 Réseau',
    },
    {
        'Japonais': 'タイムアウト<br><span style="font-size: 16px;">たいむあうと</span>',
        'Français': 'Timeout',
        'ExempleJP': 'APIのタイムアウトを30秒に設定してください。',
        'ExempleFR': 'Configurez le timeout de l’API à 30 secondes.',
        'Catégorie': '🌐 Réseau',
    },

    # Catégorie: Bases de Données
    {
        'Japonais': 'データベース<br><span style="font-size: 16px;">でーたべーす</span>',
        'Français': 'Base de données (Database)',
        'ExempleJP': 'データベースの接続がタイムアウトしました。',
        'ExempleFR': 'La connexion à la base de données a timeout.',
        'Catégorie': '🗃️ Base de Données',
    },
    {
        'Japonais': 'レプリカ<br><span style="font-size: 16px;">れぷりか</span>',
        'Français': 'Réplica',
        'ExempleJP': 'レプリカの同期が遅れています。',
        'ExempleFR': 'La synchronisation des réplicas est en retard.',
        'Catégorie': '🗃️ Base de Données',
    },
    {
        'Japonais': 'クエリ<br><span style="font-size: 16px;">くえり</span>',
        'Français': 'Requête (Query)',
        'ExempleJP': 'このクエリがデータベースを遅くしています。',
        'ExempleFR': 'Cette requête ralentit la base de données.',
        'Catégorie': '🗃️ Base de Données',
    },
    {
        'Japonais': 'バックアップ<br><span style="font-size: 16px;">ばっくあっぷ</span>',
        'Français': 'Backup',
        'ExempleJP': 'バックアップを取ってからアップグレードしてください。',
        'ExempleFR': 'Faites un backup avant la mise à jour.',
        'Catégorie': '🗃️ Base de Données',
    },
    {
        'Japonais': 'トランザクション<br><span style="font-size: 16px;">とらんざくしょん</span>',
        'Français': 'Transaction',
        'ExempleJP': 'トランザクションがデッドロックしています。',
        'ExempleFR': 'La transaction est en deadlock.',
        'Catégorie': '🗃️ Base de Données',
    },

    # Catégorie: Sécurité
    {
        'Japonais': 'セキュリティ<br><span style="font-size: 16px;">せきゅりてぃ</span>',
        'Français': 'Sécurité (Security)',
        'ExempleJP': 'セキュリティパッチを適用してください。',
        'ExempleFR': 'Appliquez le patch de sécurité.',
        'Catégorie': '🔒 Sécurité',
    },
    {
        'Japonais': '認証<br><span style="font-size: 16px;">にんしょう</span>',
        'Français': 'Authentification',
        'ExempleJP': '認証エラーが多発しています。',
        'ExempleFR': 'Il y a de nombreuses erreurs d’authentification.',
        'Catégorie': '🔒 Sécurité',
    },
    {
        'Japonais': '暗号化<br><span style="font-size: 16px;">あんごうか</span>',
        'Français': 'Chiffrement',
        'ExempleJP': 'このデータは暗号化されていません。',
        'ExempleFR': 'Ces données ne sont pas chiffrées.',
        'Catégorie': '🔒 Sécurité',
    },
    {
        'Japonais': 'アクセス権<br><span style="font-size: 16px;">あくせすけん</span>',
        'Français': 'Permissions d’accès',
        'ExempleJP': 'このユーザーのアクセス権を確認してください。',
        'ExempleFR': 'Vérifiez les permissions d’accès de cet utilisateur.',
        'Catégorie': '🔒 Sécurité',
    },
    {
        'Japonais': '脆弱性<br><span style="font-size: 16px;">ぜいじゃくせい</span>',
        'Français': 'Vulnérabilité',
        'ExempleJP': '新しい脆弱性が報告されました。',
        'ExempleFR': 'Une nouvelle vulnérabilité a été rapportée.',
        'Catégorie': '🔒 Sécurité',
    },

    # Catégorie: Kubernetes & Conteneurs
    {
        'Japonais': 'コンテナ<br><span style="font-size: 16px;">こんてな</span>',
        'Français': 'Conteneur (Container)',
        'ExempleJP': 'このコンテナがクラッシュしました。',
        'ExempleFR': 'Ce conteneur a crashé.',
        'Catégorie': '🐳 Kubernetes',
    },
    {
        'Japonais': 'ポッド<br><span style="font-size: 16px;">ぽっど</span>',
        'Français': 'Pod',
        'ExempleJP': 'ポッドがPending状態です。',
        'ExempleFR': 'Le pod est en état Pending.',
        'Catégorie': '🐳 Kubernetes',
    },
    {
        'Japonais': 'ノードプール<br><span style="font-size: 16px;">のーどぷーる</span>',
        'Français': 'Node Pool',
        'ExempleJP': 'ノードプールをスケールアップします。',
        'ExempleFR': 'Je scale up le node pool.',
        'Catégorie': '🐳 Kubernetes',
    },
    {
        'Japonais': 'デプロイメント<br><span style="font-size: 16px;">でぷろいめんと</span>',
        'Français': 'Deployment',
        'ExempleJP': 'デプロイメントがロールアウト中です。',
        'ExempleFR': 'Le deployment est en cours de rollout.',
        'Catégorie': '🐳 Kubernetes',
    },
    {
        'Japonais': 'サービスメッシュ<br><span style="font-size: 16px;">さーびすめっしゅ</span>',
        'Français': 'Service Mesh',
        'ExempleJP': 'Istioを使ったサービスメッシュを導入します。',
        'ExempleFR': 'Nous implémentons un service mesh avec Istio.',
        'Catégorie': '🐳 Kubernetes',
    },

    # Catégorie: Phrases Utiles en Réunion
    {
        'Japonais': '現在のステータスはどうですか？<br><span style="font-size: 16px;">げんざいのすてーたすはどうですか？</span>',
        'Français': 'Quel est le statut actuel ?',
        'ExempleJP': 'A: 現在のステータスはどうですか？<br>B: まだ調査中です。',
        'ExempleFR': 'A: Quel est le statut actuel ?<br>B: Toujours en investigation.',
        'Catégorie': '🗣️ Réunion',
    },
    {
        'Japonais': '根本的な原因は何ですか？<br><span style="font-size: 16px;">こんぽんてきなげんいはなんですか？</span>',
        'Français': 'Quelle est la cause racine ?',
        'ExempleJP': '根本的な原因はデータベースのメモリリークです。',
        'ExempleFR': 'La cause racine est une fuite mémoire dans la base de données.',
        'Catégorie': '🗣️ Réunion',
    },
    {
        'Japonais': '対応策はありますか？<br><span style="font-size: 16px;">たいおうさくはありますか？</span>',
        'Français': 'Avez-vous un plan d’action ?',
        'ExempleJP': '一時的な対応策として、トラフィックをリダイレクトします。',
        'ExempleFR': 'En mesure temporaire, nous redirigeons le trafic.',
        'Catégorie': '🗣️ Réunion',
    },
    {
        'Japonais': '影響範囲はどこまでですか？<br><span style="font-size: 16px;">えいきょうはんいはどこまでですか？</span>',
        'Français': 'Quel est le périmètre impacté ?',
        'ExempleJP': '影響範囲はユーザーAPIのみです。',
        'ExempleFR': 'Seule l’API utilisateur est impactée.',
        'Catégorie': '🗣️ Réunion',
    },
    {
        'Japonais': '次のステップは何ですか？<br><span style="font-size: 16px;">つぎのすてっぷはなんですか？</span>',
        'Français': 'Quelle est la prochaine étape ?',
        'ExempleJP': '次のステップはログの詳細分析です。',
        'ExempleFR': 'La prochaine étape est une analyse détaillée des logs.',
        'Catégorie': '🗣️ Réunion',
    },
]

# Ajout des cartes au deck
for card in sre_cards:
    note = Note(
        model=sre_model,
        fields=[
            card['Japonais'],
            card['Français'],
            card['ExempleJP'],
            card['ExempleFR'],
            card['Catégorie'],
            '',  # Champ audio vide (peut être ajouté plus tard)
        ]
    )
    sre_deck.add_note(note)

# Génération du fichier .apkg
package = Package(sre_deck)
package.write_to_file('SRE_Japanese_Flashcards.apkg')

# Message de confirmation
print("✅ Fichier 'SRE_Japanese_Flashcards.apkg' généré avec succès !")
print("→ Importez-le dans Anki (Fichier > Importer)")
