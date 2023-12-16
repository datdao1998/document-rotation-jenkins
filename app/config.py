class Config:
    def __init__(self):
        self.rotatenet_path = 'checkpoints/rotatenet.onnx'
        self.input_size = 512
        self.mean=[0.485, 0.456, 0.406]
        self.std=[0.229, 0.224, 0.225]

config = Config()