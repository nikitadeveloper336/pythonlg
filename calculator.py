import ast

class EvalError(Exception):
    pass


ALLOWED_NODES = {
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Load,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow,
    ast.USub, ast.UAdd, ast.FloorDiv, ast.LShift, ast.RShift,
    ast.BitAnd, ast.BitOr, ast.BitXor, ast.Call, ast.Name, ast.Tuple,
    ast.List, ast.Tuple, ast.Constant, ast.Subscript, ast.Index,
    ast.Slice, ast.ListComp, ast.comprehension
}


def _check_node(node):
    for child in ast.walk(node):
        if type(child) not in ALLOWED_NODES:
            raise EvalError(f"Disallowed expression: {type(child).__name__}")


def evaluate(expr: str):
    """Safely evaluate a simple arithmetic expression.

    Supported: + - * / // % ** parentheses and numeric literals.
    """
    try:
        node = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise EvalError("Syntax error") from e

    _check_node(node)

    # Only allow numeric names like 'pi' if needed; none for now
    safe_names = {}

    try:
        return eval(compile(node, filename="<calc>", mode="eval"), {"__builtins__": {}}, safe_names)
    except Exception as e:
        raise EvalError(str(e)) from e


if __name__ == "__main__":
    print("calculator module: use from main.py or import evaluate()")
