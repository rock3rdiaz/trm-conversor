from conversor import Conversor
from data_handler import get_exchange_rate
from input_handler import get_user_input
from output_handler import show_result

exchange_rate = get_exchange_rate()
user_input = get_user_input()

if user_input is not None:
    conversor = Conversor(user_input["cantidad"], user_input["cantidad"], exchange_rate)

    if user_input["conversion"] == "1":
        result = conversor.convert_to_dollars()
        show_result(f"{user_input['cantidad']} pesos colombianos equivalen a {result} dólares.")
    else:
        result = conversor.convert_to_pesos()
        show_result(f"{user_input['cantidad']} dólares equivalen a {result} pesos colombianos.")

