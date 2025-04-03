from flask import Flask, render_template, redirect, url_for, request
import time
from forms import LoginForm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        data = fetch_linkedin_data(email, password)
        if data[0]:
            return redirect(url_for('company'))
    return render_template('login.html', form=form)

@app.route('/company', methods=['GET', 'POST'])
def company():
    if request.method == 'POST':
        company_name = request.form['company_name']
        limit = int(request.form['limit'])
        data = fetch_company_data(company_name, limit)
        return render_template('company_data.html', data=data)
    return render_template('company.html')

@app.route('/home')
def home():
    return "Hello, Flask!"

def fetch_linkedin_data(email, password):
    global driver
    driver = webdriver.Chrome()

    try:
        driver.get('https://www.linkedin.com/login')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        email_input = driver.find_element(By.ID, 'username')
        email_input.send_keys(email)
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        login_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
        login_button.click()
        return [True]
    except Exception as e:
        return [f"An error occurred: {e}", False]

def fetch_company_data(company_name, limit):
    try:
        company_name = company_name.lower()
        company_url = f"https://www.linkedin.com/company/{company_name}/people/"
        driver.get(company_url)
        time.sleep(5)
        scroll_pause_time = 2
        last_height = driver.execute_script("return document.body.scrollHeight")
        l = 0
        while True:
            if l >= limit:
                break
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            l += 1
            if new_height == last_height:
                break
            last_height = new_height

        name_elements = driver.find_elements(By.CSS_SELECTOR, ".org-people-profile-card__profile-title")
        title_elements = driver.find_elements(By.CSS_SELECTOR, ".lt-line-clamp.lt-line-clamp--multi-line")
        people = []
        for name, title in zip(name_elements, title_elements):
            people.append({
                "name": name.text,
                "title": title.text
            })
        return people

    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)