import win32com.client

class PhotoshopAutomation:
    def __init__(self):
        self.app = win32com.client.Dispatch("Photoshop.Application")

    def open_document(self, file_path):
        doc = self.app.Open(file_path)
        return doc

    def save_document(self, doc, file_path):
        doc.SaveAs(file_path)

    def close_document(self, doc):
        doc.Close()

    def resize_image(self, doc, width, height):
        doc.ResizeImage(width, height)

    def crop_image(self, doc, left, top, right, bottom):
        doc.Crop([left, top, right, bottom])

    def add_text(self, doc, text, font_name, font_size, left, top, color, layer_name=None):
        text_layer = doc.ArtLayers.Add()
        text_layer.Kind = 2  # Set the layer kind to text
        text_layer.TextItem.Contents = text
        text_layer.TextItem.Position = [left, top]
        text_layer.TextItem.Font = font_name
        text_layer.TextItem.Size = font_size
        text_layer.TextItem.Color = color
        if layer_name is not None:
            text_layer.Name = layer_name

    def add_image(self, doc, file_path, left, top):
        new_layer = doc.ArtLayers.Add()
        new_layer.Place(file_path)
        new_layer.Translate(left, top)

    def delete_layer(self, doc, layer_name):
        layer = doc.ArtLayers.Item(layer_name)
        layer.Delete()

    def duplicate_layer(self, doc, layer_name, new_name):
        layer = doc.ArtLayers.Item(layer_name)
        layer.Duplicate(doc, 0)
        doc.ArtLayers.Item(layer_name + " copy").Name = new_name

    def get_all_layer_names(self, doc):
        layer_names = []
        for layer in doc.ArtLayers:
            layer_names.append(layer.Name)
        return layer_names

ps = PhotoshopAutomation()

doc = ps.open_document("D:\Pictures\Blindtest\Bleach\Abarai, Renji.jpg")

ps.add_text(doc, "Hello World!", "Arial", 72, 50, 50, [255, 0, 0], layer_name="My Text Layer")

ps.get_all_layer_names(doc)