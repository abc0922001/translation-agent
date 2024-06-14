import os
import sys
import argparse
from translation_agent import translate

def main(source_lang, file_path):
    """
    執行翻譯操作。
    從指定的文件讀取文本，並翻譯成繁體中文（臺灣），並將結果輸出到新的文件中。
    """
    target_lang = "Traditional Chinese"
    country = "Taiwan"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_path)

    try:
        with open(full_path, encoding="utf-8") as file:
            source_text = file.read()
    except FileNotFoundError:
        print(f"Error: File not found - {full_path}")
        return
    except IOError as e:
        print(f"Error: Unable to read file - {full_path}. IOError: {e}")
        return

    print(f"Source text:\n\n{source_text}\n------------\n")

    translation = translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )

    print(f"Translation:\n\n{translation}")

    # 設定輸出檔案名稱
    base, ext = os.path.splitext(full_path)
    output_file_path = f"{base}_zh-TW{ext}"

    # 將翻譯結果寫入新文件
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(translation)
    except IOError as e:
        print(f"Error: Unable to write to file - {output_file_path}. IOError: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate text from a file to Traditional Chinese (Taiwan).")
    parser.add_argument("source_lang", type=str, help="Source language")
    parser.add_argument("file_path", type=str, help="Relative path to the text file")

    args = parser.parse_args()

    main(args.source_lang, args.file_path)
