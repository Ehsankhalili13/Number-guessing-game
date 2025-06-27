from flask import Flask, render_template, request, redirect, url_for
from random import randint

app = Flask(__name__)

chance = [15]  # تعداد فرصت‌های باقیمانده
number = []  # عدد تصادفی که باید حدس زده شود


@app.route("/")
def home():
    return render_template('index.html', chance=chance[0])


@app.route('/create_number')
def create_number():
    chance[0] = 15  # بازنشانی تعداد فرصت‌ها
    random_number = randint(1, 100)
    number.clear()
    number.append(random_number)
    return redirect(url_for("home"))


@app.route('/process_equal', methods=['POST'])
def equalprocess():
    try:
        if not number:  # اگر عددی برای حدس زدن وجود ندارد
            return '''<script>alert("لطفاً اول یک عدد ایجاد کنید!");
                    window.location.href = '/';</script>'''

        user_guess = int(request.form.get('number'))

        if chance[0] == 0:
            return '''<script>alert("شانس های شما به اتمام رسید.یک عدد جدید بسازید.");
                    window.location.href = '/';</script>'''
        elif user_guess == number[0]:
            number.clear()
            return '''<script>alert("درست حدس زدید! شما برنده شدید.");
                    window.location.href = '/';</script>'''
        elif user_guess > number[0]:
            chance[0] -= 1
            return '''<script>alert("عدد شما بزرگتر از عدد مورد نظر است!");
                    window.location.href = '/';</script>'''
        elif user_guess < number[0]:
            chance[0] -= 1
            return '''<script>alert("عدد شما کوچکتر از عدد مورد نظر است!");
                    window.location.href = '/';</script>'''
    except ValueError:
        return '''<script>alert("لطفاً یک عدد معتبر وارد کنید!");
                window.location.href = '/';</script>'''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

