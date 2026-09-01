# 77M Vessel Archive (`barge77m`)

[![Deploy 77M Site to GitHub Pages](https://github.com/burked9/barge77m/actions/workflows/deploy.yml/badge.svg)](https://github.com/burked9/barge77m/actions/workflows/deploy.yml)

A static archival website dedicated to the history, technical specifications, and community fundraising events of the **77M workboat fleet** (featuring *Hibernia* and expandable up to 7 vessels).

Built with **Pelican** and deployed automatically via **GitHub Actions** to **GitHub Pages**.

---

## 📁 Repository Structure

```text
barge77m/
├── pelicanconf.py              # Development configuration & navigation menu
├── publishconf.py              # Production publishing configuration (SITEURL)
├── requirements.txt            # Python dependencies (pelican, markdown)
├── .gitignore                  # Git ignore rules for build artifacts
├── README.md                   # Repository documentation & guide
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD deployment script
├── theme/                      # Custom Pelican visual theme (HTML & CSS)
│   ├── static/
│   │   ├── css/style.css       # Layout styles & responsive media rules
│   │   └── images/             # Splash banner (77M at Church Bay), logo, etc.
│   └── templates/              # HTML layout templates (home, page, base)
└── content/                    # Website markdown content
    ├── images/                 # Content photos (vessels, events, restoration)
    └── pages/                  # Markdown pages
        ├── home.md             # Landing page (Index)
        ├── fleet.md            # Fleet index (1-7 vessel slots)
        ├── hibernia.md         # Hibernia vessel profile & history
        ├── fundraisers.md      # Archival charity & non-profit event logs
        ├── contact.md          # Contact page
        └── vessels/
            └── vessel_template.md  # Template for adding new 77M class vessels
```

---

## 🚢 Scaling the Fleet (Adding Vessels 2 through 7)

This repository is structured to scale smoothly from 1 vessel up to 7 vessels:

1. **Duplicate Template**: Copy `content/pages/vessels/vessel_template.md` to `content/pages/<vessel_slug>.md`.
2. **Fill Metadata & Content**: Edit the title, specs, history, and photo links.
3. **Register in Fleet Index**: Open `content/pages/fleet.md` and update the corresponding entry under the **Archival Fleet Registry**.
4. **Optionally Add to Navigation**: If you want a direct header link, update `MENUITEMS` in `pelicanconf.py`.

---

## 🛠️ Local Development & Testing

### 1. Set Up Virtual Environment
```bash
cd /Users/danielburke/Documents/repositories/Projects/barge77m
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Build Site Locally
```bash
pelican content -s pelicanconf.py
```
Generated HTML output will be placed in `output/`.

### 3. Local Preview Server
```bash
pelican --listen
```
Open your browser to `http://localhost:8000`.

---

## 🚀 GitHub Pages Setup & Initial Push

When you are ready to publish:

### Step 1: Initialize Git & Commit
```bash
cd /Users/danielburke/Documents/repositories/Projects/barge77m
git init
git add .
git commit -m "Initial 77M vessel archive site setup"
git branch -M main
```

### Step 2: Link to Remote & Push
```bash
git remote add origin https://github.com/burked9/barge77m.git
git push -u origin main
```

### Step 3: Enable GitHub Pages in GitHub
1. Go to your repository on GitHub: `https://github.com/burked9/barge77m`
2. Navigate to **Settings > Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. The site will automatically build and publish to `https://burked9.github.io/barge77m/` (or your custom domain).
