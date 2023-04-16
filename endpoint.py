from flask import Flask, request
import algorithms.simulated_annealing.simanneal_implementation as simanneal

api = Flask(__name__)

@api.route('/plot', methods=['POST'])
def recieve_plot():
    json_data = request.get_json()
    simanneal.main(json_data)
    return "works"

if __name__=="__main__":
    api.run(port=5001)