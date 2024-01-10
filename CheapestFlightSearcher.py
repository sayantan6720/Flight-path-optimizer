import copy
import heapq


class   CheapestFlightSearcher:

    def __init__(self, adjacency_matrix, airport_code_to_index_dict):
        self.__adjacency_matrix = adjacency_matrix
        self.__airport_code_to_index_dict = airport_code_to_index_dict
        self.__index_to_airport_code_dict = {v: k for k, v in airport_code_to_index_dict.items()}

    # todo: add time complexity analysis information
    def search(self, source_airport_code, destination_airport_code):
        if source_airport_code not in self.__airport_code_to_index_dict.keys():
            raise ValueError("Unable to find source airport code in the dict provided during initialization.")

        if destination_airport_code not in self.__airport_code_to_index_dict.keys():
            raise ValueError("Unable to find destination airport code in the dict provided during initialization.")

        # Get associated indices of source and destination airports
        source_index, destination_index = \
            self.__airport_code_to_index_dict[source_airport_code], self.__airport_code_to_index_dict[
                destination_airport_code]

        # Create min heap and visited set
        # By default, python orders by the first element in the tuple
        heap = [(0, source_index, [source_index])]  # [(cost,node,path)] 
        visited_nodes_dict = dict()  # { visited_node -> cost}
        path_dict = {i: [] for i in range(0, len(self.__adjacency_matrix[0]))}  # { node -> [shortest path] }

        # Run Dijkstras as long as the heap is not empty
        while heap:
            cost, current_node, path_list_of_current_node = heapq.heappop(heap)
            if current_node in visited_nodes_dict.keys():
                continue

            # Add node to the visit set
            visited_nodes_dict[current_node] = cost

            # Add the shortest path (containing all intermediary nodes) to path_dict
            path_dict[current_node] = path_list_of_current_node

            # Iterate through all adjacent nodes and add them to the heap
            for node in range(0, len(self.__adjacency_matrix[current_node])):
                if self.__adjacency_matrix[current_node][node] == -1:
                    continue  # there is no edge between the current node and the destination node
                path_list = copy.deepcopy(path_list_of_current_node)
                path_list.append(node)
                heapq.heappush(heap, (cost + self.__adjacency_matrix[current_node][node], node, path_list))

        # Get the cost of the cheapest path & the associated path
        cost_to_reach_destination = visited_nodes_dict[destination_index]
        path_to_reach_destination = \
            list(map(lambda airport_code_index: self.__index_to_airport_code_dict[airport_code_index],
                     path_dict[destination_index]))

        # Return cost and path as a tuple
        return cost_to_reach_destination, source_airport_code, path_to_reach_destination
