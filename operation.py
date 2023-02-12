class Operation:

    def __init__(self, opr_id, opr_date, opr_amount, opr_description, opr_from, opr_to):
        self.opr_id = opr_id
        self.opr_date = opr_date
        self.opr_amount = opr_amount
        self.opr_description = opr_description
        self.opr_from = opr_from
        self.opr_to = opr_to

    def __repr__(self):
        return f'Операция № {self.id}'


