import pytest
from main import route_planner


# Normal tests (4)


def test_unweighted_simple_path():
    graph = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B"],
    }
    path, cost = route_planner(graph, "A", "C", weighted=False)
    assert path == ["A", "B", "C"]
    assert cost == 2


def test_weighted_simple_path():
    graph = {
        "A": [("B", 5)],
        "B": [("A", 5), ("C", 1)],
        "C": [("B", 1)],
    }
    path, cost = route_planner(graph, "A", "C", weighted=True)
    assert path == ["A", "B", "C"]
    assert cost == 6


def test_unweighted_start_equals_goal():
    graph = {"X": ["Y"], "Y": ["X"]}
    path, cost = route_planner(graph, "X", "X", weighted=False)
    assert path == ["X"]
    assert cost == 0


def test_weighted_start_equals_goal():
    graph = {"X": [("Y", 3)], "Y": [("X", 3)]}
    path, cost = route_planner(graph, "X", "X", weighted=True)
    assert path == ["X"]
    assert cost == 0


# Edge-case tests (3)


def test_missing_nodes_return_empty_and_none():
    graph_unweighted = {"A": ["B"], "B": ["A"]}
    graph_weighted = {"A": [("B", 2)], "B": [("A", 2)]}

    assert route_planner(graph_unweighted, "X", "B", False) == ([], None)
    assert route_planner(graph_unweighted, "A", "Y", False) == ([], None)
    assert route_planner(graph_weighted, "X", "B", True) == ([], None)
    assert route_planner(graph_weighted, "A", "Y", True) == ([], None)


def test_unweighted_no_path():
    graph = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"],
    }
    path, cost = route_planner(graph, "A", "D", weighted=False)
    assert path == []
    assert cost is None


def test_weighted_no_path():
    graph = {
        "A": [("B", 1)],
        "B": [("A", 1)],
        "C": [("D", 2)],
        "D": [("C", 2)],
    }
    path, cost = route_planner(graph, "A", "D", weighted=True)
    assert path == []
    assert cost is None


# Complex tests (3)


def test_unweighted_larger_graph():
    graph = {
        "S": ["A", "B"],
        "A": ["S", "C"],
        "B": ["S", "D"],
        "C": ["A", "E"],
        "D": ["B", "E"],
        "E": ["C", "D", "F"],
        "F": ["E"],
    }
    path, cost = route_planner(graph, "S", "F", weighted=False)
    assert path[0] == "S"
    assert path[-1] == "F"
    assert cost == 4  # S -> A/B -> C/D -> E -> F is 5 nodes => 4 edges


def test_weighted_choose_correct_shortest():
    graph = {
        "S": [("A", 1), ("B", 5)],
        "A": [("S", 1), ("C", 2)],
        "B": [("S", 5), ("C", 1), ("D", 7)],
        "C": [("A", 2), ("B", 1), ("E", 3)],
        "D": [("B", 7), ("E", 1)],
        "E": [("C", 3), ("D", 1)],
    }
    path, cost = route_planner(graph, "S", "E", weighted=True)
    assert path[0] == "S"
    assert path[-1] == "E"
    # One best path: S -> A -> C -> E: 1 + 2 + 3 = 6
    assert cost == 6


@pytest.mark.parametrize(
    "weighted_flag,expected_cost",
    [
        (False, 2),  # unweighted: S->X->Y (2 edges)
        (True, 8),   # weighted: S->Z->Y (3 + 5 = 8) better than S->X->Y (10 + 1 = 11)
    ],
)
def test_flag_changes_behavior(weighted_flag, expected_cost):
    unweighted_graph = {
        "S": ["X", "Z"],
        "X": ["S", "Y"],
        "Z": ["S", "Y"],
        "Y": ["X", "Z"],
    }
    weighted_graph = {
        "S": [("X", 10), ("Z", 3)],
        "X": [("S", 10), ("Y", 1)],
        "Z": [("S", 3), ("Y", 5)],
        "Y": [("X", 1), ("Z", 5)],
    }

    if weighted_flag:
        graph = weighted_graph
    else:
        graph = unweighted_graph

    path, cost = route_planner(graph, "S", "Y", weighted=weighted_flag)
    assert path[0] == "S"
    assert path[-1] == "Y"
    assert cost == expected_cost
