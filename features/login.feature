# language: ru
Функционал: Авторизация

  Сценарий: Успешный вход
    Given на странице "login"
    When ввожу в "login_email" текст "test@example.com" 
    And ввожу в "login_password" текст "password123"
    And кликаю "login_submit"
    Then URL содержит "/dashboard"
    