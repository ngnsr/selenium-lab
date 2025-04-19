# 🧪 Selenium Form Testing

Цей проєкт містить автоматизовані тести для веб-форми: [https://www.selenium.dev/selenium/web/web-form.html](https://www.selenium.dev/selenium/web/web-form.html)  
Тести реалізовано з використанням бібліотеки **Selenium** та мови **Python**.  
Кожен з трьох сценаріїв взаємодіє щонайменше з двома елементами та перевіряє результат взаємодії.

---

## ⚙️ Як запустити

### 1. Клонувати або завантажити репозиторій

```bash
git clone https://github.com/ngnsr/selenium-lab
cd selenium-lab
```

Або просто збережіть файл `main.py` з цього репозиторію.

### 2. Створити та активувати віртуальне середовище

```bash
python -m venv .venv
```

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```

- **Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Встановити залежності

```bash
pip install selenium webdriver-manager
```

---

## 🌐 Налаштування ChromeDriver

Selenium потребує **ChromeDriver**, сумісний з вашою версією Google Chrome.

### Варіант 1: Ручне налаштування

1. Дізнайтеся свою версію Chrome.
2. Завантажте ChromeDriver відповідної версії з:  
   [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
3. Додайте шлях до драйвера у `PATH`

---

## 🚀 Запуск тестів

Після налаштування всього, запустіть:

```bash
python3 main.py
```

Очікуваний результат — повідомлення у консолі про проходження трьох тестів:

```
✅ Тест 1 пройдено  
✅ Тест 2 пройдено  
✅ Тест 3 пройдено
```

---

## 📝 Структура файлів

```
selenium-form-tests/
├── main.py        # Файл з тестами
├── README.md       # Інструкція (цей файл)
└── .venv/          # Віртуальне середовище (ігнорується у Git)
```
---

## 💡 Порада

Тести використовують headless Chrome — браузер працює у фоновому режимі.  
Щоб побачити візуально, що відбувається, видаліть або закоментуйте рядок:

```python
options.add_argument("--headless")
```

у функції `setup_driver()`.
