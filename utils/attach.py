import allure
from allure_commons.types import AttachmentType
from selene import browser
# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# логи
def add_logs():
    try:
        logs = browser.driver.get_log('browser')
        log_text = "\n".join(f"{log['level']} - {log['message']}" for log in logs)
    except Exception as e:
        log_text = f"Логи недоступны: {e}"
    allure.attach(log_text, 'browser_logs', AttachmentType.TEXT)

# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

# скринкаст
def add_video(browser):
    video_url = f"https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')