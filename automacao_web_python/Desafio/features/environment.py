from main import debug
from util.config.driver import Driver

def before_scenario(context, scenario):
    if debug:
        print(f'DEBUG MDOE -> environment.py -> before_scenario {scenario} -> Iniciando driver')
    Driver.get_driver()

def after_scenario(context, scenario):
    if debug:
        print(f'DEBUG MDOE -> environment.py -> after_scenario {scenario} -> Encerrando driver')
    Driver.quit()