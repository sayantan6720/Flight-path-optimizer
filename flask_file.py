from Model.CheapestFlightSearcher import CheapestFlightSearcher
from Model.adjacencymatrix import AdjacencyMatrix


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    source = None
    destination = None
    path_to_reach_destination = []
    cost_to_reach_destination = 0
    if request.method == 'POST':
        if 'price' in request.form or 'ghg' in request.form:
            source = request.form.get('source')
            destination = request.form.get('destination')
            matrix = AdjacencyMatrix("Model/Flight Data - Sheet1.csv")
            airport_code_to_index_dict = {flight_label: index for index, flight_label in enumerate(matrix.get_vertices())}
            searcher = CheapestFlightSearcher(matrix.get_GHG_matrix() if('ghg' in request.form) else matrix.get_USD_matrix(), airport_code_to_index_dict)
            cost_to_reach_destination, _, path_to_reach_destination = searcher.search(source, destination)
        
            

      
    return render_template('UI.html', source=source, destination=destination, path=path_to_reach_destination, price=cost_to_reach_destination)

if __name__ == "__main__":
    app.run(debug=True)
