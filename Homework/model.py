import xml.etree.ElementTree as ET


class Record:
    def __init__(self, name, telephone, comment=None):
        self.name = name
        self.telephone = telephone
        self.comment = comment

    @property
    def comment(self):
        if self._comment is None:
            return " "
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    def to_element_tree(self):
        record = ET.Element("record")
        record_name = ET.Element("name")
        record_telephone = ET.Element("telephone")
        record_comment = ET.Element("comment")

        record.append(record_name)
        record.append(record_telephone)
        record.append(record_comment)

        record_name.text = self.name
        record_telephone.text = self.telephone
        record_comment.text = self.comment

        return record

    def __str__(self):
        text = f"{self.name} {self.telephone}"
        if self.comment is not None and len(self.comment) > 0:
            text += f" {self.comment}"
        return text

    @classmethod
    def from_element_tree(cls, elem):
        if type(elem) != ET.Element:
            return None
        name = None
        telephone = None
        comment = None
        for current in elem:
            if current.tag == "name":
                name = current.text
            elif current.tag == "telephone":
                telephone = current.text
            elif current.tag == "comment":
                comment = current.text

        return cls(name, telephone, comment)


class Phonebook:

    def __init__(self, file_name="text.txt"):
        self.__records = list()
        self.file_name = file_name
        self.reestablish()

    def reestablish(self):
        self.__records = list()
        try:
            tree = ET.parse(self.file_name)
        except:
            return
        records = tree.findall('record')
        for record in records:
            obj_record = Record.from_element_tree(record)
            self.__records.append(obj_record)

    def __str__(self):
        records = self.get_records()
        text = "|{0:3} | {1:15} | {2:15} | {3:30}|".format("#", "Имя", "Телефон", "Комментарий")
        count_ = len(text)
        text += "\n{0:30}".format(count_ * "-")
        for index, record in enumerate(records):
            current_name = record.name if record.name is not None else ''
            current_telephone = record.telephone if record.telephone is not None else ''
            current_comment = record.comment if record.comment is not None else ''
            text += "\n|{0:3} | {1:15} | {2:15} | {3:30}|".format(index + 1, current_name, current_telephone, current_comment)
        return text

    def __repr__(self):
        return self.__str__()

    def dump(self):
        elem = self.to_element_tree()
        tree = ET.ElementTree(elem)
        tree.write(self.file_name, encoding='utf-8')

    def to_element_tree(self):
        records = self.__records
        elem_phonebook = ET.Element("phonebook")
        for record in records:
            elem_record = record.to_element_tree()
            elem_phonebook.append(elem_record)
        return elem_phonebook

    def get_records(self):
        return self.__records

    def add_record(self, record):
        self.__records.append(record)
        self.dump()

    def validate_index(self, index):
        if type(index) != int:
            raise ValueError("Тип индекса должен быть целым числом")

        if (index > 0) and index > len(self.__records) - 1:
            raise ValueError("Индекс выходит за границы")
        elif index < 0 and abs(index) > len(self.__records):
            raise ValueError("Индекс выходит за границы")

    def __getitem__(self, item):
        self.validate_index(item)
        return self.__records[item]

    def __setitem__(self, key, value):
        if type(value) is not Record:
            raise ValueError("Тип значения должен быть объект класса Record")
        self.validate_index(key)
        self.__records[key] = value
        self.dump()

    def __delitem__(self, key):
        self.validate_index(key)
        del self.__records[key]
        self.dump()

    def __len__(self):
        return len(self.__records)



