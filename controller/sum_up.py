from model.model_constants import MIN_OIL_LEVEL



class SumUp:
    def __init__(self) -> None:
        pass

    def print_statistics(self, model):
        current_oil = 0
        cells_with_minmal_oil = 0
        cells_contaminated = 0
        all_cells = model.shape[0] * model.shape[1]
        for y, row in enumerate(model.cells):
            for x, cell in enumerate(row):
                current_oil += cell.oil_level
                if cell.oil_level >= MIN_OIL_LEVEL:
                    cells_with_minmal_oil += 1
                if cell.was_significant:
                    cells_contaminated += 1

        print("Amount of oil spilled:", model.oil_spilled)
        print("Amount of oil left:", current_oil)
        print("Percentage of oil waporized or photolyzed: {:.2f}%".format(100 - current_oil / model.oil_spilled * 100))
        print("Surface that had oil: {}km2".format(cells_with_minmal_oil * 4))
        print("Surface that was strongly contaminated: {}km2".format(cells_contaminated * 4))
        print("Percentage of cells that had oil: {:.2f}%".format(cells_with_minmal_oil / all_cells * 100))
        print("Percentage of cells that were strongly contaminated: {:.2f}%".format(cells_contaminated / all_cells * 100))
