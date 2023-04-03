from src.autonomous.apis import OpenAI


class TestOpenAI:

    def test_init(self):
        oai = OpenAI()

    def test_generate_image(self):
        oai = OpenAI()
        prompt = "The prettiest girl in the world named Natasha"
        oai.generate_image(prompt, size="256x256",
                           path="tests/unit/imgs/", n=1)
