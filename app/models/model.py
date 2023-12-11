import onnxruntime


class Model:
    name = "Model"
    __version__ = "v1.0"

    def __init__(self, model_path):
        self.session = onnxruntime.InferenceSession(
            model_path, providers=["CPUExecutionProvider"]
        )

    def infer(self, input):
        if isinstance(input, list):
            ort_input = {
                self.session.get_inputs()[idx].name: x for idx, x in enumerate(input)
            }
        else:
            ort_input = {self.session.get_inputs()[0].name: input}

        output = self.session.run(None, ort_input)
        return output
