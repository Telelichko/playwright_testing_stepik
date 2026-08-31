Feature: Авторизация

@smoke
@timeout(1)
Scenario: Успешный вход
  Given на странице "login"
  When ввожу в "Поле_логин" текст "test@example.com" 
  And ввожу в "Поле_пароль" текст "password123"
  And кликаю "Кнопка_войти"
  Then URL содержит "/dashboard"

@smoke
@timeout(1)
Scenario Outline: Успешный вход
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
  