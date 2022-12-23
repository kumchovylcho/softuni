from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for item in self.categories:
            if item.id == category_id:
                item.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for item in self.topics:
            if item.id == topic_id:
                item.topic = new_topic
                item.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        find_doc = [d for d in self.documents if d.id == document_id][0]
        if find_doc:
            find_doc.file_name = new_file_name

    def delete_category(self, category_id):
        find_category = [c for c in self.categories if c.id == category_id]
        if find_category:
            self.categories.remove(find_category[0])

    def delete_topic(self, topic_id):
        find_topic = [t for t in self.topics if t.id == topic_id]
        if find_topic:
            self.topics.remove(find_topic[0])

    def delete_document(self, document_id):
        find_document = [d for d in self.documents if d.id == document_id]
        if find_document:
            self.documents.remove(find_document[0])

    def get_document(self, document_id):
        find_document = [d for d in self.documents if d.id == document_id]
        if find_document:
            return find_document[0]

    def __repr__(self):
        result = [str(d) for d in self.documents]
        return '\n'.join(result)
