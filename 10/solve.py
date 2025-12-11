from ortools.sat.python import cp_model

lines = open("10/input.txt").read().splitlines()


def parse_line(line):
    indicators = line.split("[")[1].split("]")[0]
    wiring = [{int(x) for x in p.split(")")[0].split(",")} for p in line.split("(")[1:]]
    joltage = [int(x) for x in line.split("{")[1].split("}")[0].split(",")]
    return [c == "#" for c in indicators], wiring, joltage


def solve(targets, wiring, xor_mode=True):
    model = cp_model.CpModel()
    n_buttons, max_val = len(wiring), 1 if xor_mode else max(targets)
    buttons = [model.NewIntVar(0, max_val, f"b{i}") for i in range(n_buttons)]

    for pos, target in enumerate(targets):
        effects = [buttons[i] for i in range(n_buttons) if pos in wiring[i]]
        if xor_mode:
            aux = model.NewIntVar(0, n_buttons, f"sum_{pos}")
            model.Add(aux == sum(effects))
            model.AddModuloEquality(target, aux, 2)
        else:
            model.Add(sum(effects) == target)

    model.Minimize(sum(buttons))
    solver = cp_model.CpSolver()
    return (
        sum(solver.Value(b) for b in buttons)
        if solver.Solve(model) == cp_model.OPTIMAL
        else -1
    )


machines = [parse_line(l) for l in lines]
print(sum(solve(ind, wir) for ind, wir, _ in machines))
print(sum(solve(jolt, wir, xor_mode=False) for _, wir, jolt in machines))
