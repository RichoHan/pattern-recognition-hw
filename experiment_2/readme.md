## 前情提要
感覺我的情況比較特殊，需要的話我可以帶筆電demo給TA們看。

## 系統
Mac OSX Yosemite 10.10.2  
(原則上ubuntu應該也適用，Windows就不確定了)  

## 環境敘述
語言：  
Python  

Requirements：  
adaptfilt==0.2  
matplotlib==1.4.3  
mock==1.0.1  
nose==1.3.4  
numpy==1.9.2  
pyparsing==2.0.3  
python-dateutil==2.4.1  
pytz==2014.10  
scikit-learn==0.15.2  
scipy==0.15.1  
six==1.9.0  
wsgiref==0.1.2  

## 環境架設(視TA環境而定，想要獨立環境的話可以用virtualenv)
+ 安裝[pip](https://pip.pypa.io/en/latest/installing.html)  
+ 安裝[iPython](http://ipython.org/install.html)  
+ 直接從文字檔案內安裝相關package  
	
	`pip install -r requirements.txt  `

## 執行
+ 先在terminal進入code資料夾
+ 直接在ipython內執行experiment.py(for 3.1~3.3)來看分佈圖和分類結果  
```
# 先執行ipython進入interactive mode  
ipython  
# 執行experiment.py，此時會先跑出3.1-Perceptron Classifier的圖，關閉之後會再跑出Sum-of-error-squares和LMS的圖  
# 三張圖都跑完之後，會自動接續下一小題圖，故總共3*3=9張  
# 最後輸出每一小題、每一分類器的score(即coefficient of determination)  
run experiment.py  
```
