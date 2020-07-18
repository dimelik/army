from composite_unit import CompositeUnit


def print_composite_unit(composite_unit: CompositeUnit):
    print(composite_unit.name)
    for unit in composite_unit.units:
        if unit.is_composite() is True:
            print(unit.name + ' in ' + composite_unit.name)
            for child_unit in unit.units:
                print(child_unit.name + ' in ' + unit.name)
        else:
            print(unit.name + ' in ' + composite_unit.name)
