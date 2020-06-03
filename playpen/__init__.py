__version__ = '0.1.0'

import ast
import operator as op
from typing import Dict, Union, Optional, Any

Number = Union[int, float]

OPS = {
    ast.Mult: op.mul, ast.Add: op.add
}

def eval_numeric(expression : str, /, variables : Optional[Dict[str, Number]] = None) -> Union[bool, Number]:
    ops = {
        ast.Mult: op.mul, ast.Add: op.add, ast.Sub: op.sub, ast.Pow: op.pow
    }
    return _eval(ast.parse(expression, mode='eval'), variables, ops)


def _eval(tree, variables : Dict[str, Any], ops : Dict[Any, Any]) -> Any:
    if type(tree) is ast.Constant:
        return tree.value

    b = tree.body
    if type(b) is ast.BinOp:
        return ops[type(b.op)](_eval(tree.body.left, variables, ops),
                               _eval(tree.body.right, variables, ops))
