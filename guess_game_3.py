from flask import Flask, request


app = Flask(__name__)

HTML_START = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>guess_game_3</title>
</head>
<body>
<h1>Imagine a number between 1 and 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</body>
</html>
"""


HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="too big">
    <input type="submit" name="user_answer" value="too small">
    <input type="submit" name="user_answer" value="you win">
    <input type="submit" name="user_answer" value="you won">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""


HTML_WIN = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Hooray! I guessed! Your number is {guess}</h1>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def guess_game_3():
    if request.method == 'GET':
        return HTML_START.format(1, 1001)
    else:
        min_range = int(request.form.get('min'))
        max_range = int(request.form.get('max'))
        print(min_range, max_range)
        user_answer = request.form.get('user_answer')
        guess = int(request.form.get('guess', 501))

        if user_answer == "too big":
            max_range = guess
        elif user_answer == "too small":
            min_range = guess
        elif user_answer == "you won":
            return HTML_WIN.format(guess=guess)

        guess = (max_range - min_range) // 2 + min_range

        return HTML.format(guess=guess, min=min_range, max=max_range)


if __name__ == '__main__':
    app.run(debug=True)
