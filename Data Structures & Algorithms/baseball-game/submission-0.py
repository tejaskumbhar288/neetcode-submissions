class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        records = []

        for op in operations:
            if op == "+":
                if len(records) > 1:
                    first = records[-1]
                    second = records[-2]
                    newRecord = first + second
                    records.append(newRecord)

            elif op == "C":
                records.pop()

            elif op == "D":
                first = records[-1]
                newRecord = 2 * first
                records.append(newRecord)

            else:
                records.append(int(op))

        for record in records:
            total = total + record

        return total