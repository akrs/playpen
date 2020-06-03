__version__ = '0.1.0'

import ast
import operator as op
from typing import Dict, Union, Optional, Any

Number = Union[int, float]

OPS = {
    ast.Mult: op.mul, ast.Add: op.add,
}

def eval_numeric(expression : str, /, variables : Optional[Dict[str, Number]] = None) -> Union[bool, Number]:
    tree = ast.parse(expression, mode='eval')
    ops = {
        ast.Mult: op.mul, ast.Add: op.add, ast.Sub: op.sub, ast.Pow: op.pow,
        ast.USub: op.neg,
        ast.Lt: op.lt, ast.Gt: op.gt
    }
    _eval = _eval_builder(variables, ops)
    return _eval(tree)


def _eval_builder(variables : Dict[str, Any], ops : Dict[Any, Any]):
    def _compare(left, ops_list, comparators):
        if not ops[type(ops_list[0])](_eval(left), _eval(comparators[0])):
            return False

        if len(ops_list) == 1:
            return True

        return _compare(comparators[0], ops[1:], comparators[1:])

    def _eval(node):
        if type(node) is ast.Constant:
            return node.value
        if type(node) is ast.Name:
            return variables[node.id]

        if type(node) is ast.Expression:
            node = node.body

        if type(node) is ast.BinOp:
            return ops[type(node.op)](_eval(node.left), _eval(node.right))
        if type(node) is ast.UnaryOp:
            return ops[type(node.op)](_eval(node.operand))
        if type(node) is ast.Compare:
            return _compare(node.left, node.ops, node.comparators)

    return _eval
