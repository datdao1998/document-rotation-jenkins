import cv2
import numpy as np

from app.models.model import Model


class RotateNet(Model):
    def __init__(
        self,
        model_path,
        input_size=512,
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ):
        """Rotate model for document

        :param model_path: Path to onnx model
        :type model_path: str
        :param input_size: Input size of model, defaults to 512
        :type input_size: int, optional
        :param mean: Default mean to calculate, defaults to [0.485, 0.456, 0.406]
        :type mean: list, optional
        :param std: Default standard deviation, defaults to [0.229, 0.224, 0.225]
        :type std: list, optional
        """
        super().__init__(model_path)
        self.input_size = input_size
        self.mean = mean
        self.std = std

    def preprocess(self, image):
        """Preprocess for origin image

        :param image: Origin image
        :type image: np.array
        :return: Preprocessed image
        :rtype: np.array
        """
        input = cv2.resize(
            image, (self.input_size, self.input_size), interpolation=cv2.INTER_AREA
        )
        input = input.astype(np.float32) / 255.0
        input -= self.mean
        input /= self.std

        input = np.transpose(input, (2, 0, 1))
        input = np.expand_dims(input, axis=0)
        return input

    def execute(self, image):
        """Infer model onnx

        :param image: Input image
        :type image: np.array
        :return: Output image with angle
        :rtype: list
        """
        input = self.preprocess(image)

        output = self.infer(input)

        output = np.squeeze(np.argmax(output))
        cls = int(output)
        angle = "0"

        if cls == 1:
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            angle = "90"
        elif cls == 2:
            image = cv2.rotate(image, cv2.ROTATE_180)
            angle = "180"
        elif cls == 3:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            angle = "270"

        return image, angle
