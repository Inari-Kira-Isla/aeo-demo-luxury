# aeo-demo-luxury

## Overview
這是一個針對奢侈品行業的 AEO（AI 搜尋引擎優化）示範範本，展示了如何結合 Schema.org、llms.txt 和 AI-friendly 語法來提升內容在 AI 系統中的可見性與理解度。專案旨在提供一個符合現代 AI 爬蟲和生成式 AI 應用友好的網站結構範例。

## Tech Stack
- **核心語言**: HTML5
- **標記語言**: Schema.org (JSON-LD)
- **AI 優化**: llms.txt
- **部署平台**: Vercel

## Architecture
- `index.html`: 首頁入口，包含主要的 AEO 結構化資料。
- `llms.txt`: 專為 AI 爬蟲設計的文字檔案，提供頁面內容摘要。
- `faq.html`: 常見問題頁面，展示 FAQ Schema 的應用。
- `assets/`: 靜態資源目錄（CSS, Images）。

## Commands
由於是靜態 HTML 專案，建置與部署指令主要依賴部署平台（如 Vercel）。
1. **本地開發**: 直接在瀏覽器開啟 `index.html` 或使用 VS Code Live Server。
2. **部署**: 推送至 GitHub 後，連結 Vercel 進行自動部署。

## Coding Style
- 使用語意化 HTML 標籤 (Semantic HTML) 以提升可訪問性與 SEO。
- Schema.org 資料應以 JSON-LD 格式嵌入 `<head>` 中。
- 確保程式碼結構清晰，便於 AI 解析內容邏輯。

## Important Rules
- **嚴禁**: 阻擋 AI 爬蟲存取關鍵內容 (如透過 robots.txt 禁止 llms.txt)。
- **必須**: 實作 JSON-LD 結構化資料。
- **必須**: 維護更新 `llms.txt` 以反映網站最新內容。