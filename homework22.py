team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
tasks_total = score_1 + score_2
team1_time = 1552.512
team2_time = 2153.31451
time_avg = (team1_time + team2_num) / tasks_total


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print('В команде Мастера кода участников: %s!' % team1_num)
print('В команде Волшебники данных участников: %s!' % team2_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

print('Команда Мастера кода решила задач: {}!'.format(score_1))
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Мастера кода решили задачи за {}с!'.format(team1_time))
print('Волшебники данных решили задачи за {}с!'.format(team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
