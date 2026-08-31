Feature: Авторизация

@smoke
@timeout(1)
Scenario: Успешный вход
  Given на странице "login"
  When ввожу в "Поле_логин" текст "test@example.com" 
  And ввожу в "Поле_пароль" текст "password123"
  And кликаю "Кнопка_войти"
  Then URL содержит "/dashboard"
  