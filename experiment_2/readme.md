## 前情提要
感覺我的情況比較特殊，需要的話我可以帶筆電demo給TA們看。

## 系統
Mac OSX Yosemite 10.10.2  
(原則上ubuntu應該也適用，Windows就不確定了)  

## 環境敘述
語言：  
Python  

Requirements：  
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
	
	pip install -r requirements.txt  

## 執行
+ 先進到Code資料夾之中  
+ classifier.py內implement了四種classifier，不會需要執行  
+ Data generation需要在ipython內直接執行data_plot_a.py(for 2.2~2.5)和data_plot_b.py(for 2.7)來看分佈圖  
	
	<!-- 先執行ipython進入interactive mode -->  
	ipython  
	<!-- 執行data_plot_a.py，此時會先跑出2.2(a)的圖，關閉之後會再跑出下一小題的圖，共四張 -->  
	run data_plot_a.py  
	<!-- 執行data_plot_b.py，此時會先跑出X5的分佈圖，關閉之後會再跑出X5'的分佈圖 -->  
	run data_plot_b.py  
+ experiment_a.py implement了problem 2.2~2.5的b、c小題，顯示平均的classification error，並輸出結果至csv檔  
	
	<!-- 執行experiment_a.py -->  
	<!-- 透過main function裏的experiment_time變數，可以自行設定實驗次數 -->  
	python experiment_a.py  
+ experiment_b.py implement了problem 2.7的b、c小題，顯示平均的classification error，並輸出結果至csv檔  
	
	<!-- 執行experiment_b.py -->  
	<!-- 透過main function裏的experiment_time變數，可以自行設定實驗次數 -->  
	python experiment_b.py  
+ experiment_c.py implement了problem 2.8，顯示平均的classification error，並輸出結果至csv檔  
	
	<!-- 執行experiment_c.py -->  
	<!-- 透過main function裏的experiment_time變數，可以自行設定實驗次數 -->  
	python experiment_c.py  
