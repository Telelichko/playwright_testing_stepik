Feature: Авторизация

@smoke @minor
Scenario: Проверка страницы
  Given на странице "login"
  Then URL содержит "/login"

@smoke @low
Scenario: Успешный вход
  Given на странице "login"
  When ввожу в "Поле_логин" текст "test@example.com" 
  And ввожу в "Поле_пароль" текст "password123"
  And кликаю "Кнопка_войти"
  Then URL содержит "/dashboard"

@smoke @low
Scenario Outline: Успешный вход множественный
  Given на странице "login"
  When ввожу в "Поле_логин" текст "<login>"
  And ввожу в "Поле_пароль" текст "<password>"
  And кликаю "Кнопка_войти"
  Then URL содержит "/dashboard"

  Examples:
    | login                | password     |
    | test@example.com     | password123  |
    | user2@example.com    | pass456      |
    | admin@example.com    | admin123     |
  