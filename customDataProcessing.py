import json

# Import CustomDataset class
class CustomDataset:
    def __init__(self, annotation_path, image_folder):
        self.annotation_path = annotation_path
        self.image_folder = image_folder

        # Read annotations from JSON file
        with open(self.annotation_path, 'r') as file:
            annotations_data = json.load(file)

        self.images = annotations_data['images']
        self.annotations = annotations_data['annotations']

    def get_annotations_for_image(self, file_name):
        image_id = None
        for image_info in self.images:
            if image_info['file_name'] == file_name:
                image_id = image_info['id']
                break

        if image_id is None:
            return []

        return [annotation for annotation in self.annotations if annotation['image_id'] == image_id]