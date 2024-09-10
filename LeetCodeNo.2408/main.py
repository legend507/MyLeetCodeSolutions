# This is mainly a data storage problem.
# Decided to use dict to store the actual content of the tables.

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.table_names = names
        self.table_columns = columns
        self.table_contents = [None for _ in range(len(names))]
        self.table_insert_count = [0 for _ in range(len(names))]
        
    def insertRow(self, name: str, row: List[str]) -> None:
        idx = self.table_names.index(name)
        self.table_insert_count[idx] += 1
        # Table no content yet. Initialize.
        if self.table_contents[idx] == None:
            self.table_contents[idx] = {self.table_insert_count[idx]: row}
        else:
            self.table_contents[idx][self.table_insert_count[idx]] = row
        

    def deleteRow(self, name: str, rowId: int) -> None:
        idx = self.table_names.index(name)
        del self.table_contents[idx][rowId]
        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        idx = self.table_names.index(name)
        if self.table_contents[idx] == None:
            return None
        return self.table_contents[idx][rowId][columnId - 1]

        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)