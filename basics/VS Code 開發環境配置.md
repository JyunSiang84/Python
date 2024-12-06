# VS Code Python 開發環境配置指南
## 1. 基礎安裝
### 1.1 下載與安裝 VS Code
Visual Studio Code（VS Code）是微軟開發的輕量級但功能強大的程式碼編輯器。安裝步驟如下：

1. 前往官方網站 https://code.visualstudio.com/ 下載適合您作業系統的版本
2. Windows 用戶：執行下載的安裝檔，建議在安裝時勾選「新增到右鍵選單」選項
3. macOS 用戶：將下載的 .dmg 檔案拖曳到應用程式資料夾
4. Linux 用戶：依據您的發行版本使用相應的套件管理器安裝

安裝完成後，第一次啟動時建議登入 Microsoft 帳號以同步設定。

### 1.2 Python 相關擴充套件
#### 1.2.1 必備的擴充套件包括：
1. Python（Microsoft 官方擴充套件）
- 提供基本的 Python 支援
- 包含除錯、智能提示、程式碼格式化等功能

2. Pylance
- Microsoft 的 Python 語言伺服器
- 提供更快的類型檢查和程式碼智能提示
  
#### 1.2.2 建議的額外擴充套件：
- Python Test Explorer：用於管理和執行單元測試
- Python Docstring Generator：自動生成文件字串
- Python Indent：智能縮排支援
- GitLens：增強的 Git 整合功能

## 2. 環境配置
### 2.1 Python 直譯器選擇
設定 Python 直譯器的步驟：

1. 確保系統已安裝 Python（建議使用 Python 3.8 或更新版本）
2. 在 VS Code 中使用快捷鍵 Ctrl+Shift+P（Windows/Linux）或 Cmd+Shift+P（macOS）
3. 輸入 "Python: Select Interpreter"
4. 選擇合適的 Python 版本

注意事項：
- 建議使用虛擬環境的 Python 直譯器
- 確保選擇的版本與專案需求相符
- 可以在狀態列查看當前使用的 Python 版本
   
### 2.2 工作區設定
在專案根目錄建立 .vscode 資料夾，包含以下檔案：
1. settings.json：控制編輯器的行為（如何編輯和檢視程式碼）
是 VS Code 的設定檔，就像是您的個人化偏好設定中心。在程式開發的環境中，它控制了編輯器的行為和外觀。
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true,
    "editor.rulers": [80, 100],
    "files.trimTrailingWhitespace": true
}
```
- "python.defaultInterpreterPath": Python 解釋器路徑設定
- "python.formatting.provider": 程式碼格式化設定，使用 Black 作為 Python 程式碼的格式化工具。它會自動調整您的程式碼格式，使其符合一致的風格。
- "python.linting": 程式碼檢查設定，使用 Pylint 工具。檢查語法錯誤，還會檢查程式碼風格、可能的邏輯問題，甚至可能的優化建議。
- "editor.formatOnSave": 讓 VS Code 在每次儲存檔案時自動進行格式化。這就像是一個自動整理桌面的助手，每次您完成工作後都會幫您整理工作環境。這確保了您的程式碼總是保持整潔的格式，不需要手動執行格式化命令。
- "editor.rulers":這個設定在編輯器中顯示兩條垂直參考線，分別在第 80 和第 100 列的位置。這些線提供視覺提示，幫助您控制程式碼行的長度。保持適當的行長度可以提高程式碼的可讀性，特別是在並排閱讀或在較小螢幕上檢視程式碼時。就像是在寫作時保持適當的段落長度，讓閱讀更輕鬆。
- "files.trimTrailingWhitespace": 這個設定會自動移除每行結尾的多餘空白字元。
  
2. launch.json：控制執行行為（如何執行和除錯程式）
錯指令書，就像是飛行前的檢查清單。它告訴 VS Code 當您要執行或除錯程式時該做什麼。這個檔案定義了不同的執行場景，就像不同的飛行計畫。
```json
{
    "version": "0.2.0",  // 配置版本號，確保與 VS Code 相容
    "configurations": [   // 包含所有執行配置的陣列
        {
            "name": "Python: Current File",  // 在除錯面板中顯示的名稱
            "type": "python",               // 指定使用的除錯器類型
            "request": "launch",            // 執行模式
            "program": "${file}",           // 要執行的程式
            "console": "integratedTerminal" // 輸出位置
        }
    ]
}
```

### 2.3 虛擬環境設定
首先，虛擬環境就像是為您的專案創建一個獨立的工作空間。想像您在一個大型辦公室中有自己的私人辦公室，所有的工具都是為您的專案量身定制的。
以下建立和管理虛擬環境引導。

#### 2.3.1. 在終端機中建立虛擬環境：
```bash
 python -m venv venv
```
這個指令中，第一個 venv 是 Python 的虛擬環境模組，第二個 venv 是您要創建的虛擬環境資料夾名稱。您可以選擇其他名稱，但 venv 是一個常見的慣例。

#### 2.3.2. 啟動虛擬環境：
成功啟動後，您會在命令提示字元前看到 (venv) 標記，這表示您現在在虛擬環境中工作。
- Windows: .\venv\Scripts\activate
- macOS/Linux: source venv/bin/activate

#### 2.3.3. 專案依賴：確保在激活虛擬環境後再安裝依賴
- 新專案建立(更新)依賴清單：pip freeze > requirements.txt
- 安裝現有專案的依賴：pip install -r requirements.txt
- 套件更新：
```bash
pip list --outdated  # 先檢查有哪些可更新的套件(檢查過時的套件)
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}  # Windows
pip freeze | cut -d'=' -f1 | xargs pip install --upgrade  # macOS/Linux
#要記得 更新 依賴清單
```
#### 2.3.4. 確保 VS Code 使用虛擬環境的 Python 解釋器
這個過程就像是告訴 VS Code 要使用哪個「工具箱」來執行您的 Python 程式。

##### 方法一：透過命令面板選擇（最直觀的方式）
##### 方法二：透過設定檔配置（適合團隊協作）
##### 方法三：建立工作區設定（最靈活的方式）

#### 2.3.5. 結束使用虛擬環境：
```bash
deactivate
```

## 3. 程式碼品質工具
### 3.1 安裝開發工具
### 3.2 Linting 配置
### 3.3 格式化工具配置

## 4. 除錯配置
### 4.1 建立除錯設定

## 5. 實用快捷鍵

## 6. 常見問題解決
### 6.1 路徑問題
### 6.2 編碼問題

## 7. 建議的工作流程

## 8. 進階配置
### 8.1 Git 整合
### 8.2 自動化測試
