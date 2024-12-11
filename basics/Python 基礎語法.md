# Python 基礎語法
這份文件詳細介紹 Python 的基礎語法，包含變數、運算子、流程控制、函式和模組等核心概念。每個概念都會搭配實際的程式碼範例。
## 1. 變數與資料型態
### 1.1 變數基礎概念
在 Python 中，變數就像是一個標籤或名稱，指向記憶體中儲存的資料。當我們建立一個變數時，Python 會在記憶體中配置適當的空間來儲存資料，並將變數名稱與這個記憶體位置建立連結。
#### 1.1.1 變數命名規則
了寫出清晰易讀的程式碼，且為了讓程式碼能夠執行， Python 變數命名有一些必須遵守的基本規則：
```python
# 變數命名規則示範
# 正確的命名方式
student_name = "小明"    # 使用下劃線連接（推薦）
studentAge = 20         # 駝峰式命名
_private = "私有變數"    # 底線開頭
student1 = "小華"      # 可以包含數字（但不能以數字開頭）
CONSTANT = 3.14        # 全大寫表示常數

# 錯誤的命名方式
1name = "小明"         # 不能以數字開頭
my-name = "小華"       # 不能使用連字號
class = "一年級"       # 不能使用 Python 保留字
```
##### 1. 基本規則（必須遵守）
- 變數名稱只能包含：
```python
# 合法的字元
alphabet = "abc"     # 英文字母（a-z，A-Z）
number_2 = 42        # 數字（0-9，不能放在開頭）
user_name = "test"   # 底線（_）
```
- 大小寫敏感：
```python
name = "小明"
Name = "小華"
NAME = "小陳"
# 這是三個不同的變數，因為 Python 會區分大小寫
```
- 不能使用保留字：
```python
# 這些都是錯誤的命名
if = "條件"          # if 是保留字
for = "迴圈"         # for 是保留字
class = "類別"       # class 是保留字
```

##### 2. 命名慣例（建議遵守）
- 一般變數使用小寫字母：
```python
# 建議的寫法
first_name = "John"
age = 25
total_score = 98

# 不建議的寫法
FirstName = "John"    # 這種寫法通常用於類別名稱
AGE = 25             # 這種寫法通常用於常數
```
- 多個單字的連接方式：
```python
# 建議使用底線連接（Snake Case）
user_name = "john_doe"
total_score = 100
current_user_age = 25

# 也可以使用駝峰式（Camel Case），但在 Python 中比較少見
userName = "john_doe"
totalScore = 100
currentUserAge = 25
```
- 常數命名使用全大寫：
```python
# 全大寫，單字間用底線連接
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = 'https://api.example.com'

# 模組層級的配置
class Config:
    DATABASE_URL = 'postgresql://localhost:5432'
    CACHE_TIMEOUT = 300
    DEBUG_MODE = True
```

##### 3. 特殊命名規則
- 私有變數命名：
```python
_private_var = "這是約定俗成的私有變數"
__really_private = "這是強制的私有變數"
```

- 特殊方法命名：
```python
__init__ = "建構子方法"
__str__ = "字串表示方法"
__len__ = "長度方法"
```

##### 4. 命名的最佳實踐
- 使用描述性名稱：
```python
# 好的命名
user_age = 25
total_score = 100
is_valid = True

# 不好的命名
a = 25
ts = 100
flag = True
```
- 避免使用容易混淆的名稱：
```python
# 避免使用
l = 1          # 小寫 L 容易與數字 1 混淆
O = 0          # 大寫 O 容易與數字 0 混淆
```
- 適當的名稱長度：
```python
# 太短的名稱可能不夠清楚
n = "John"              # 不清楚
name = "John"           # 較好

# 太長的名稱也不好
calculated_average_score_for_all_students_in_class = 85    # 太長
class_avg_score = 85    # 較好
```

##### 5. 進階－函式命名
當我們在寫函式時，通常希望函式名稱能夠清楚表達這個函式的行為：
```python
# 動詞 + 名詞的形式
def calculate_total(numbers):
    return sum(numbers)

def get_user_info(user_id):
    return user_database[user_id]

def validate_email(email):
    return '@' in email

# 布林函式通常用 is_、has_、can_ 開頭
def is_adult(age):
    return age >= 18

def has_permission(user, action):
    return user.permissions[action]

def can_access(user, resource):
    return check_permission(user, resource)
```

##### 6. 進階－類別相關命名
類別的命名有其特殊的慣例：
```python
# 類別名稱使用大寫開頭（PascalCase）
class UserAccount:
    def __init__(self, username):
        # 實例變數通常用底線連接（snake_case）
        self.user_name = username
        self._account_balance = 0  # 受保護的屬性
        self.__password = None     # 私有屬性

# 異常類別通常以 Error 結尾
class ValidationError(Exception):
    pass

class NetworkConnectionError(Exception):
    pass
```

##### 7. 進階－集合類型命名
當處理列表、字典等集合類型時，名稱應該反映其內容：
```python
# 列表通常使用複數形式
users = ['Alice', 'Bob', 'Charlie']
active_accounts = [acc for acc in accounts if acc.is_active]

# 字典可以用描述性的名稱
user_scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
config_settings = {'timeout': 30, 'retry_count': 3}

# 集合通常表達其元素的特性
valid_states = {'open', 'closed', 'pending'}
unique_visitors = {user.id for user in page_visits}
```

##### 8. 進階－迭代變數命名
在迴圈和推導式中的命名：
```python
# 單個字母用於簡單迭代
for i in range(5):
    print(i)

# 更具描述性的迭代變數
for user in users:
    process_user(user)

# 當有巢狀迴圈時
for row_index, row in enumerate(matrix):
    for col_index, value in enumerate(row):
        process_cell(row_index, col_index, value)
```

##### 9. 進階－回調函式命名
處理回調和事件處理時的命名：
```python
# 使用 on_ 前綴表示事件處理
def on_click(event):
    handle_click_event(event)

def on_data_received(data):
    process_incoming_data(data)

# 使用 handle_ 前綴表示處理程序
def handle_error(error_code):
    log_error(error_code)
```

##### 10. 進階－臨時變數命名
有時需要使用臨時變數：
```python
# 臨時變數要有意義
temp_user = copy.deepcopy(user)  # 而不是just用 temp
old_value = current_value        # 而不是用 x 或 y

# 在列表推導式中的臨時變數
squared_numbers = [num ** 2 for num in numbers]  # 而不是 [x**2 for x in numbers]
```

##### 11. 進階－單位相關命名
當變數涉及單位時：
```python
# 在名稱中包含單位資訊
timeout_seconds = 30
file_size_bytes = 1024
distance_km = 100
temperature_celsius = 25

# 時間間隔
retry_interval_ms = 500  # 毫秒
cache_duration_days = 7  # 天數
```

#### 1.1.2 變數作用域（全域與區域變數）
理解變數作用域對於寫出可維護和可靠的程式碼非常重要。它幫助我們：
- 避免命名衝突
- 控制變數的可見性
- 管理程式的狀態
- 實現資料封裝
##### 1. 變數作用域的基本概念
變數作用域（Variable Scope）決定了變數在程式中的可見性和生命週期。Python 主要有四種作用域，按照查找順序分為：
- Local（區域）：函式內的變數
- Enclosing（閉包）：巢狀函式中外層函式的變數
- Global（全域）：模組層級的變數
- Built-in（內建）：Python 內建的變數
這個順序也被稱為 LEGB 規則，讓我們通過例子來理解：
```python
# Built-in 作用域
# 像 print、len、str 這些都是內建作用域的名稱

# Global 作用域
global_var = "我是全域變數"

def outer_function():
    # Enclosing 作用域
    enclosing_var = "我是閉包變數"
    
    def inner_function():
        # Local 作用域
        local_var = "我是區域變數"
        print(local_var)      # 可以訪問區域變數
        print(enclosing_var)  # 可以訪問閉包變數
        print(global_var)     # 可以訪問全域變數

    inner_function()

outer_function()
```

##### 2. 區域變數（Local Variables）
區域變數是在函式內部定義的變數，只能在該函式內部使用：
```python
def calculate_sum():
    # x 和 y 是區域變數
    x = 10
    y = 20
    total = x + y
    return total

# print(x)  # 這會產生錯誤，因為 x 是區域變數
result = calculate_sum()
print(result)  # 這是可以的，因為我們使用了返回值
```
##### 3. 全域變數（Global Variables）
全域變數是在模組層級定義的變數，可以在整個模組中使用：
```python
# 全域變數
counter = 0

def increment_counter():
    global counter  # 宣告我們要使用全域變數
    counter += 1    # 修改全域變數
    print(f"計數器現在是: {counter}")

def print_counter():
    print(f"計數器的值是: {counter}")  # 讀取全域變數不需要 global 宣告

increment_counter()  # 輸出：計數器現在是: 1
print_counter()     # 輸出：計數器的值是: 1
```
##### 4. 變數遮蔽（Variable Shadowing）
當區域變數和全域變數同名時，區域變數會"遮蔽"全域變數：
```python
name = "全域小明"

def print_name():
    name = "區域小華"  # 這會建立一個新的區域變數
    print(f"函式內的名字是: {name}")  # 輸出：區域小華

print(f"全域的名字是: {name}")  # 輸出：全域小明
print_name()
print(f"全域的名字仍然是: {name}")  # 輸出：全域小明
```
##### 5. nonlocal 關鍵字
在巢狀函式中，如果要修改外層函式的變數，需要使用 nonlocal 關鍵字：
```python
def counter_function():
    count = 0
    
    def increment():
        nonlocal count  # 宣告我們要使用外層函式的變數
        count += 1
        return count
    
    return increment

counter = counter_function()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```
##### 6. 使用建議和最佳實踐
- 盡量避免使用全域變數：
```python
# 不好的做法
total = 0

def add_to_total(value):
    global total
    total += value

# 更好的做法
class Calculator:
    def __init__(self):
        self.total = 0
    
    def add_value(self, value):
        self.total += value
```
- 使用函式參數而不是全域變數：
```python
# 不好的做法
base_rate = 0.05

def calculate_interest(amount):
    return amount * base_rate

# 更好的做法
def calculate_interest(amount, rate=0.05):
    return amount * rate
```
- 返回值而不是修改全域狀態：
```python
# 不好的做法
result = []

def process_data(data):
    global result
    result = [x * 2 for x in data]

# 更好的做法
def process_data(data):
    return [x * 2 for x in data]

result = process_data([1, 2, 3])
```

##### 7. 變數作用域的應用場景
- 配置值和常數：
```python
# config.py
DATABASE_URL = "postgresql://localhost:5432"
MAX_CONNECTIONS = 100

def get_db_config():
    return {
        "url": DATABASE_URL,
        "max_connections": MAX_CONNECTIONS
    }
```
- 計數器和累加器：
```python
# config.py
DATABASE_URL = "postgresql://localhost:5432"
MAX_CONNECTIONS = 100

def get_db_config():
    return {
        "url": DATABASE_URL,
        "max_connections": MAX_CONNECTIONS
    }
```

#### 1.1.3 變數生命週期
理解變數的生命週期有助於我們：
- 更有效地管理記憶體
- 避免記憶體洩漏
- 寫出更高效的程式碼
- 理解並預防一些常見的程式錯誤
  
#### 1.1.4 變數記憶體管理

### 1.2 基本資料型態
#### 1.2.1 數值型態
- 整數 (int)
- 浮點數 (float)
- 複數 (complex)
#### 1.2.2 文字型態 (str)
#### 1.2.3 布林型態 (bool)

### 1.3 型態轉換
#### 1.3.1 隱含型態轉換
#### 1.3.2 顯式型態轉換
#### 1.3.3 安全的型態轉換實務

## 2. 運算子與運算式
### 2.1 算術運算子
#### 2.1.1 基本運算 (+, -, *, /, //, %)
#### 2.1.2 指數運算 (**)
#### 2.1.3 複合指派運算子 (+=, -=, *=, /=)

### 2.2 比較運算子
#### 2.2.1 值的比較 (>, <, >=, <=)
#### 2.2.2 相等性比較 (==, !=)
#### 2.2.3 is 與 is not 運算子

### 2.3 邏輯運算子
#### 2.3.1 and, or, not 運算子
#### 2.3.2 短路求值
#### 2.3.3 優先順序

### 2.4 位元運算子
位元與 (&)
位元或 (|)
位元反相 (~)
位移運算子 (>>, <<)

### 2.5 特殊運算子
成員運算子 (in, not in)
身分運算子 (is, is not)
三元運算子

## 3. 流程控制
### 3.1 條件判斷
#### 3.1.1 if 語句基礎
#### 3.1.2 elif 與多重條件
#### 3.1.3 else 子句
#### 3.1.4 巢狀條件判斷

### 3.2 迴圈結構
#### 3.2.1 for 迴圈
1. range() 函式使用
2. 迭代器與生成器
3. enumerate() 使用

#### 3.2.2 while 迴圈
1. 條件控制
2. 無限迴圈
3. while-else 子句

### 3.3 迴圈控制
#### 3.3.1 break 語句
#### 3.3.2 continue 語句
#### 3.3.3 pass 語句
#### 3.3.4 return 語句

### 3.4 例外處理
#### 3.4.1 try-except 基礎
#### 3.4.2 多重例外捕捉
#### 3.4.3 finally 子句
#### 3.4.4 自訂例外

## 4. 函式定義與呼叫
### 4.1 函式基礎
#### 4.1.1 函式定義語法
#### 4.1.2 回傳值
#### 4.1.3 參數傳遞
#### 4.1.4 文件字串 (Docstring)

### 4.2 參數類型
#### 4.2.1 位置參數
#### 4.2.2 關鍵字參數
#### 4.2.3 預設參數
#### 4.2.4 可變參數 (*args)
#### 4.2.5 可變關鍵字參數 (**kwargs)

### 4.3 函式進階概念
#### 4.3.1 匿名函式 (Lambda)
#### 4.3.2 遞迴函式
#### 4.3.3 裝飾器 (Decorator)
#### 4.3.4 生成器函式

### 4.4 函式最佳實務
#### 4.4.1 函式命名規範
#### 4.4.2 參數設計原則
#### 4.4.3 回傳值設計
#### 4.4.4 程式碼重用性

## 5. 模組導入與使用

### 5.1 模組基礎
#### 5.1.1 模組導入語法
#### 5.1.2 模組搜尋路徑
#### 5.1.3 模組重新載入
#### 5.1.4 __name__ 與 __main__

### 5.2 套件結構
#### 5.2.1 套件定義
#### 5.2.2 __init__.py 檔案
#### 5.2.3 子套件組織
#### 5.2.4 相對導入

### 5.3 常用標準函式庫
#### 5.3.1 數學相關 (math, random)
#### 5.3.2 時間處理 (datetime, time)
#### 5.3.3 系統相關 (os, sys)
#### 5.3.4 檔案處理 (json, csv)

### 5.4 第三方套件管理
#### 5.4.1 pip 使用方式
#### 5.4.2 虛擬環境建立
#### 5.4.3 requirements.txt
#### 5.4.4 套件版本控制
