'''
匯入工具

備註: 每次執行以下任一範例前，都要執行一次"匯入工具"的 cell
'''

# 操作 browser 的 API
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By

# 加入行為鍊 ActionChain (在 WebDriver 中模擬滑鼠移動、點繫、拖曳、按右鍵出現選單，以及鍵盤輸入文字、按下鍵盤上的按鈕等)
from selenium.webdriver.common.action_chains import ActionChains

# 加入鍵盤功能 (例如 Ctrl、Alt 等)
from selenium.webdriver.common.keys import Keys

# 強制等待 (執行期間休息一下)
from time import sleep

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消通知

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)


# 前往頁面
driver.get('https://www.musicca.com/zh/piano')

# 取得被拖曳的來源元素
# keywhite = driver.find_element(By.CSS_SELECTOR, "div.piano-wrapper")

# 目標元素 (放置的區域 共21個 0-20)
items = driver.find_elements(By.CSS_SELECTOR, "span.white-key")

# 建立行為鍊
ac = ActionChains(driver)

ac.move_to_element(items[11]).click()
ac.pause(0.2)
ac.move_to_element(items[9]).click()
ac.pause(0.2)
ac.move_to_element(items[9]).click()
ac.pause(0.5)
ac.move_to_element(items[10]).click()
ac.pause(0.2)
ac.move_to_element(items[8]).click()
ac.pause(0.2)
ac.move_to_element(items[8]).click()
ac.pause(0.5)
ac.move_to_element(items[7]).click()
ac.pause(0.2)
ac.move_to_element(items[8]).click()
ac.pause(0.2)
ac.move_to_element(items[9]).click()
ac.pause(0.2)
ac.move_to_element(items[10]).click()
ac.pause(0.2)
ac.move_to_element(items[11]).click()
ac.pause(0.2)
ac.move_to_element(items[11]).click()
ac.pause(0.2)
ac.move_to_element(items[11]).click()
ac.pause(0.6)

ac.move_to_element(items[11]).click()
ac.pause(0.2)
ac.move_to_element(items[9]).click()
ac.pause(0.2)
ac.move_to_element(items[9]).click()
ac.pause(0.5)
ac.move_to_element(items[10]).click()
ac.pause(0.2)
ac.move_to_element(items[8]).click()
ac.pause(0.2)
ac.move_to_element(items[8]).click()
ac.pause(0.5)
ac.move_to_element(items[7]).click()
ac.pause(0.2)
ac.move_to_element(items[9]).click()
ac.pause(0.2)
ac.move_to_element(items[11]).click()
ac.pause(0.2)
ac.move_to_element(items[11]).click()
ac.pause(0.2)
ac.move_to_element(items[9]).click()
ac.pause(0.2)

ac.perform()

sleep(5)

driver.quit()
