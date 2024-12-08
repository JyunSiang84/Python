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
    "[python]": {
        "editor.defaultFormatter": "ms-python.python", 
        "editor.formatOnSave": true,
　　　　　"editor.rulers": [80, 100]
    },
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    
    "files.trimTrailingWhitespace": true
}
```
#### "python.defaultInterpreterPath": Python 解釋器路徑設定
這行設定指向您專案中的虛擬環境（Virtual Environment）。虛擬環境可以讓每個專案擁有獨立的 Python 套件，避免不同專案之間的套件版本衝突。${workspaceFolder} 是 VS Code 的變數，代表您目前開啟的專案資料夾。
#### "[python]":
- "python.formatting.provider":有兩個選項
1. "ms-python.python":這是主要的 Python 擴充功能，提供基本的 Python 開發功能
2. "ms-python.black-formatter":這是專門的 Black 格式化工具擴充功能，只專注於代碼格式化功能，使用 Black 的格式化規則，程式碼格式化設定，使用 Black 作為 Python 程式碼的格式化工具。要注意與主要 Python 擴展產生衝突，有時會有版本相容性的問題。 (手動設置Black 配置設定細節可見 3.2.2)
- "editor.formatOnSave":
1. true:當你儲存 Python 檔案時，會自動進行格式化，這就像是一個自動整理桌面的助手，每次您完成工作後都會幫您整理工作環境。
2. false:需要手動格式化（通常是 Shift+Alt+F）
#### "python.linting": 
程式碼檢查設定，使用 Pylint 工具。檢查語法錯誤，還會檢查程式碼風格、可能的邏輯問題，甚至可能的優化建議。詳細細節可見[3.2.1 Pylint 配置]
1. "python.linting.enabled": true
- 這是啟用 Python 程式碼檢查的總開關
- 會在你編寫程式碼時即時檢查問題
- 會顯示紅色波浪線（錯誤）或黃色波浪線（警告）
2. "python.linting.pylintEnabled": true
指定使用 Pylint 作為程式碼檢查工具
#### "editor.rulers":
這個設定在編輯器中顯示兩條垂直參考線，分別在第 80 和第 100 列的位置。這些線提供視覺提示，幫助您控制程式碼行的長度。保持適當的行長度可以提高程式碼的可讀性，特別是在並排閱讀或在較小螢幕上檢視程式碼時。就像是在寫作時保持適當的段落長度，讓閱讀更輕鬆。
#### "files.trimTrailingWhitespace":
這個設定會自動移除每行結尾的多餘空白字元。
  
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
- Windows第一種: .\venv\Scripts\activate
- Windows第二種PowerShell: .\.venv\Scripts\Activate.ps1
- Windows第二種Command Prompt (cmd):.\.venv\Scripts\activate.bat
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
1. 首先按下快捷鍵開啟命令面板：
- Windows/Linux：Ctrl + Shift + P
- macOS：Cmd + Shift + P
2. 在命令面板中輸入 "Python: Select Interpreter"，您會看到一個下拉選單，列出所有可用的 Python 解釋器。在這裡，您應該能看到虛擬環境的 Python 解釋器，通常會標示為 ('venv': venv)。
3. 選擇您的虛擬環境解釋器後，VS Code 會在狀態列（左下角）顯示所選的 Python 版本，這樣您就能確認是否正在使用正確的解釋器。
##### 方法二：透過設定檔配置（適合團隊協作）
在專案的 .vscode/settings.json 檔案中添加以下設定：
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.pythonPath": "${workspaceFolder}/venv/bin/python"
}
```
這裡的路徑需要根據您的作業系統調整：
- Windows：使用 venv\\Scripts\\python.exe
- macOS/Linux：使用 venv/bin/python
##### 方法三：建立工作區設定（最靈活的方式）

#### 2.3.5. 確認虛擬環境是否正確啟用/結束使用虛擬環境：
- 確認虛擬環境是否正確啟用，有幾個方法可以確認您是否正在使用虛擬環境：
1. 觀察狀態列：在 VS Code 的左下角，您應該能看到 Python 解釋器的路徑，它應該指向您的虛擬環境。
2. 透過終端機確認：開啟 VS Code 的整合終端機（Ctrl+），您應該能看到提示符號前有 (venv)` 標記。
3. 執行測試程式：
```bash
import sys
print(sys.executable)  # 這會顯示當前使用的 Python 解釋器路徑
```
- 結束使用虛擬環境
```bash
deactivate
```
### 2.4 版本控制配置-Git 整合
設定 Git 整合功能：
1. 安裝 GitLens 擴充套件
2. 配置 .gitignore：
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# VS Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

# IDE
.idea/
*.swp
*.swo
```
3. 設定 Git 提交模板：
在 .git/config 中添加
```
# 在 .git/config 中添加
[commit]
    template = .gitmessage
```

## 3. 程式碼品質工具
### 3.1 安裝開發工具
在 Python 開發中，程式碼品質工具就像是我們的品質管理團隊，每個工具都扮演著特定且重要的角色。首先，讓我們在虛擬環境中安裝這些基本工具：
```bash
pip install pylint black isort pytest mypy
```
- pylint：程式碼分析員，負責檢查程式碼品質和風格
- black：格式化專家，自動調整程式碼排版
- isort：導入語句管理員，整理和組織導入語句
- pytest：測試工程師，確保程式碼功能正確
- mypy：型別檢查專家，防止型別相關錯誤
- 
### 3.2 程式碼風格與品質配置

#### 3.2.1 Pylint 配置（Linting）
Pylint 是我們的首席程式碼審查員。它不只檢查程式碼是否能運行，還會關注程式碼的品質和風格。
首先，在專案根目錄創建 .pylintrc 檔案：
```bash
# 方法一：讓 pylint 自動生成預設配置文件
pylint --generate-rcfile > .pylintrc

# 方法二：手動創建文件
touch .pylintrc  # Linux/macOS
# 或在 Windows PowerShell 中：
# New-Item .pylintrc -Type File
```
 .pylintrc 配置文件內容：
```ini
[MASTER]
# 忽略特定目錄，通常是不需要檢查的目錄
ignore=CVS,migrations,venv,tests

[MESSAGES CONTROL]
# 停用一些常見但不那麼重要的警告，讓我們能專注於更重要的問題
disable=C0111,  # missing-docstring：缺少文檔字符串
        C0103,  # invalid-name：變數命名規範
        C0303,  # trailing-whitespace：行尾空格
        W0611,  # unused-import：未使用的導入
        R0903,  # too-few-public-methods：公開方法太少
        R0913   # too-many-arguments：參數太多

[FORMAT]
# 程式碼格式設定，確保程式碼的可讀性
max-line-length=100
indent-string='    '

[BASIC]
# 允許的變數名稱，允許常用的簡短變數名
good-names=i,j,k,ex,Run,_,id,df,ax

[DESIGN]
# 設定程式碼結構的基本限制，防止函數或類變得太複雜
max-args=5          # 函數參數最大數量
max-attributes=7    # 類屬性最大數量
max-locals=15       # 局部變數最大數量
```
在 VS Code 的 settings.json 中配置 Pylint：
```json
"python.linting.enabled": true,
"python.linting.pylintEnabled": true,
```
這兩行設定是 Linting 的基礎開關。想像您有一位助手在您寫程式碼時即時檢查您的工作。
- 第一行是總開關，告訴 VS Code「是的，我想要即時程式碼檢查」。
- 第二行特別指定要使用 Pylint 作為檢查工具，就像選擇特定的助手來幫您檢查程式碼。

```json
"python.linting.pylintArgs": [
    "--errors-only",
    "--generated-members=numpy.* ,torch.* ,cv2.* ,cv.*"
],
```
這部分設定告訴 Pylint 如何執行檢查工作：
- "--errors-only" 表示 Pylint 只會報告實際的錯誤，而不會提示風格問題。這就像告訴助手「只告訴我可能導致程式出錯的問題，暫時不用在意程式碼是否漂亮」。
- "--generated-members=numpy.* ,torch.* ,cv2.* ,cv.*" 是一個特別重要的設定，它處理動態生成的程式碼成員。在使用 NumPy、PyTorch 或 OpenCV 這類函式庫時特別有用。這些函式庫會動態生成一些成員，Pylint 可能會誤判這些成員不存在。這個設定就像告訴助手「這些特定的程式庫會自動產生一些功能，不要把它們標記為錯誤」。

測試是否生效
```bash
pylint Pylint_Test.py --enable=all
# 這個命令告訴 Pylint 忽略所有的配置文件設定，使用最嚴格的檢查標準。
pylint Pylint_Test.py
# 配置文件設定，作為檢查標準。
```
基本使用方法：
```bash
# 基本使用
pylint your_file.py

# 或分析整個目錄
pylint your_directory/
```

#### 3.2.2 Black 配置（格式化）
Black 是我們的程式碼格式化專家，它使用一套固定的規則來確保程式碼風格的一致性。它的特點是不妥協——所有的程式碼都會遵循相同的格式標準。
Black 就像是一位固執但高效的美編，它會自動調整您的程式碼格式，使其符合一致的風格標準。它的特點是不講情面 - 用固定的規則確保所有程式碼都有相同的外觀。
```bash
# 安裝
pip install black

# 格式化單一檔案
black your_file.py

# 格式化整個目錄
black .

# 檢查而不修改（顯示會做什麼更改）
black --check your_file.py
```

#### 3.2.3 isort 配置（import 排序）
isort 專門整理您的 import 語句，就像一位專門整理書架的圖書管理員，確保所有的導入語句都按照邏輯順序排列。
```bash
# 安裝
pip install isort

# 排序單一檔案
isort your_file.py

# 排序整個目錄
isort .

# 檢查而不修改
isort --check-only your_file.py
```

#### 3.2.4 整合配置（pyproject.toml）
- pyproject.toml 是現代 Python 專案的中央配置文件，它可以統一管理多個開發工具的設定。這個文件應該放在專案根目錄：
- pyproject.toml 是一個現代的 Python 專案配置檔案，使用 TOML 格式（一種易於閱讀的配置檔案格式）。想像它像是一個食譜，告訴不同的工具該如何處理您的程式碼。

這個設定是關於自動整理您的 import 語句。每當您儲存檔案時，VS Code 會：
- 移除未使用的 import
- 按照特定規則排序 import 語句
- 合併相同來源的 import
這就像有位助手在您整理完文件後，自動幫您將參考文獻整理成正確的格式和順序。
```json
"editor.codeActionsOnSave": {
    "source.organizeImports": true
}
```


1. Black 工具的配置：
```toml
[tool.black]
line-length = 100                # 設定每行程式碼的最大長度為100個字符
target-version = ['py38']        # 指定要支援的 Python 版本
include = '\.pyi?$'             # 設定要格式化的檔案類型（.py 和 .pyi 檔案）
extend-exclude = '''
# A regex preceded with ^/ will apply only to files and directories
# in the root of the project.
^/foo.py  # exclude a file named foo.py in the root of the project
'''                             # 設定要排除的檔案
```
這部分告訴 Black（Python 的程式碼格式化工具）如何工作：
- 允許較長的行（100個字符而不是預設的88個）
- 針對 Python 3.8 版本優化格式化
- 可以排除特定檔案不被格式化

2. isort 工具的配置：
```toml
[tool.isort]
profile = "black"
multi_line_output = 3
```
這部分設定 isort（用於排序 import 語句的工具）：
- 確保它的格式化風格與 Black 一致
- 指定如何處理多行的 import 語句

3. 實際運用範例
格式化前：
```python
import sys,os
from datetime import datetime,date,timedelta
def very_long_function_name(parameter1,parameter2,parameter3,parameter4,parameter5,parameter6,parameter7):return parameter1+parameter2
```
使用這個配置後，代碼會被格式化為：
```python
from datetime import date, datetime, timedelta
import os
import sys

def very_long_function_name(
    parameter1,
    parameter2,
    parameter3,
    parameter4,
    parameter5,
    parameter6,
    parameter7,
):
    return parameter1 + parameter2
```

4. 如何使用
- 安裝所需工具： pip install black isort
- 在專案根目錄建立 pyproject.toml 檔案並加入配置
- 運行格式化：
```bash
black .          # 格式化所有 Python 檔案
isort .         # 排序所有檔案的 imports
```
這樣的配置有助於確保團隊中所有成員的程式碼風格保持一致，減少因為格式問題而產生的版本控制衝突。

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true

### 3.3 測試工具配置
#### 3.3.1 pytest 配置
pytest 是您的品質保證工程師，它幫助您確保程式碼的每個部分都能正確運作。它提供了一個直觀的方式來編寫和執行測試。
```bash
# 安裝
pip install pytest

# 建立測試檔案 test_example.py
def test_simple_function():
    assert 1 + 1 == 2

# 運行測試
pytest  # 運行所有測試
pytest test_specific_file.py  # 運行特定檔案
pytest -v  # 詳細輸出
pytest -k "test_name"  # 運行特定測試
```
pytest 是 Python 最受歡迎的測試框架之一，它提供了直觀的方式來編寫和執行測試：
```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_string_methods():
    assert "hello".upper() == "HELLO"
```

在 pytest.ini 中配置測試行為：
```ini
[pytest]
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --cov=. --cov-report=html
testpaths = tests
```
#### 3.3.2 mypy 配置(靜態類型檢查工具)
mypy 就像是一位型別檢查專家，它在程式碼運行之前就能找出可能的型別錯誤，幫助您避免執行時才發現的問題。
```bash
# 安裝
pip install mypy

# 基本使用
mypy your_file.py

# 檢查整個專案
mypy .
```
mypy 是強大的靜態型別檢查工具，它能在程式執行前找出潛在的型別錯誤：
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

# mypy 會檢查這類型別使用是否正確
result: str = greet("World")  # 正確
result: int = greet("World")  # mypy 會報錯
```

### 3.4 VS Code 整合設定
將所有工具整合到 VS Code 中，在 settings.json 中添加：
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.mypyEnabled": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "python.sortImports.args": ["--profile", "black"]
}
```
這些設定確保：
1. 儲存時自動格式化程式碼
2. 自動整理導入語句
3. 即時顯示程式碼問題
4. 進行型別檢查

在開發過程中，這些工具會共同工作，確保您的程式碼品質。它們就像是一個協調良好的團隊，每個成員都專注於自己的專業領域，共同為產出高品質的程式碼而努力。

## 4. 除錯配置
### 4.1 建立除錯設定
在 .vscode/launch.json 中添加更多除錯配置：
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true
        },
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_ENV": "development"
            },
            "args": ["run", "--no-debugger"]
        }
    ]
}
```

## 5. 實用快捷鍵
常用的 VS Code 快捷鍵：
- 格式化代碼：Shift+Alt+F（Windows）/ Shift+Option+F（macOS）
- 移動當前行：Alt+↑/↓（Windows）/ Option+↑/↓（macOS）
- 複製當前行：Shift+Alt+↑/↓（Windows）/ Shift+Option+↑/↓（macOS）
- 多光標選擇：Ctrl+D（Windows）/ Cmd+D（macOS）
- 開啟命令面板：Ctrl+Shift+P（Windows）/ Cmd+Shift+P（macOS）
- 開啟整合終端機：`Ctrl+``（Windows/macOS）
- 跳轉到定義：F12
- 查看所有參考：Shift+F12
- 重新命名符號：F2

## 6. 常見問題解決
### 6.1 路徑問題
常見路徑相關問題的解決方案。
#### 6.1.1 模組找不到
- 確保 PYTHONPATH 包含專案根目錄
- 在 .env 文件中設定 PYTHONPATH=${workspaceFolder}
#### 6.1.2 虛擬環境無法識別
- 確保虛擬環境路徑正確
- 重新選擇 Python 解釋器
- 檢查 settings.json 中的路徑設定
  
### 6.2 編碼問題
處理文件編碼問題：
1. 在 settings.json 中設定預設編碼：
   ```json
   {
    "files.encoding": "utf8",
    "files.autoGuessEncoding": true
   }
   ```
2. 對於特定檔案類型的編碼設定：
   ```json
   {
    "[python]": {
        "files.encoding": "utf8"
    }
   }
   ```
   
## 7. 建議的工作流程
高效的 Python 開發工作流程：

1. 專案初始化：
- 建立虛擬環境
- 安裝必要套件
- 設定 git 忽略檔案

2. 開發流程：
- 使用版本控制
- 遵循程式碼風格指南
- 定期執行測試
- 使用分支管理功能

3. 測試與品質保證：
- 編寫單元測試
- 執行程式碼分析
- 進行程式碼審查
- 自動化測試流程

4. 發布與部署：
- 更新版本號
- 產生變更記錄
- 建立發布標籤
- 執行部署流程

## 8. 進階配置  
### 8.1 自動化測試
配置自動化測試環境：
1. 設定 pytest.ini：
```ini
[pytest]
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --cov=. --cov-report=html
testpaths = tests
```

2. 設定持續整合：
- 建立 GitHub Actions 工作流程
- 設定測試覆蓋率報告
- 配置自動化部署流程
  
3. 在 VS Code 中設定測試探索：
   ```json
   {
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestArgs": [
        "tests"
    ]
   }
   ```
## 9. 持續整合/持續部署（CI/CD）配置
