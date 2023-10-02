import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Создаем нечеткие переменные
power = ctrl.Antecedent(np.arange(0, 11, 1), 'power')
room_volume = ctrl.Antecedent(np.arange(0, 101, 1), 'room_volume')
ambient_temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'ambient_temperature')
desired_temperature = ctrl.Consequent(np.arange(0, 31, 1), 'desired_temperature')

# Задаем функции принадлежности
power['low'] = fuzz.trimf(power.universe, [0, 0, 5])
power['medium'] = fuzz.trimf(power.universe, [0, 5, 10])
power['high'] = fuzz.trimf(power.universe, [5, 10, 10])

room_volume['small'] = fuzz.trimf(room_volume.universe, [0, 0, 50])
room_volume['medium'] = fuzz.trimf(room_volume.universe, [0, 50, 100])
room_volume['large'] = fuzz.trimf(room_volume.universe, [50, 100, 100])

ambient_temperature['cool'] = fuzz.trimf(ambient_temperature.universe, [0, 0, 20])
ambient_temperature['moderate'] = fuzz.trimf(ambient_temperature.universe, [10, 20, 30])
ambient_temperature['warm'] = fuzz.trimf(ambient_temperature.universe, [20, 30, 40])

desired_temperature['cool'] = fuzz.trimf(desired_temperature.universe, [0, 0, 15])
desired_temperature['comfortable'] = fuzz.trimf(desired_temperature.universe, [10, 15, 25])
desired_temperature['warm'] = fuzz.trimf(desired_temperature.universe, [20, 30, 30])

# Создаем правила
rule1 = ctrl.Rule(power['low'] & room_volume['small'] & ambient_temperature['cool'], desired_temperature['cool'])
rule2 = ctrl.Rule(power['medium'] & room_volume['medium'] & ambient_temperature['moderate'], desired_temperature['comfortable'])
rule3 = ctrl.Rule(power['high'] & room_volume['large'] & ambient_temperature['warm'], desired_temperature['warm'])

# Создаем систему управления
temperature_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Создаем симуляцию
temperature_simulator = ctrl.ControlSystemSimulation(temperature_ctrl)

# Задаем входные значения
temperature_simulator.input['power'] = 7
temperature_simulator.input['room_volume'] = 75
temperature_simulator.input['ambient_temperature'] = 25

# Вычисляем результат
temperature_simulator.compute()

# Получаем выходное значение
print("Рекомендуемая температура:", temperature_simulator.output['desired_temperature'])

# Визуализация результатов
desired_temperature.view(sim=temperature_simulator)

# Построение графиков функций принадлежности
power.view(sim=temperature_simulator)
room_volume.view(sim=temperature_simulator)
ambient_temperature.view(sim=temperature_simulator)
desired_temperature.view(sim=temperature_simulator)

input()
