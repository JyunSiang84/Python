## 機器學習中「特徵」(Feature)的概念很重要：
### 1. 特徵的定義：
  - 是用來描述數據樣本的屬性或特性
  - 是模型學習的輸入變數
  - 決定了模型能學到什麼

### 2. 特徵的類型：
```Python
# 數值型特徵
age = 25
height = 170.5
weight = 65.3

# 類別型特徵
gender = "female"
color = "red"

# 布林型特徵
is_student = True
has_car = False
```
### 3. 特徵工程的常見處理：
```Pytho
from sklearn.preprocessing import StandardScaler

# 標準化數值特徵
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 類別特徵編碼
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
gender_encoded = encoder.fit_transform(['male', 'female', 'male'])
```

### 4. 特徵的重要性：
  - 影響模型性能
  - 決定模型的學習效果
  - 好的特徵可以簡化模型

### 5. 常見的特徵處理方法：
  - 特徵選擇：選擇最重要的特徵
  - 特徵縮放：將特徵值調整到相似範圍
  - 特徵組合：創建新的複合特徵
  - 特徵轉換：改變特徵的表示方式
實際例子：房價預測模型的特徵
```Pytho
house_features = {
    '面積': 100,  # 數值特徵
    '房間數': 3,  # 整數特徵
    '位置': '市中心',  # 類別特徵
    '有車位': True,  # 布林特徵
    '建築年份': 2010  # 時間特徵
}
```
### 6. 特徵工程的步驟：
  - 特徵提取：從原始數據中提取有用信息
  - 特徵處理：處理缺失值、異常值
  - 特徵轉換：將特徵轉換為模型可用的格式
  - 特徵創建：基於領域知識創建新特徵
