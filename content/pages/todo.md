Title: To-Do & Content Roadmap
Date: 2026-09-01
Save_as: pages/todo.html

# 77M Site Roadmap & Content Migration Mapping

This internal roadmap tracks the structure, tasks, and content migration mapping from the legacy `bargehibernia` archive.

---

## 📌 Phase 1: Structure & Design Tasks

- [x] Establish Heritage Boat Association header branding & title divider
- [x] Configure navigation menu bar (`Home`, `About`, `Publications & References`, `Vessels`, `Gallery`, `Contact`)
- [x] Create right-aligned thumbnail widgets for vessel cards (`vessels.html`)
- [x] Establish media folder structure (`content/images/thumbnails/` & `content/images/vessels/<vessel_slug>/<year>/`)
- [x] Add discreet footer roadmap link (`To-Do / Roadmap`)
- [ ] Finalize responsive photo grid layout for Gallery page (`gallery.html`)
- [ ] Polish About & Contact page design

---

## 🚢 Phase 2: Vessel Content Migration Mapping (`bargehibernia`)

Below is the mapping for transferring articles and media from the `bargehibernia` repository:

### 1. **Barge Hibernia** *(Priority 1)*
*   **Legacy Source:** `bargehibernia/pelican_site/content/vessels/hibernia.md` & `content/vessels/hibernia.md`
*   **Target Page:** [`content/pages/hibernia.md`]({filename}/pages/hibernia.md)
*   **Media Folder:** `content/images/vessels/hibernia/`
*   **Content Highlights to Copy:**
    - [ ] 1912 Portadown Foundry build history (63ft x 15ft Lagan lighter)
    - [ ] Early luxury pleasure conversion details (portholes, tiled concrete floors, fireplace, bath)
    - [ ] 1964 submergence on Upper Bann & 2003 "Mud Bucket" salvage history
    - [ ] Engine specifications (Bolinder -> 11L AEC Mandator -> Perkins 6354 with Perkins 4108 wing engine)
    - [ ] 2018 road transfer from Lough Neagh to Portaneena (Lough Ree)

### 2. **77M**
*   **Legacy Source:** `bargehibernia/pelican_site/content/vessels/77m.md`
*   **Target Page:** [`content/pages/77m.md`]({filename}/pages/77m.md)
*   **Media Folder:** `content/images/vessels/77m/`
*   **Content Highlights:**
    - [x] 1937 Ringsend Dockyard McMillen build (61'9" x 13'3")
    - [x] CIE commercial carrying & Banagher crews
    - [x] Priestman dredger conversion & Lister engine
    - [x] 2014 auction purchase & Church Bay restoration

### 3. **Little Knocknagow**
*   **Target Page:** [`content/pages/little_knocknagow.md`]({filename}/pages/little_knocknagow.md)
*   **Media Folder:** `content/images/vessels/little_knocknagow/`
*   **Content Highlights:**
    - [x] c.1890 Lanarkshire steam tug history
    - [x] Suir carrying trade & Dowleys fleet
    - [x] Richard Miller Grand Canal shortening & sailing masts
    - [x] 2004 transfer & Dromineer mooring

### 4. **68M** *(To Be Migrated)*
*   **Legacy Source:** `bargehibernia/pelican_site/content/vessels/68m.md`
*   **Target Page:** `content/pages/vessels/68m.md`
*   **Media Folder:** `content/images/vessels/68m/`

### 5. **ESB-1** *(To Be Migrated)*
*   **Legacy Source:** `bargehibernia/pelican_site/content/vessels/esb-1.md`
*   **Target Page:** `content/pages/vessels/esb1.md`
*   **Media Folder:** `content/images/vessels/esb1/`

### 6. **ESB-2** *(To Be Migrated)*
*   **Legacy Source:** `bargehibernia/pelican_site/content/vessels/esb-2.md`
*   **Target Page:** `content/pages/vessels/esb2.md`
*   **Media Folder:** `content/images/vessels/esb2/`

### 7. **45M / Rising 45M** *(To Be Migrated)*
*   **Legacy Source:** `bargehibernia/bargehibernia/content/memories/rising_45m.md`
*   **Target Page:** `content/pages/vessels/45m.md`
*   **Media Folder:** `content/images/vessels/45m/`

---
*Return to [Home]({filename}/pages/home.md) or explore [Vessels]({filename}/pages/fleet.md).*
