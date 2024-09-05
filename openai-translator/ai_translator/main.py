from translator import PDFTranslator
from model import GLMModel, OpenAIModel
from utils import ArgumentParser, ConfigLoader, LOG
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    # by wy：python ai_translator/main.py --model_type OpenAIModel --openai_model gpt-4o-mini --file_format markdown --book tests/test.pdf
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    config_loader = ConfigLoader(args.config)

    config = config_loader.load_config()

    model_name = args.openai_model or config['OpenAIModel']['model']
    api_key = args.openai_api_key or config['OpenAIModel']['api_key']
    model = OpenAIModel(model=model_name, api_key=api_key)

    pdf_file_path = args.book or config['common']['book']
    file_format = args.file_format or config['common']['file_format']

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    translator = PDFTranslator(model)
    translator.translate_pdf(pdf_file_path, file_format)
