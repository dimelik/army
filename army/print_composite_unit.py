from composite_unit import CompositeUnit


def print_composite_unit(composite_unit: CompositeUnit):
    for unit in composite_unit:
        print(unit.name + ' in ' + composite_unit.name)
        print_composite_unit(unit)
