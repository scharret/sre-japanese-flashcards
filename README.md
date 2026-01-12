# 🇯🇵 SRE Japanese Vocabulary (N4→N2) / Vocabulaire SRE Japonais (N4→N2)
[![English](https://img.shields.io/badge/lang-English-blue)](https://github.com/your-repo/sre-japanese-flashcards)
[![Français](https://img.shields.io/badge/lang-Français-red)](https://github.com/your-repo/sre-japanese-flashcards)

> **Switch language / Changer de langue** :
> Scroll down for **French** or keep reading for **English**.

---

# 🇬🇧 English Version WIP

An **Anki deck** designed for **Site Reliability Engineers (SRE)** and DevOps engineers to master **technical Japanese vocabulary** (JLPT N4→N2 level) related to:
- **Incidents & Emergencies** (障害, 復旧, ダウンタイム...)
- **Infrastructure** (インフラ, サーバー, クラウド...)
- **Monitoring** (モニタリング, ログ, メトリクス...)
- **CI/CD & Deployments** (デプロイ, ロールバック, パイプライン...)
- **Networking & Databases** (ネットワーク, データベース, トランザクション...)
- **Kubernetes & Containers** (ポッド, ノードプール, サービスメッシュ...)
- **Security** (セキュリティ, 認証, 暗号化...)
- **Useful Meeting Phrases** (現在のステータスは？, 根本的な原因は？...)

---

## 📦 Deck Contents
- **100+ flashcards** organized by thematic categories
- **Optimized format**:
  - **Front**: Japanese term (Kanji + Kana) + Category
  - **Back**: English/French translation + contextual examples (JP/EN/FR)
- **Clean design** with HTML/CSS styling for readability
- **Level**: Technical vocabulary from **N4 to N2** (intermediate/advanced)

---

## 🛠️ Prerequisites
### Tools Used
This project uses:
- **[asdf](https://asdf-vm.com/guide/getting-started.html)**: Manage all your runtime versions with a single tool.
- **[PDM](https://pdm-project.org/)** – Modern Python dependency manager (alternative to `pip`/`poetry`).
- **[uv](https://github.com/astral-sh/uv)** – Ultra-fast package installer (compatible with PDM).
- **[direnv](https://direnv.github.io/)** – Auto-loads environment variables and virtualenv when entering the project directory.


## 🚀 Usage

### Initial setup

1. Clone the repository and enter the directory:

```bash
git clone https://github.com/scharret/sre-japanese-flashcards.git
cd sre-japanese-flashcards
```

2. Automatic environment activation with direnv

direnv will automatically load the environment (see .envrc).

- On first use:

```bash
direnv allow
```

3. Bootstrap the virtual environment and dependencies:

```bash
just create-env
```

---

### Generate the Anki deck

```bash
just build
```

✅ The file SRE_Japanese_Flashcards.apkg will be generated.

---

### Import into Anki

1. Open Anki
2. Go to File → Import
3. Select the generated .apkg file
4. The deck 🇯🇵 Japanese SRE Vocabulary (N4→N2) will appear in your list.

---

## 📂 Project structure

```text
├── .envrc                         # direnv configuration (auto env activation)
├── pyproject.toml                 # Project configuration (PDM)
├── sre_japanese_flashcards.py     # Main script
└── SRE_Japanese_Flashcards.apkg   # Generated deck (to import into Anki)

```
---

## 🔧 Customization

### ➕ Add new cards

1. Edit the sre_cards list in sre_japanese_flashcards.py:

```python
sre_cards = [
    {
        'Japonais': '新しい用語<br><span style="font-size: 16px;">ふりがな</span>',
        'Français': 'French translation',
        'ExempleJP': '例文 (日本語)',
        'ExempleFR': 'Example sentence (English)',
        'Catégorie': '🏷️ New Category',
    },
    # ...
```
]

2. Regenerate the deck:

```bash
just build
```

---

### 🎨 Customize the style

You can customize the appearance of the cards by editing:

- The css section of the model
- The qfmt (front) and afmt (back) templates

This allows you to:

- 🎨 Change colors (#ccc, #666, etc.)
- 🔠 Adjust font sizes
- 🧩 Modify the content layout

---

## 🎯 Why this deck?

- SRE / DevOps focused
  Technical vocabulary rarely covered by generic decks.

- Professional context
  Sentences tailored for incident response meetings and technical discussions.

- Effective learning
  Based on Anki’s spaced repetition system for long-term retention.

- Hands-on oriented
  Ideal for working in Japanese or bilingual engineering environments.

---

## 🙏 Contributing

1. Fork the project
2. Add or modify cards
3. Open a Pull Request

### 💡 Improvement ideas

- 🔊 Add audio files (pronunciation)
- 🔁 Expand with useful verbs (e.g. restart, monitor)
- 🌍 Add English translations for an international audience

---

## 📜 License

MIT – Free to use, modify, and share.

---

# 🇬🇧 Version française

Un deck Anki spécialement conçu pour les ingénieurs **Site Reliability Engineering (SRE)** et DevOps souhaitant maîtriser le vocabulaire technique japonais lié à :
- **Les incidents et urgences** (障害, 復旧, ダウンタイム...)
- **L'infrastructure** (インフラ, サーバー, クラウド...)
- **Le monitoring** (モニタリング, ログ, メトリクス...)
- **Le déploiement CI/CD** (デプロイ, ロールバック, パイプライン...)
- **Les réseaux et bases de données** (ネットワーク, データベース, トランザクション...)
- **Kubernetes et conteneurs** (ポッド, ノードプール, サービスメッシュ...)
- **La sécurité** (セキュリティ, 認証, 暗号化...)
- **Les phrases utiles en réunion** (現在のステータスは？, 根本的な原因は？...)

---

## 📦 Contenu du Deck
- **100+ cartes** organisées par catégories thématiques
- **Format optimisé** :
  - **Recto** : Termes japonais (Kanji + Kana) + Catégorie
  - **Verso** : Traduction française + Exemples contextuels (JP/FR)
- **Design clair** avec mise en forme HTML/CSS pour une meilleure lisibilité
- **Niveau** : Vocabulaire technique **N4 à N2** (intermédiaire/avancé)

---

## 🛠️ Prérequis
### Outils utilisés
Ce projet utilise :
- **[asdf](https://asdf-vm.com/guide/getting-started.html)** : Gérez toutes vos versions runtime avec un seul outil.
- **[PDM](https://pdm-project.org/)** : Gestionnaire de dépendances Python moderne (alternative à `pip`/`poetry`).
- **[uv](https://github.com/astral-sh/uv)** : Installeur de paquets ultra-rapide (compatible avec PDM).
- **[direnv](https://direnv.github.io/)** : Outil pour charger automatiquement les variables d'environnement et activer l'environnement virtuel lors de l'entrée dans le dossier du projet.

## 🚀 Utilisation

### 1️⃣ Configuration initiale

1. **Clonez le dépôt et entrez dans le dossier :**

```bash
git clone https://github.com/scharret/sre-japanese-flashcards.git
cd sre-japanese-flashcards
```

2. **Activation automatique de l’environnement avec `direnv`**

`direnv` chargera automatiquement l’environnement (voir `.envrc`).

- Lors de la première utilisation :

```bash
direnv allow
```

3. **Bootstrap du venv et des dependances :**

```bash
just create-env
```


---

### 2️⃣ Générer le deck Anki

```bash
just build
```

✅ Le fichier **`SRE_Japanese_Flashcards.apkg`** sera généré.

---

### 3️⃣ Importer dans Anki

1. Lancez **Anki**
2. Allez dans **Fichier → Importer**
3. Sélectionnez le fichier `.apkg` généré
4. Le deck **🇯🇵 Vocabulaire SRE Japonais (N4→N2)** apparaîtra dans votre liste

---

## 📂 Structure du projet

```text
.
├── .envrc                         # Configuration direnv (activation auto de l'env)
├── pyproject.toml                 # Configuration du projet (PDM)
├── sre_japanese_flashcards.py     # Script principal
└── SRE_Japanese_Flashcards.apkg   # Deck généré (à importer dans Anki)
```

---

## 🔧 Personnalisation

### ➕ Ajouter des cartes

1. Éditez la liste `sre_cards` dans `sre_japanese_flashcards.py` :

```python
sre_cards = [
    {
        'Japonais': '新しい用語<br><span style="font-size: 16px;">ふりがな</span>',
        'Français': 'Traduction française',
        'ExempleJP': '例文 (日本語)',
        'ExempleFR': "Phrase d'exemple (français)",
        'Catégorie': '🏷️ Nouvelle Catégorie',
    },
    # ...
]
```

2. Régénérez le deck :

```bash
just build
```

---

### 🎨 Modifier le style

Vous pouvez personnaliser l’apparence des cartes en modifiant :

- La section **`css`** du modèle
- Les templates **`qfmt`** (recto) et **`afmt`** (verso)

Cela permet de :
- 🎨 Changer les couleurs (`#ccc`, `#666`, etc.)
- 🔠 Ajuster la taille de police
- 🧩 Modifier la disposition du contenu

---

## 🎯 Pourquoi ce deck ?

- **Spécialisé SRE / DevOps**  
  Vocabulaire technique rarement couvert par les decks généralistes.

- **Contexte professionnel**  
  Phrases adaptées aux réunions d’incident et aux discussions techniques.

- **Apprentissage efficace**  
  Basé sur la répétition espacée d’Anki pour une mémorisation durable.

- **Orienté terrain**  
  Idéal pour travailler dans un environnement japonais ou bilingue.

---

## 🙏 Contribuer

1. **Forkez** le projet
2. Ajoutez ou modifiez des cartes
3. Ouvrez une **Pull Request**

### 💡 Idées d’améliorations

- 🔊 Ajouter des **fichiers audio** (prononciation)
- 🔁 Étendre aux **verbes utiles** (ex : redémarrer, surveiller)
- 🌍 Ajouter des **traductions anglaises** pour un public international

---

## 📜 Licence

MIT – Libre d’utiliser, modifier et partager.

